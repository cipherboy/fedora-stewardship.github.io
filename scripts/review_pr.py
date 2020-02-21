#!/usr/bin/python3

import argparse
import glob
import os
import re
import shutil
import subprocess as sp
import sys
import tempfile
import textwrap
import time

from typing import Dict, List, Tuple

from stewardship import parse_nevra, refresh_cache, get_b2s_mapping, get_s2b_mapping

LRU_CACHE_SIZE = None

DEFAULT_BLACKLIST = list(
    re.compile(pattern) for pattern in [
        # these packages' sources are missing
        "^elasticsearch$",
        "^fedora-business-cards$",
        "^publican-fedora$",
        # not interested in rebuilding ruby stuff because of jruby
        "^ruby.*",
        # no need to deal with this insanity
        "^texlive.*",
        # Orphaned in rawhide, broken due to weird test suite
        "^java-uuid-generator$"
    ]
)

if sys.version_info.minor < 5:
    print("python 3.5 or later is required for subprocess::run.")
    exit(1)

if sys.version_info.minor < 6:
    print("python 3.6 or later is required for f-strings.")
    exit(1)


def matches_regexes(package: str, regexes) -> bool:
    return any(regex.match(package) for regex in regexes)


class RetryError(Exception):
    pass


def retry(fun, *args, _retry_msg=None, _retry_times=None, _retry_delay=0, **kwargs):
    if _retry_times is None:
        condition = lambda _: True
    else:
        condition = lambda x: x < _retry_times

    tries = 0

    while condition(tries):
        try:
            return fun(*args, **kwargs)
        except KeyboardInterrupt:
            print("Cancelling upon user request.")
            raise
        except:
            tries += 1
            if _retry_msg is not None:
                print(_retry_msg)
            if _retry_delay != 0:
                time.sleep(_retry_delay)

    raise RetryError("Tried {} times, but failed.".format(_retry_times))


def copr_repo_exists(copr: str) -> bool:
    ret = sp.run(["copr-cli", "modify", copr], stdout=sp.PIPE, stderr=sp.STDOUT)
    return ret.returncode == 0


def copr_repo_create(copr: str, chroots: List[str]):
    description = "Repository for test-rebuilding packages in preparation for a pull request."

    cmd = [
        "copr-cli", "create",
        "--description", description,
        "--unlisted-on-hp", "on",
        "--delete-after-days", "30",
    ]

    # if no chroots were specified, default to fedora-rawhide-x86_64
    if not chroots:
        chroots.append("fedora-rawhide-x86_64")

    for chroot in chroots:
        cmd.extend(["--chroot", chroot])

    cmd.append(copr)

    ret = sp.run(cmd, stdout=sp.PIPE, stderr=sp.STDOUT)

    try:
        ret.check_returncode()
    except sp.CalledProcessError:
        print(ret.stdout.decode())
        raise


