import json
import subprocess
import time

from typing import Dict, List, Set, Tuple

LRU_CACHE_SIZE = None


class RetryError(Exception):
    pass


def retry(message: str = None, times: int = None, delay: int = 0):
    def wrap(f):
        def retry_wrapped(*args, **kwargs):
            if times is None:
                condition = lambda _: True
            else:
                condition = lambda x: x < times

            tries = 0

            while condition(tries):
                try:
                    return f(*args, **kwargs)
                except KeyboardInterrupt:
                    print("Cancelling upon user request.")
                    raise
                except:
                    tries += 1

                    if message is not None:
                        print(message)
                    if delay != 0:
                        time.sleep(delay)
            raise RetryError("Tried {} times, but failed.".format(times))

        return retry_wrapped

    return wrap


def is_blacklisted(package: str, blacklist) -> bool:
    return any(regex.match(package) for regex in blacklist)


def parse_nevra(nevra: str) -> Tuple[str, str, str, str, str]:
    nevr, a = nevra.rsplit(".", 1)
    n, ev, r = nevr.rsplit("-", 2)

    if ":" in ev:
        e, v = ev.split(":")
    else:
        e = "0"
        v = ev

    return n, e, v, r, a


@retry(message="Failed to refresh dnf cache.", times=3, delay=5)
def refresh_cache(repos: List[str]):
    cmd = ["dnf", "--quiet", "--installroot", "/tmp/dnf/", "--releasever", "rawhide"]

    for repo in repos:
        cmd.extend(["--repo", repo])

    cmd.extend(["makecache", "--refresh"])

    ret = subprocess.run(cmd, stdout=subprocess.PIPE)
    ret.check_returncode()


@retry(message="Failed to query dnf.", times=3, delay=5)
def get_b2s_mapping(repos: List[str]) -> Dict[str, str]:
    cmd = ["dnf", "--quiet", "--installroot", "/tmp/dnf/", "--releasever", "rawhide", "repoquery"]

    for repo in repos:
        cmd.extend(["--repo", repo])

    cmd.extend([
        "--all",
        "--arch", "x86_64",
        "--arch", "noarch",
        "--queryformat", '"%{name}": "%{source_name}"'
    ])

    ret = subprocess.run(cmd, stdout=subprocess.PIPE)
    ret.check_returncode()

    # format output in JSON format
    json_string = "{" + ", ".join(ret.stdout.decode().splitlines()) + "}"

    data = json.loads(json_string)
    return data


def get_s2b_mapping(b2s: Dict[str, str]) -> Dict[str, List[str]]:
    # calculate reverse mapping
    s2b = dict()

    for binary in b2s.keys():
        source = b2s[binary]

        if source not in s2b.keys():
            s2b[source] = list()

        s2b[source].append(binary)

    return s2b


class GetRequires:
    cache: Dict[str, Dict[str, List[str]]] = dict()

    def __init__(self, repos: List[str]):
        self.repos = repos

    def __call__(self, package: str) -> Tuple[List[str], List[str]]:
        if package in self.cache:
            return self.cache[package]["brs"], self.cache[package]["reqs"]

        @retry(message="Failed to query dnf.", times=3, delay=5)
        def query() -> Tuple[List[str], List[str]]:
            cmd = [
                "dnf", "--quiet",
                "--installroot", "/tmp/dnf/",
                "--releasever", "rawhide",
                "--arch=src,noarch,x86_64",
                "repoquery"
            ]

            for repo in self.repos:
                cmd.extend(["--repo", repo])

            cmd.extend(["--alldeps", "--whatrequires", package])

            ret = subprocess.run(cmd, stdout=subprocess.PIPE)
            ret.check_returncode()

            deps: List[str] = ret.stdout.decode().splitlines()

            requires: List[str] = list()
            buildrequires: List[str] = list()

            for dep in deps:
                n, e, v, r, a = parse_nevra(dep)

                if a == "src":
                    buildrequires.append(n)
                else:
                    requires.append(n)

            buildrequires.sort()
            requires.sort()

            return buildrequires, requires

        brs, reqs = query()
        self.cache[package] = {
            "brs": brs,
            "reqs": reqs,
        }

        return brs, reqs


def get_dep_tree(
        package: str,
        acc: Set[str],
        s2b: Dict[str, List[str]],
        b2s: Dict[str, str],
        max_depth: int,
        blacklist: list,
        repos: List[str],
        level: int = 0,
) -> List[str]:
    if level == max_depth:
        return [package]

    indent = " " * level

    if is_blacklisted(package, blacklist):
        # skip dependent packages of blacklisted items
        print(f"      {indent}- {package} (skipped)")
        acc.add(package)
        # but count blacklisted items themselves
        return [package]

    print(f"      {indent}- {package}")

    all_deps = set()
    all_deps.add(package)

    acc.add(package)

    get_requires = GetRequires(repos)
    br_deps, deps = get_requires(package)

    for br_dep in br_deps:
        try:
            binaries = s2b[br_dep]
        except KeyError:
            # foreign-arch package
            continue

        for binary in binaries:
            if binary in acc:
                continue

            for rec_dep in get_dep_tree(binary, acc, s2b, b2s, max_depth, blacklist, repos, level + 1):
                all_deps.add(rec_dep)

    for dep in deps:
        try:
            binaries = s2b[b2s[dep]]
        except KeyError:
            # foreign-arch package
            continue

        for binary in binaries:
            if binary in acc:
                continue

            for rec_dep in get_dep_tree(binary, acc, s2b, b2s, max_depth, blacklist, repos, level + 1):
                all_deps.add(rec_dep)

    result = list()
    for dep in all_deps:
        result.append(dep)
    result.sort()

    return result
