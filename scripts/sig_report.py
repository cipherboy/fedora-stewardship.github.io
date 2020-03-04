#!/usr/bin/python3

import argparse
import datetime
import json
import re
from typing import List, Dict, Union

import jinja2
import prettytable
import requests

from stewardship import get_b2s_mapping, get_s2b_mapping, GetRequires, refresh_cache, get_dep_tree

LRU_CACHE_SIZE = None
MAX_DEPTH = 3

PACKAGE_MAP_CACHE = "package_map.json"
PACKAGE_DEP_CACHE = "package_dep.json"

TEMPLATE_PATH = "sig_report_template.jinja2"

DEPENDENCY_BLACKLIST = list(
    re.compile(pattern) for pattern in [
        # javadoc subpackages take a long time and have no relevant dependencies
        ".*-javadoc$",
        # sagemath docs contain huge numbers of files and take forever to check
        "^sagemath-doc.*",
        # jruby is not interesting for us, and it pulls in all rubygems
        "^jruby.*",
        # texlive is not interesting for us, and it's a huge can of worms
        "^texlive.*",
        # also skip python3 and nodejs stacks
        "^nodejs.*",
        "^python.*",
    ]
)


def main() -> int:
    print()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "compose", action="store",
        help="identifier of the compose to analyze")
    parser.add_argument(
        "--maxdepth", action="store", type=int, default=MAX_DEPTH,
        help="override maximal dependency graph traversal steps (3)")
    parser.add_argument(
        "--koji", action="store_const", const=True, default=False,
        help="use koji repository directly instead of rawhide")
    parser.add_argument(
        "--no-refresh", action="store_const", const=True, default=False,
        help="do not refresh dnf cache before generating report")

    args = vars(parser.parse_args())
    compose: str = args["compose"]
    maxdepth: int = args["maxdepth"]
    koji: bool = args["koji"]
    no_refresh: bool = args["no_refresh"]

    if not koji:
        repos = ["rawhide", "rawhide-source"]
    else:
        repos = ["koji", "koji-sources"]

    get_requires = GetRequires(repos)

    # populate "members" list
    print("Getting group information from https://src.fedoraproject.org ...")

    sig = requests.get("https://src.fedoraproject.org/api/0/group/stewardship-sig?projects=true")
    ret = sig.json()

    members: List[str] = ret["members"]
    members.sort()

    projects = ret["projects"]
    packages = list(project["name"] for project in projects)

    # populate "maintained" table
    print("Populating package table ...")
    maintained = prettytable.PrettyTable()

    maintained.field_names = ["Package", "Main Admin", "Admin", "Commit"]

    for project in projects:
        name = project["name"]
        users = project["access_users"]
        owner = users["owner"]
        admin = users["admin"]
        commit = users["commit"]

        admin.sort()
        commit.sort()

        maintained.add_row([
            name,
            ", ".join(owner),
            ", ".join(admin) if admin else "--",
            ", ".join(commit) if commit else "--"
        ])

    maintained.hrules = prettytable.HEADER
    maintained.vrules = prettytable.NONE

    maintained.header = True
    maintained.align = "l"

    num_maintained = len(projects)

    # refreshing dnf cache
    if not no_refresh:
        print("Refreshing dnf cache ...")
        refresh_cache(repos)

    # getting binary <-> source package mappings
    b2s = get_b2s_mapping(repos)
    s2b = get_s2b_mapping(b2s)

    # check package dependencies
    print("Populating package dependency information ...")
    dep_map = dict()
    depinfo = dict()

    all_packages: List[str] = list()

    # iterate over all source packages
    for package in packages:
        print(" -", package)

        package_depended: List[Dict[str, Union[str, List[str]]]] = []
        package_leaves: List[str] = []

        # iterate over all built binary packages
        binaries = s2b[package]

        all_deps: List[str] = []

        for binary in binaries:
            print("   -", binary)

            all_packages.append(binary)

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

    # save results to JSON files for other uses
    package_map_data = {
        "compose": compose,
        "b2s": b2s,
        "s2b": s2b,
    }

    with open(PACKAGE_MAP_CACHE, "w") as file:
        file.write(json.dumps(package_map_data, indent=2, sort_keys=True))

    package_dep_data = {
        "compose": compose,
        "data": get_requires.cache,
    }

    with open(PACKAGE_DEP_CACHE, "w") as file:
        file.write(json.dumps(package_dep_data, indent=2, sort_keys=True))

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
        filtered_all_packages = all_packages.copy()
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

    # render output
    print("Rendering output ...")

    with open(TEMPLATE_PATH) as file:
        template = jinja2.Template(file.read())

    out = template.render(
        current_date=datetime.datetime.utcnow().isoformat() + " (UTC)",
        num_members=len(members),
        members=members,
        num_maintained=num_maintained,
        table=maintained.get_html_string(),
        depinfo=depinfo,
        leaves=leaves,
        sig_leaves=sig_leaves,
        all_packages=all_packages,
        compose=compose,
        levels=maxdepth,
    )

    # write output to file
    with open("../_pages/sig-report.html", "w") as file:
        file.write(out)

    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        exit(0)