def build_package_from_git(copr: str, package: str, branch: str = "master", wait: bool = False):
    def clone():
        result = sp.run(
            ["fedpkg", "clone", package],
            stdout=sp.PIPE,
            stderr=sp.STDOUT)

        try:
            result.check_returncode()
        except sp.CalledProcessError:
            print(result.stdout.decode())
            raise

    retry(
        clone,
        _retry_msg="Cloning repository failed.",
        _retry_times=3,
        _retry_delay=5
    )

    os.chdir(package)

    if branch != "master":
        ret = sp.run(
            ["fedpkg", "switch-branch", branch],
            stdout=sp.PIPE,
            stderr=sp.STDOUT)

        try:
            ret.check_returncode()
        except sp.CalledProcessError:
            print(ret.stdout.decode())
            os.chdir("..")
            raise

    if os.path.exists("dead.package"):
        print(f"  - {package} skipped (retired)")
        os.chdir("..")
        return

    def sources():
        result = sp.run(
            ["fedpkg", "sources"],
            stdout=sp.PIPE,
            stderr=sp.STDOUT)

        try:
            result.check_returncode()
        except sp.CalledProcessError:
            print(result.stdout.decode())
            raise

    try:
        retry(
            sources,
            _retry_msg="Downloading sources failed.",
            _retry_times=3,
            _retry_delay=5
        )
    except RetryError as e:
        print(e)
        os.chdir("..")
        return

    def srpm():
        result = sp.run(
            ["fedpkg", "srpm"],
            stdout=sp.PIPE,
            stderr=sp.STDOUT)

        try:
            result.check_returncode()
        except sp.CalledProcessError:
            print(result.stdout.decode())
            raise

    try:
        retry(
            srpm,
            _retry_msg="Creating source package failed.",
            _retry_times=3,
            _retry_delay=5
        )
    except RetryError as e:
        print(e)
        os.chdir("..")
        return

    cmd = ["copr-cli", "build", copr, glob.glob("*.src.rpm")[0], "--background"]

    if not wait:
        cmd.append("--nowait")

    def build():
        result = sp.run(cmd, stdout=sp.PIPE, stderr=sp.STDOUT)

        try:
            result.check_returncode()
        except sp.CalledProcessError:
            print(result.stdout.decode())
            raise

    try:
        # if we don't care about the build result, at least make sure
        # the source package is uploaded successfully
        if not wait:
            retry(
                build,
                _retry_msg="Failed to upload source package to COPR.",
                _retry_times=3,
                _retry_delay=5
            )

            print(f"  - {package} successfully uploaded.")

        # if the build fails, don't try again
        else:
            build()

            print(f"  - {package} successfully built.")

    finally:
        os.chdir("..")


def build_package(copr: str, package: str, wait: bool = False):
    os.mkdir(package)
    os.chdir(package)

    def srpm():
        result = sp.run(
            ["dnf", "--quiet", "--installroot", "/tmp/dnf/",
             "--releasever", "rawhide",
             "--repo=rawhide", "--repo=rawhide-source",
             "download", "--source", package],
            stdout=sp.PIPE,
            stderr=sp.STDOUT)

        try:
            result.check_returncode()
        except sp.CalledProcessError:
            print(result.stdout.decode())
            raise

    try:
        retry(
            srpm,
            _retry_msg="Downloading source package failed.",
            _retry_times=3,
            _retry_delay=5
        )
    except RetryError:
        os.chdir("..")
        raise

    cmd = ["copr-cli", "build", copr, glob.glob("*.src.rpm")[0], "--background"]

    if not wait:
        cmd.append("--nowait")

    def build():
        result = sp.run(cmd, stdout=sp.PIPE, stderr=sp.STDOUT)

        try:
            result.check_returncode()
        except sp.CalledProcessError:
            print(result.stdout.decode())
            raise

    try:
        # if we don't care about the build result, at least make sure
        # the source package is uploaded successfully
        if not wait:
            retry(
                build,
                _retry_msg="Failed to upload source package to COPR.",
                _retry_times=3,
                _retry_delay=5,
            )

            print(f"  - {package} successfully uploaded.")

        # if the build fails, don't try again
        else:
            build()

            print(f"  - {package} successfully built.")

    finally:
        os.chdir("..")


def build_fork(copr: str, user: str, package, branch: str = "master"):
    url = f"https://src.fedoraproject.org/forks/{user}/rpms/{package}.git"

    def clone():
        result = sp.run(
            ["git", "clone", url, f"{package}-fork"],
            stdout=sp.PIPE,
            stderr=sp.STDOUT)

        try:
            result.check_returncode()
        except sp.CalledProcessError:
            print(result.stdout.decode())
            raise

    retry(
        clone,
        _retry_msg="Failed to clone repository.",
        _retry_times=3,
        _retry_delay=5,
    )

    os.chdir(f"{package}-fork")

    if branch != "master":
        ret = sp.run(
            ["fedpkg", "switch-branch", branch],
            stdout=sp.PIPE,
            stderr=sp.STDOUT)

        try:
            ret.check_returncode()
        except sp.CalledProcessError:
            print(ret.stdout.decode())
            os.chdir("..")
            raise

    def srpm():
        regex = re.compile("f[0-9][0-9]")

        if branch == "master":
            srpm_cmd = ["fedpkg", "srpm"]
        elif regex.match(branch):
            srpm_cmd = ["fedpkg", "srpm"]
        else:
            srpm_cmd = ["fedpkg", "--release", "f31", "srpm"]

        result = sp.run(
            srpm_cmd,
            stdout=sp.PIPE,
            stderr=sp.STDOUT)

        try:
            result.check_returncode()
        except sp.CalledProcessError:
            print(result.stdout.decode())
            raise

    try:
        retry(
            srpm,
            _retry_msg="Downloading sources or creating source package failed.",
            _retry_times=3,
            _retry_delay=5
        )
    except RetryError:
        os.chdir("..")
        raise

    cmd = ["copr-cli", "build", copr, glob.glob("*.src.rpm")[0]]

    def build():
        result = sp.run(cmd, stdout=sp.PIPE, stderr=sp.STDOUT)

        try:
            result.check_returncode()
        except sp.CalledProcessError:
            print(result.stdout.decode())
            raise

    try:
        build()

        print(f"  - {package} successfully built.")

    finally:
        os.chdir("..")


