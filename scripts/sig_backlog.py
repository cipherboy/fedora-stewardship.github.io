#!/usr/bin/python3

import json
from datetime import date, timedelta
from operator import itemgetter
from pprint import pprint
from typing import Dict, Tuple

import jinja2
import pandas as pd
from matplotlib import pyplot as plt
from rpm import labelCompare

# start statistics at this date (used as starting point for graphs)
STATS_START_DATE = date.fromisoformat("2019-02-26")

VALID_EVENTS = [
    "released",
    "updated",
    "adopted",
    "removed",
]


with open("../data/packages.json") as FILE:
    PACKAGES = json.loads(FILE.read())


class Package:
    def __init__(self, name: str):
        self.name = name

        self.last_version = None
        self.last_updated = None

        self.sig_package = False
        self.update_backlog: Dict[Version, int] = dict()


def fluffify(version) -> Tuple[str, str, str]:
    return "0", version, "0"


class Version(str):
    def __hash__(self):
        return super().__hash__()

    def __lt__(self, other):
        return labelCompare(fluffify(self), fluffify(other)) == -1

    def __gt__(self, other):
        return labelCompare(fluffify(self), fluffify(other)) == 1

    def __eq__(self, other):
        return labelCompare(fluffify(self), fluffify(other)) == 0

    def __ne__(self, other):
        return labelCompare(fluffify(self), fluffify(other)) != 0

    def __le__(self, other):
        return labelCompare(fluffify(self), fluffify(other)) != 1

    def __ge__(self, other):
        return labelCompare(fluffify(self), fluffify(other)) != -1


def validate(datum):
    event = datum["event"]

    if event not in VALID_EVENTS:
        print(f"Invalid event: {event}:")
        pprint(datum)
        raise Exception("Invalid event")

    name = datum["package"]

    if name not in PACKAGES:
        print(f"Invalid package: {name}:")
        pprint(datum)
        raise Exception("Invalid package")

    datestr = datum["date"]

    try:
        date.fromisoformat(datestr)
    except:
        print(f"Invalid date: {datestr}:")
        pprint(datum)
        raise Exception("Invalid date")

    version = datum["version"]

    if version is not None and "-" in version:
        print(f"Invalid version: {version}:")
        pprint(datum)
        raise Exception("Invalid version")


