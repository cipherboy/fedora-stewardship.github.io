#!/usr/bin/python3

import argparse
import re
import time
from typing import Dict, List, Set

import requests

from stewardship import get_b2s_mapping, get_s2b_mapping, get_dep_tree, refresh_cache

LRU_CACHE_SIZE = None
MAX_DEPTH = 15


DEPENDENCY_BLACKLIST = list(
    re.compile(pattern) for pattern in [
        ".*-javadoc$",
        "^jruby.*",
    ]
)


def is_blacklisted(package: str, blacklist) -> bool:
    return any(regex.match(package) for regex in blacklist)


def get_sig_packages():
    data = requests.get("https://src.fedoraproject.org/api/0/group/stewardship-sig?projects=true").json()
    projects = data["projects"]

    return list(project["name"] for project in projects)


def main() -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--maxdepth", action="store", type=int, default=MAX_DEPTH,
        help="max number of traversed edges in dependency graph (default: 15)")
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
        print()

    # getting binary <-> source package mappings
    b2s = get_b2s_mapping(repos)
    s2b = get_s2b_mapping(b2s)

    # query src.fedoraproject.org for packages maintained by @stewardship-sig
    print("Getting group information from https://src.fedoraproject.org ...")
    sig_packages = get_sig_packages()
    print()

    # include packages supplied on the command line
    source_packages = sig_packages + include

    # calculate list of binary packages owned by the SIG
    binary_packages = list()
    for source_package in source_packages:
        binary_packages.extend(s2b[source_package])

    # initialize candidate list with all SIG source packages
    candidates = sig_packages.copy()

    causes: Dict[str, Set[str]] = dict()

    for depth in range(1, maxdepth + 1):
        dep_tree = dict()

        print(f"Traversing dependency graph for {depth} edge(s).")
        print("Currently considered SIG leaf candidates:")
        for package in candidates:
            print(" -", package)
        print()

        time.sleep(5)

        for package in candidates:
            print(" -", package, "(source)")

            # iterate over all built binary packages
            binaries = s2b[package]

            for binary in binaries:
                print("   -", binary, "(binary)")

                # calculate dependency tree from dnf metadata
                allrec = get_dep_tree(binary, set(), s2b, b2s, depth, DEPENDENCY_BLACKLIST, repos)

                # remove dependencies on "self"
                allrec.remove(binary)

                # save metadata for later
                dep_tree[binary] = allrec

        # generate list of "SIG leaf" packages
        # (only packages outside of this group depend on them)
        not_sig_leaves: Set[str] = set()

        for package in candidates:
            binaries = s2b[package]

            # ignore dependencies on "self"
            filtered_all_packages = binary_packages.copy()
            for binary in binaries:
                if binary in filtered_all_packages:
                    filtered_all_packages.remove(binary)

            # collect all dependencies
            all_deps = set()
            for binary in binaries:
                for dep in dep_tree[binary]:
                    all_deps.add(dep)

            # check if any dependencies are SIG binary packages
            for dep in all_deps:
                if dep in filtered_all_packages:
                    not_sig_leaves.add(package)

                    # keep track of non-leaf status causes
                    if package not in causes.keys():
                        causes[package] = set()

                    causes[package].add(dep)

        print()

        print(f"Traversed dependency graph for {depth} edge(s).")
        for package in not_sig_leaves:
            print(f" - {package} is not a SIG leaf")
            candidates.remove(package)
        print()

    # print non-SIG-leaf packages
    for key, values in causes.items():
        print(f" - {key} is required by:")
        for package in sorted(values):
            print(f"   - {package}")
    print()

    # print remaining candidates
    for package in candidates:
        print(f" - Package is a SIG leaf: {package}")
    print()

    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        exit(0)