def parse_filename(nevrax: str) -> Tuple[str, str, str, str, str]:
    nevra, x = nevrax.rsplit(".", 1)
    n, e, v, r, a = parse_nevra(nevra)

    return n, e, v, r, a


def get_all_dependents(
        package: str,
        blacklist: list,
        b2s: Dict[str, str],
        no_recursive: bool
) -> List[str]:
    """
    This function queries dnf for reverse dependencies of a package and returns
    a list of source package names that depend on it.
    """

    cmd = ["dnf", "--quiet", "--installroot", "/tmp/dnf/", "--releasever", "rawhide",
           "repoquery", "--repo=rawhide", "--repo=rawhide-source",
           "--arch", "x86_64", "--arch", "noarch", "--arch", "src",
           "--alldeps"]

    if not no_recursive:
        cmd.append("--recursive")

    cmd.extend(["--whatrequires", package])

    def query():
        ret = sp.run(cmd, stdout=sp.PIPE, stderr=sp.STDOUT)

        try:
            ret.check_returncode()
        except sp.CalledProcessError:
            print(ret.stdout.decode())
            raise

        deps: List[str] = ret.stdout.decode().splitlines()

        requires: List[str] = list()
        buildrequires: List[str] = list()

        all_deps = set()

        for dep in deps:
            n, e, v, r, a = parse_nevra(dep)

            if matches_regexes(n, blacklist):
                continue

            if a == "src":
                buildrequires.append(n)
            else:
                requires.append(n)

        for br in buildrequires:
            all_deps.add(br)

        for req in requires:
            src = b2s[req]
            all_deps.add(src)

        ret = list()

        for dep in all_deps:
            ret.append(dep)

        ret.sort()
        return ret

    return retry(
        query,
        _retry_msg="dnf subprocess failed, trying again.",
        _retry_times=3,
        _retry_delay=5,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""\
            This script can be used to automatically build a forked package (with
            or without Pull Request) and rebuild all its dependent packages against
            the new version, in a COPR repository.
            
            Note that, by default, some packages are excluded from being rebuilt.
            This includes ruby gems (unnecessary), elasticsearch (broken repo),
            and all eclipse packages (broken). Additional packages can be blacklisted
            by using the "--exclude" flag.
            """),
        epilog=textwrap.dedent("""\
            The "--exclude" arguments are interpreted as regular expressions with the
            syntax accepted by python's "re" module.
            
            Examples:
            - only one package should be matched: "^elasticsearch$"
            - exclude ruby gems (default): "^rubygem-*"
            """)
    )

    parser.add_argument("copr", action="store", help="copr repo to use (and create)")
    parser.add_argument("project", action="store", nargs="+",
                        help="projects to build (in order); format: USER:REPO:BRANCH")

    parser.add_argument("--wait", "-w", action="store_const", const=True, default=False,
                        help="wait for COPR builds to succeed")
    parser.add_argument("--skip-self", "-s", action="store_const", const=True, default=False,
                        help="skip build of the forked packages themselves")
    parser.add_argument("--dep-offset", "-d", action="store", type=int, default=0,
                        help="specify offset of build dependencies to rebuild")
    parser.add_argument("--no-blacklist", "-b", action="store_const", const=True, default=False,
                        help="disable built-in package blacklist")
    parser.add_argument("--exclude", "-x", action="append", default=[],
                        help="regex for packages to exclude from rebuilding")
    parser.add_argument("--from-git", action="append", default=[],
                        help="regexes for packages to build from git")
    parser.add_argument("--no-recursive", "-n", action="store_const", const=True, default=False,
                        help="only rebuild directly dependent packages")
    parser.add_argument("--chroot", action="append", default=[],
                        help="create COPR project with the specified chroot")

    args = vars(parser.parse_args())

    copr = args["copr"]
    project_list: List[str] = args["project"]

    wait = args["wait"]
    skip = args["skip_self"]
    offset = args["dep_offset"]
    noblacklist = args["no_blacklist"]
    exclude = args["exclude"]
    from_git = args["from_git"]
    no_recursive = args["no_recursive"]
    chroots = args["chroot"]

    if noblacklist:
        blacklist = []
    else:
        blacklist = list(re.compile(pattern) for pattern in exclude) + DEFAULT_BLACKLIST

    if from_git:
        from_gits = list(re.compile(pattern) for pattern in from_git)
    else:
        from_gits = []

    projects = list()
    for entry in project_list:
        parsed = entry.split(":")

        if len(parsed) != 3:
            print(f"Project entry '{entry}' cannot be parsed.")
            print("Arguments must be of the form: USER:PACKAGE:BRANCH")
            return 1

        user, package, branch = parsed
        projects.append({"user": user, "package": package, "branch": branch})

    if not copr_repo_exists(copr):
        copr_repo_create(copr, chroots)
        print("Created COPR repository.")

    print()
    print("Blacklisted packages:")
    for item in blacklist:
        print(f"  - {item.pattern}")
    print()

    print("Querying all dependent packages.")
    repos = ["rawhide", "rawhide-source"]
    refresh_cache(repos)

    b2s = get_b2s_mapping(repos)
    s2b = get_s2b_mapping(b2s)

    dep_set = set()
    for project in projects:
        for binary in s2b[project["package"]]:
            for dep in get_all_dependents(binary, blacklist, b2s, no_recursive):
                dep_set.add(dep)

    deps = list()
    for dep in dep_set:
        deps.append(dep)
    deps.sort()

    # remove packages that are going to be rebuilt anyway from dependencies
    for project in projects:
        if project["package"] in deps:
            deps.remove(project["package"])

    # do the rest in a temporary directory
    tempdir = tempfile.mkdtemp(prefix=f"{copr.replace('/', '-')}-review-")
    print(f"Created temporary directory: {tempdir}")

    os.chdir(tempdir)

    print()

    try:
        if not skip:
            for project in projects:
                user = project["user"]
                package = project["package"]
                branch = project["branch"]

                print(f"Building forked package: {user}/{package}:{branch}")
                build_fork(copr, user, package, branch)
        else:
            print("Skipping build of forked packages.")

        for num, dep in enumerate(deps[offset:], start=offset):
            if not matches_regexes(dep, blacklist):
                if not matches_regexes(dep, from_gits):
                    print(f"Building dependent package {num}: {dep}")
                    build_package(copr, dep, wait)
                else:
                    print(f"Building dependent package {num}: {dep} (from git)")
                    build_package_from_git(copr, dep, "master", wait)
            else:
                print(f"Skipping rebuild of: {dep}")

    except sp.CalledProcessError or OSError or IOError:
        print("Failed to build packages.")
        print("Resume by passing '--skip-self' and '--dep-offset' arguments.")
        return 1

    print()

    # make sure not to delete stuff we didn't create
    if tempdir.startswith(f"/tmp/{copr.replace('/', '-')}-review-"):
        print("Deleting temporary directory.")
        shutil.rmtree(tempdir)
    else:
        print("Something went wrong. Not deleting temporary directory.")
        print("Expected a path with prefix: {}".format(f"/tmp/{copr.replace('/', '-')}-review-"))
        print("Actual path: {}", tempdir)
        raise RuntimeError

    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        exit(0)
