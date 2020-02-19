#!/usr/bin/python3

from typing import List

import requests


def get_needed_orphans() -> List[str]:
    ret = requests.get("https://churchyard.fedorapeople.org/orphans.txt")

    ret.raise_for_status()

    sig = list(filter(
        lambda line: line.startswith("stewardship-sig: "),
        ret.text.splitlines()
    ))

    if not sig:
        return []

    pstring = sig[0].split(":")[1]
    packages = pstring.strip().replace(" ", "").split(",")
    packages.sort()

    return packages


def main() -> int:
    try:
        packages = get_needed_orphans()
    except:
        print("Failed to fetch orphans.txt file.")
        return 1

    print()

    for package in packages:
        print("-", package)

    print()
    print("Number of needed packages:", len(packages))

    return 0


if __name__ == "__main__":
    exit(main())