def main():
    with open("../data/events.json") as file:
        data = json.loads(file.read())

    data.sort(key=itemgetter("date"))

    for datum in data:
        validate(datum)

    start_date = date.fromisoformat(data[0]["date"])
    stop_date = date.today()

    packages: Dict[str, Package] = {name: Package(name) for name in PACKAGES}
    statistics = dict()

    # FIXME optimize
    # iterate over all days
    current_date = start_date
    while current_date <= stop_date:
        stats = dict()
        statistics[current_date] = stats

        events = list(
            filter(lambda x: x["date"] == current_date.isoformat(), data)
        )

        # increment package update backlog lengths
        for package in packages.values():
            for version in package.update_backlog.keys():
                package.update_backlog[version] += 1

        # update package data according to this day's events
        for event in events:
            name: str = event["package"]
            package: Package = packages[name]
            etype: str = event["event"]

            if etype == "adopted":
                package.sig_package = True
                continue

            if etype == "removed":
                package.sig_package = False
                continue

            # for "released" and "updated", there's a version
            version = Version(event["version"])

            if etype == "released":
                # only update latest version if it's actually greater
                if package.last_version is None or package.last_version < version:
                    package.last_version = version

                # initialize backlog duration for new versions with 0
                if package.last_updated is None or version > package.last_updated:
                    package.update_backlog[version] = 0

            if etype == "updated":
                # always update latest update, assume it never decreases
                package.last_updated = version

                # if the package is updated to the latest version:
                if package.last_version == package.last_updated:
                    # drop all backlog information
                    package.update_backlog.clear()

                # if it was updated to a version that's not the latest version:
                else:
                    # drop all versions that are older than the updated one
                    versions = list(package.update_backlog.keys())
                    for v in versions:
                        if version >= v:
                            package.update_backlog.pop(v)

        # filter by packages that are maintained by the SIG
        sig_packages = {
            package.name: package
            for package in filter(
                lambda p: p.sig_package, packages.values()
            )
        }

        # calculate update backlogs
        sum_backlog_len = sum(
            len(package.update_backlog.keys())
            for package in sig_packages.values()
        )

        average_backlog_len = (
            sum_backlog_len / len(sig_packages.keys())
            if len(sig_packages.keys()) != 0 else 0
        )

        # calculate maximum update delays
        sum_backlog_dur = sum(
            max(package.update_backlog.values(), default=0)
            for package in sig_packages.values()
        )

        average_backlog_dur = (
            sum_backlog_dur / len(sig_packages.keys())
            if len(sig_packages.keys()) != 0 else 0
        )

        # gather number of outdated packages
        abs_outdated_pkgs = len(list(
            filter(lambda x: (
                    len(x.update_backlog.keys()) != 0
                    and
                    x.sig_package
            ), packages.values())
        ))

        rel_outdated_pkgs = (abs_outdated_pkgs / len(sig_packages)) if len(sig_packages) != 0 else 0

        stats["sig_pkgs"] = len(sig_packages)
        stats["abs_outdated_pkgs"] = abs_outdated_pkgs
        stats["rel_outdated_pkgs"] = rel_outdated_pkgs
        stats["sum_bl_len"] = sum_backlog_len
        stats["sum_bl_dur"] = sum_backlog_dur
        stats["avg_bl_len"] = average_backlog_len
        stats["avg_bl_dur"] = average_backlog_dur

        # on towards the next day
        current_date += timedelta(days=1)

    # print today's package statistics
    pprint({name: package.__dict__ for name, package in packages.items()})

    for name, package in packages.items():
        if package.last_version is None:
            print("No release information for:", name)
        if package.last_updated is None:
            print("No update information for:", name)

    # print package statistics
    with open("sig_backlog_template.jinja2") as file:
        template = jinja2.Template(file.read())
    stats_document = template.render(
        packages=packages,
        package_ods=str(statistics[stop_date]["abs_outdated_pkgs"]),
        package_num=str(statistics[stop_date]["sig_pkgs"]),
        package_od_percent=(str(round(statistics[stop_date]["rel_outdated_pkgs"]*100)) + "%"),
    )

    with open("../_pages/sig-backlog.md", "w") as file:
        file.write(stats_document)

    # create markdown document of package overview table
    markdown = list()

    markdown.append("| package | last updated | last release | status |")
    markdown.append("| ------- | ------------ | ------------ | ------ |")

    for name, package in packages.items():
        if not package.sig_package:
            continue

        if package.last_version == package.last_updated:
            status = "current"
        else:
            days = max([*package.update_backlog.values()] + [0])
            status = f"{days} days behind"

        markdown.append(
            f"| {package.name} "
            f"| {package.last_updated} "
            f"| {package.last_version} "
            f"| {status} |"
        )

    overview_doc = "\n".join([
        "---",
        "title:      Overview",
        "layout:     page",
        "permalink:  /overview/",
        "---",
        "",
        "![SIG Packages](/assets/sig_pkgs.png)",
        "![Total backlog duration](/assets/sum_bl_dur.png)",
        "![Total backlog length](/assets/sum_bl_len.png)",
        "![Average backlog duration](/assets/avg_bl_dur.png)",
        "![Average backlog length](/assets/avg_bl_len.png)",
        "![Number of outdated packages](/assets/od_pkgs_abs.png)",
        "![Ratio of outdated packages](/assets/od_pkgs_rel.png)",
        "",
    ] + markdown + [""])

    with open("../_pages/sig-overview.md", "w") as file:
        file.write(overview_doc)

    # start statistics at 2019-02-26 (one day before packages were added)
    stat_start_date = STATS_START_DATE
    stat_stop_date = date.today()

    # restrict data to interesting time period
    curr_date = stat_start_date
    dates = list()

    # linearize statistics
    sig_pkgs = list()
    od_pkgs_abs = list()
    od_pkgs_rel = list()
    sum_bl_lens = list()
    sum_bl_durs = list()
    avg_bl_lens = list()
    avg_bl_durs = list()

    while curr_date <= stat_stop_date:
        dates.append(curr_date.isoformat())
        sig_pkgs.append(statistics[curr_date]["sig_pkgs"])
        od_pkgs_abs.append(statistics[curr_date]["abs_outdated_pkgs"])
        od_pkgs_rel.append(statistics[curr_date]["rel_outdated_pkgs"])
        sum_bl_lens.append(statistics[curr_date]["sum_bl_len"])
        sum_bl_durs.append(statistics[curr_date]["sum_bl_dur"])
        avg_bl_lens.append(statistics[curr_date]["avg_bl_len"])
        avg_bl_durs.append(statistics[curr_date]["avg_bl_dur"])

        curr_date += timedelta(days=1)

    # plot statistics

    # get first of the month for plot ticks
    firsts = list()
    labels = list()
    for i, d in enumerate(dates):
        iso = date.fromisoformat(d)
        if iso.day == 1:
            firsts.append(i)
            labels.append(d)

    df0 = pd.DataFrame(sig_pkgs, index=dates)
    df1 = pd.DataFrame(avg_bl_lens, index=dates)
    df1s = pd.DataFrame(sum_bl_lens, index=dates)
    df2 = pd.DataFrame(avg_bl_durs, index=dates)
    df2s = pd.DataFrame(sum_bl_durs, index=dates)
    df3 = pd.DataFrame(od_pkgs_abs, index=dates)
    df3r = pd.DataFrame(od_pkgs_rel, index=dates)

    # number of maintained packages vs. time
    pt0 = df0.plot(color="navy", lw=2, use_index=True,
                   legend=False, rot=90, figsize=(10, 5))
    pt0.set_title("Number of maintained packages")
    pt0.grid(axis="y")
    plt.locator_params(axis="y", nbins=4)
    plt.xticks(firsts, labels)
    plt.savefig("../assets/sig_pkgs.png", bbox_inches="tight", dpi=300)

    # average update backlog vs. time
    pt1 = df1.plot(color="navy", lw=2, use_index=True,
                   legend=False, rot=90, figsize=(10, 5))
    pt1.set_title("Average length of update backlogs")
    pt1.grid(axis="y")
    plt.locator_params(axis="y", nbins=3)
    plt.xticks(firsts, labels)
    plt.savefig("../assets/avg_bl_len.png", bbox_inches="tight", dpi=300)

    # total update backlog vs. time
    pt1s = df1s.plot(color="navy", lw=2, use_index=True,
                     legend=False, rot=90, figsize=(10, 5))
    pt1s.set_title("Total length of update backlogs")
    pt1s.grid(axis="y")
    plt.locator_params(axis="y", nbins=5)
    plt.xticks(firsts, labels)
    plt.savefig("../assets/sum_bl_len.png", bbox_inches="tight", dpi=300)

    # average update delay vs. time
    pt2 = df2.plot(color="navy", lw=2, use_index=True,
                   legend=False, rot=90, figsize=(10, 5))
    pt2.set_title("Average update delay in days for all packages")
    pt2.grid(axis="y")
    plt.locator_params(axis="y", nbins=4)
    plt.xticks(firsts, labels)
    plt.savefig("../assets/avg_bl_dur.png", bbox_inches="tight", dpi=300)

    # total update delay vs. time
    pt2s = df2s.plot(color="navy", lw=2, use_index=True,
                     legend=False, rot=90, figsize=(10, 5))
    pt2s.set_title("Total update delay in days for all packages")
    pt2s.grid(axis="y")
    plt.locator_params(axis="y", nbins=5)
    plt.xticks(firsts, labels)
    plt.savefig("../assets/sum_bl_dur.png", bbox_inches="tight", dpi=300)

    # absolute and relative number of outdated packages
    pt3 = df3.plot(color="navy", lw=2, use_index=True,
                   legend=False, rot=90, figsize=(10, 5))
    pt3.set_title("Total number of outdated packages")
    pt3.grid(axis="y")
    plt.locator_params(axis="y", nbins=5)
    plt.xticks(firsts, labels)
    plt.savefig("../assets/od_pkgs_abs.png", bbox_inches="tight", dpi=300)

    pt3r = df3r.plot(color="navy", lw=2, use_index=True,
                     legend=False, rot=90, figsize=(10, 5))
    pt3r.set_title("Fraction of outdated packages")
    pt3r.grid(axis="y")
    plt.locator_params(axis="y", nbins=5)
    plt.xticks(firsts, labels)
    plt.savefig("../assets/od_pkgs_rel.png", bbox_inches="tight", dpi=300)

    return 0


if __name__ == "__main__":
    exit(main())

