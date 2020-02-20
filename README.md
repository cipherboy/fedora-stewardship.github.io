# fedora Stewardship SIG

Data and code in this git repository is either released into the Public Domain,
or licensed under the terms of the **Unlicense** license text contained in the
`LICENSE` file, whichever is applicable wherever you are.

For more information, look into the `docs` folder or go to
<https://fedora-stewardship.github.io>.

### Updating event data

Some data for events is hard to collect automatically, so those events are kept
track of manually in the `data/events.json` file. These events are:

- new package is adopted (`adopted` event)
- package is removed from the SIG (`removed` event)
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

**NOTE**: Keep in mind that for new packages that were never maintained by the
SIG before, it's necessary to add the event for the last time the package in
fedora was updated before the adoption by the SIG **and** all upstream releases
made after (and including) the packaged version need to be added to the
`events.json` file to ensure accurate statistics and timekeeping.

For this purpose, it might be convenient to look at the [libraries.io] page for
the project in question, where a good overview of released versions and release
dates can be found. This can also be used to verify that the maven
`groupId:artifactId` documented in the spreadsheet are accurate.

**NOTE**: If it's not immediately obvious when a new version was released by an
upstream project, use release dates as published on [libraries.io] as source of
consistent information. Be aware that the "new version" BugZillas filed by
[release-monitoring.org] are sometimes created even before the maven central
repository has the new version. If this is the case, wait until maven central is
up to date, refresh [libraries.io] data, and use the release date displayed
there.

[libraries.io]: https://libraries.io
[release-monitoring.org]: https://release-monitoring.org

### Rendering and viewing pages locally

To build and view documentation locally, install `ruby` and `bundler`, and then
execute `bundle install` or `bundle update`, which will download and build all
dependencies into the `vendor` folder. Once that's done, you can use this
command to build a live preview of the docs, which will then be available on
<http://localhost:4000> by default.

```
bundle exec jekyll serve --watch --livereload
```

**NOTE**: Do not run this with the `--watch` flag while updating the generated
pages and images with the `update` script - it will lead to problems and broken
images.

### Automatically updating generated content

The report, PR report, overview, and backlog pages are automatically generated
from rawhide repository data, the list of packages currently maintained by this
SIG, open pull requests on SIG package repositories, and the curated data in
`data/events.json`.

To automatically check for new data, and update the pages accordingly, just run
the `./update` script. It has only a few requirements:

- `dnf`, `dnf-tools` and `fedora-repos-rawhide`
- `python >= 3.5`
- `jinja2`, `pandas`, `prettytable`, `requests`, `rpm` python3 modules

