#!/usr/bin/python3

import jinja2
import requests

from stewardship import retry


TEMPLATE = """\
---
title:      Pull Requests
layout:     page
permalink:  /pr-report/
---

{% for package, pr_list in prs.items() %}
## {{ package }}
{% for pr in pr_list %}
- [#{{ pr.id }}: {{ pr.title }}]({{ pr.link }})
{% endfor %}
{% endfor %}
"""

LINK_TEMPLATE = "https://src.fedoraproject.org/rpms/{name}/pull-request/{id}"


@retry("Failed to get group information from src.fp.org.", 3, 5)
def get_group():
    return requests.get("https://src.fedoraproject.org/api/0/group/stewardship-sig?projects=true").json()


@retry("Failed to get Pull Requests from src.fp.org.", 3, 5)
def get_requests(name):
    return requests.get("https://src.fedoraproject.org/api/0/rpms/{}/pull-requests?".format(name)).json()


def main() -> int:
    group = get_group()
    projects = group["projects"]

    prs = dict()

    for project in projects:
        name = project["name"]
        print(" -", name)

        pull_requests = get_requests(name)["requests"]

        for request in pull_requests:
            pr_id = request["id"]
            pr_title = request["title"]

            if name not in prs.keys():
                prs[name] = list()

            prs[name].append({
                "id": pr_id,
                "title": pr_title,
                "link": LINK_TEMPLATE.format(id=pr_id, name=name),
            })

    template = jinja2.Template(TEMPLATE)
    out = template.render(prs=prs)

    with open("../docs/_pages/pr-report.md", "w") as file:
        file.write(out)

    return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        print("Cancelling upon user request.")
        exit(0)
