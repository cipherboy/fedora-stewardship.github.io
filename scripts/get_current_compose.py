#!/usr/bin/python3

import subprocess
from typing import List

import requests

BASE_URL = "https://kojipkgs.fedoraproject.org/compose/rawhide"

COMPOSE_ID_URL = BASE_URL + "/latest-Fedora-Rawhide/COMPOSE_ID"
COMPOSE_CL_URL = BASE_URL + "/Fedora-Rawhide-{}/logs/changelog-Fedora-Rawhide-{}.json"


def get_compose() -> str:
    string = requests.get(COMPOSE_ID_URL, timeout=30).text.strip()
    compose = string.split("-")[2]
    return compose


def get_changelog_json(compose: str) -> dict:
    url = COMPOSE_CL_URL.format(compose, compose)
    data = requests.get(url, timeout=30).json()
    return data


def get_rawhide_packages() -> List[str]:
    ret = subprocess.run(
        [
            "dnf", "--quiet",
            "--installroot", "/tmp/dnf",
            "--releasever", "rawhide",
            "--repo", "rawhide-source",
            "makecache", "--refresh",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    ret.check_returncode()

    ret = subprocess.run(
        [
            "dnf", "--quiet",
            "--installroot", "/tmp/dnf",
            "--releasever", "rawhide",
            "--repo", "rawhide-source",
            "repoquery", "--nvr"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    ret.check_returncode()

    return ret.stdout.decode().splitlines(keepends=False)


def is_current(compose: str) -> bool:
    compose = get_changelog_json(compose)
    packages = get_rawhide_packages()

    added = compose["added_packages"]
    upgraded = compose["upgraded_packages"]

    # iterate over added and upgraded packages
    for entry in added + upgraded:
        # skip modules, they aren't in the standard rawhide repos
        if ".module_" in entry["nvr"]:
            continue
        # check if the first non-module nvr is in the repo
        else:
            return entry["nvr"] in packages
    # all added and upgraded packages were considered (or there were none),
    # but none were useful for determining if the repo is up to date
    else:
        raise Exception("Cannot determine if the rawhide repo is current.")


def main() -> int:
    compose = get_compose()

    if is_current(compose):
        print(compose)
        return 0

    else:
        print("Current compose:", compose)
        print("Rawhide repository does not yet contain data from the most recent compose.")
        print("Wait a few hours and check again.")
        return 1


if __name__ == "__main__":
    exit(main())
