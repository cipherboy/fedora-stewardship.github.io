---
title:      Adoption Process
layout:     page
permalink:  /adoption/
updated:    2020-02-21
---

When adding a new package to be maintained by the SIG, process the following
steps to make sure statistics and reports will be accurate once they are
regenerated:

1. Add the **package name** to the list in `data/packages.json` (keep it
   alphabetically sorted).
   This data is used to verify valid events in `data/events.json`, and only
   explicitly mentioned package names are considered valid. 
2. Add an `adopted` event to `data/events.json` (with `null` as version).
3. Add the **date the package was last updated** in fedora as an `updated` event
   to `data/events.json`.
4. Add all **stable upstream releases, starting from the packaged version**, as
   `released` events to `data/events.json`.

For this purpose, it might be useful to look at the
[libraries.io](https://libraries.io) for the project, which has a good overview
of upstream releases and release dates.

Additionally, update the Google Docs spreadsheet with the package data:

1. Add a new row for the package (keeping the table sorted alphabetically by
   package name).
2. Find out and enter the maven `groupId:artifactId` for the package.
3. Enter the **packaged version** and the **latest stable version**, copy the
   formula for the package state into the new row, and update the row color
   according to the color scheme.
4. Enter the date of the package adoption into the "First added" column.

Then, triage pre-existing issues for packages:

1. Look at <https://src.fedoraproject.org/rpms/{PACKAGE}> to see if there are
   any open Pull Requests.
2. Look at the BugZilla component for the package to see if there are any open
   bugs:

<https://bugzilla.redhat.com/buglist.cgi?bug_status=NEW&bug_status=ASSIGNED&classification=Fedora&product=Fedora&component={PACKAGE}>

Also check if there are any existing (now wrong) default BugZilla assignee
overrides for the fedora package. Right now, this is still handled by files by
files in the `fedora-scm-requests` git repository. If there is no such file for
the package in question, then there are no overrides in place.

<https://pagure.io/releng/fedora-scm-requests/blob/master/f/rpms/{PACKAGE}}>

Fork this repository, make your changes, and open a Pull Request.
