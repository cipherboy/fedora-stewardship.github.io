---
title:      Event list maintenance
layout:     page
permalink:  /events/
updated:    2020-02-21
---

Some data for events is hard to collect automatically, so those events are kept
track of manually in the `data/events.json` file. These events are:

- new package is adopted (`adopted` event, see also
  [process for adoptions](/adoption/))
- package is removed from the SIG (`removed` event, see also
  [process for orphaning](/orphaning))
- the upstream project released a new version (`released` event)
- the fedora package was updated to a new version (`updated` event)

Add any new events at the bottom the JSON data, and run the `sort_events.py`
script to automatically and reproducibly sort the array by date.

Also add the new information to the SIG's spreadsheet in Google Docs, if
necessary:

- adopted package: add new row in the spreadsheet and fill in the data
- removed package: remove the row entirely
- updated package: update packaged version, last updated, and formatting
- upstream release: update latest version, last outdated, and formatting

---

**NOTE**: Keep in mind that for new packages that were never maintained by the
SIG before, it's necessary to add the event for the last time the package in
fedora was updated before the adoption by the SIG **and** all upstream releases
made after (and including) the packaged version need to be added to the
`events.json` file to ensure accurate statistics and timekeeping.

For this purpose, it might be convenient to look at the [libraries.io] page for
the project in question, where a good overview of released versions and release
dates can be found. This can also be used to verify that the maven
`groupId:artifactId` documented in the spreadsheet are accurate.

---

**NOTE**: If it's not immediately obvious when a new version was released by an
upstream project, use release dates as published on [libraries.io] as source of
consistent information. Be aware that the "new version" BugZillas filed by
[release-monitoring.org] are sometimes created even before the maven central
repository has the new version. If this is the case, wait until maven central is
up to date, refresh [libraries.io] data, and use the release date displayed
there.

[libraries.io]: https://libraries.io
[release-monitoring.org]: https://release-monitoring.org
