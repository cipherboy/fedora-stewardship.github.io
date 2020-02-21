---
layout:     page
updated:    2020-02-21
---

There's also a [Wiki page][sig-Wiki] for this SIG on the fedoraproject Wiki.


## IRC and Meetings

The `#fedora-stewardship` IRC channel on freenode is used for synchronous
conversations. Meetings are held bi-weekly in the `#fedora-meeting-1` channel,
at 15:00 UTC every other Tuesday (starting April 30, 2019). The meeting process
is documented [here](/meetings/). The meetings are also automatically tracked in
the [fedora calendar].


## Mailing List

The private `stewardship-sig` fedora mailing list is used for announcements,
BugZilla E-Mails, and asynchronous conversations. New members will be added to
this list automatically.


## Maintained packages

The list of packages that are currently maintained under the Stewardship SIG
umbrella can be found on the [group's page][src-group] on
[src.fedoraproject.org].


## Package build status

The current build status of all packages can be seen on the
[koschei page for the Stewardship SIG group][koschei-group].


## Prioritized packages

There are a few packages that we want to keep maintained, even if no proper new
maintainer wants to pick them up in the near future. Others we want to keep in
a working (and building state), but we don't maintain the packages themselves:

- **ant**
- **dogtag-pki** (deps only)
- **eclipse** (deps only)
- **libreoffice** (deps only)
- **maven**

To suggest a new prioritized package (or to ask us to take over an orphaned
package) for a good reason, open a [new ticket][suggestion-ticket] in our
tracking project on pagure.


## How to help

Most of our packages are looking for new, permanent maintainers, so if you are
an experienced packager and want to take some packages off our hands, open a
[new ticket][adoption-ticket] in our tracking project on pagure.


<!-- Links -->

[sig-wiki]: https://fedoraproject.org/wiki/SIGs/Stewardship
[fedora calendar]: https://apps.fedoraproject.org/calendar/location/fedora-meeting-1%40irc.freenode.net/#m9655
[src-group]: https://src.fedoraproject.org/group/stewardship-sig
[src.fedoraproject.org]: https://src.fedoraproject.org
[koschei-group]: https://apps.fedoraproject.org/koschei/groups/stewardship-sig?
[suggestion-ticket]: https://pagure.io/stewardship-sig/new_issue?template=package_suggestion&title=Package%20maintenance%20request:%20foo
[adoption-ticket]: https://pagure.io/stewardship-sig/new_issue?template=package_adoption_request&title=Package%20adoption%20request:%20foo
