#!/usr/bin/python3 -OO

import argparse
import re
from typing import Dict, List, Union

import requests

from stewardship import get_b2s_mapping, get_s2b_mapping, GetRequires, get_dep_tree, refresh_cache

LRU_CACHE_SIZE = None
MAX_DEPTH = 5


DEPENDENCY_BLACKLIST = list(
    re.compile(pattern) for pattern in [
        ".*-javadoc$",
        "^jruby.*",
    ]
)


def is_blacklisted(package: str, blacklist) -> bool:
    return any(regex.match(package) for regex in blacklist)


def main() -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--maxdepth", action="store", type=int, default=MAX_DEPTH,
        help="max number of hops in dependency graph (default: 5, increase with caution - blows up script runtime)")
    parser.add_argument(
        "package", action="store", nargs="+",
        help="list of packages to check 'SIG leaf' status for")
    parser.add_argument(
        "--koji", action="store_const", const=True, default=False,
        help="use koji repository directly instead of rawhide")
    parser.add_argument(
        "--no-refresh", action="store_const", const=True, default=False,
        help="do not refresh dnf cache before generating report")
    parser.add_argument(
        "--include", action="append", default=[],
        help="include package as if it was maintained by the SIG")

    args = vars(parser.parse_args())

    maxdepth: int = args["maxdepth"]
    packages: List[str] = args["package"]
    koji: bool = args["koji"]
    no_refresh: bool = args["no_refresh"]
    include: List[str] = args["include"]

    if not koji:
        repos = ["rawhide", "rawhide-source"]
    else:
        repos = ["koji", "koji-sources"]

    # refreshing dnf cache
    if not no_refresh:
        print("Refreshing dnf cache ...")
        refresh_cache(repos)

    get_requires = GetRequires(repos)

    # getting binary <-> source package mappings
    b2s = get_b2s_mapping(repos)
    s2b = get_s2b_mapping(b2s)

    # fetch SIG packages
    print("Getting group information from https://src.fedoraproject.org ...")

    sig = requests.get("https://src.fedoraproject.org/api/0/group/stewardship-sig?projects=true")
    ret = sig.json()
    projects = ret["projects"]

    source_packages = list(project["name"] for project in projects)

    # include packages supplied on command line
    source_packages.extend(include)

    binary_packages = list()
    for source_package in source_packages:
        binary_packages.extend(s2b[source_package])

    dep_map = dict()
    depinfo = dict()

    for package in packages:
        print(" -", package)

        package_depended: List[Dict[str, Union[str, List[str]]]] = []
        package_leaves: List[str] = []

        # iterate over all built binary packages
        binaries = s2b[package]

        all_deps: List[str] = []

        for binary in binaries:
            print("   -", binary)

            # calculate dependencies from dnf metadata
            brs, reqs = get_requires(binary)
            allrec = get_dep_tree(binary, set(), s2b, b2s, maxdepth, DEPENDENCY_BLACKLIST, repos)
            allrec.remove(binary)

            # save metadata for later
            dep_map[binary] = dict()
            dep_map[binary]["reqs"] = reqs
            dep_map[binary]["brs"] = brs
            dep_map[binary]["all-recursive"] = allrec

            all_deps.extend(reqs + brs)

            # check if the package isn't depended upon
            if len(reqs + brs) == 0:
                package_leaves.append(binary)

            # package is depended upon by external packages
            else:
                package_depended.append({"srcname": package,
                                         "pkgname": binary,
                                         "reqs": reqs,
                                         "brs": brs})

        # check if the subpackages only depend within a source package
        if all((dep in binaries) for dep in all_deps):
            package_leaves.append(package)

        depinfo[package] = {
            "depended": package_depended,
            "leaves": package_leaves,
        }

    # generate list of "total leaf" packages
    # (no packages at all depend on any part of them)
    leaves: List[str] = []

    for pkg in depinfo.keys():
        if not depinfo[pkg]["depended"]:
            leaves.append(pkg)

    # generate list of "SIG leaf" packages
    # (only packages outside of this group depend on them)
    sig_leaves: List[str] = []

    for package in packages:
        binaries = s2b[package]

        # ignore dependencies on "self"
        filtered_all_packages = binary_packages.copy()
        for binary in binaries:
            if binary in filtered_all_packages:
                filtered_all_packages.remove(binary)

        all_deps = []

        # collect all dependencies
        for binary in binaries:
            all_deps.extend(dep_map[binary]["all-recursive"])

        # if none of the dependents are within our package set: SIG leaf
        if not any((dep in filtered_all_packages) for dep in all_deps):
            sig_leaves.append(package)

    # print updated SIG leaves status
    print(f"Checked for SIG leaf status up to a dependency graph depth of {maxdepth}.")

    for package in packages:
        if package in sig_leaves:
            print(f"Package is a SIG leaf: {package}")
        else:
            print(f"Package is not a SIG leaf: {package}")
            print("It is (transitively) depended on by:")

            for pkg in s2b[package]:
                deps = dep_map[pkg]["all-recursive"]

                for dep in deps:
                    if dep in binary_packages:
                        print(f" - {dep}")

    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        exit(0)
