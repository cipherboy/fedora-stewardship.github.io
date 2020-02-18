#!/usr/bin/python3

import json
from datetime import date
from operator import itemgetter
from pprint import pprint


VALID_EVENTS = [
    "released",
    "updated",
    "adopted",
    "removed",
]

with open("packages.json") as file:
    PACKAGES = json.loads(file.read())


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
    with open("events.json") as file:
        data = json.loads(file.read())

    data.sort(key=itemgetter("date"))

    seen = list()

    for datum in data:
        try:
            validate(datum)
        except:
            continue

        comp = (datum["date"], datum["package"], datum["event"], datum["version"])

        if comp in seen:
            print("Duplicate event:")
            print(comp)
        else:
            seen.append(comp)

    with open("events.json", "w") as file:
        file.write(json.dumps(data, indent=2))

    return 0


if __name__ == "__main__":
    exit(main())

