---
title:      Orphaning Process
layout:     page
permalink:  /orphaning/
updated:    2020-02-21
---

When dropping a package from SIG maintenance, process the following steps:

1. Remove the SIG group from the package.
2. Give the package to the new owner (either `orphan` or the FAS username of the
   new maintainer).
3. Remove yourself from the package (**optional**). 

These settings are availabe on each package's settings page:
<https://src.fedoraproject.org/rpms/{PACKAGE}/settings#usersgroups-tab>

To make sure statistics and reports will be accurate once they are
regenerated, add an `removed` event to `data/events.json` (with `null` as
version).

Additionally, update the Google Docs spreadsheet by simply removing the row for
the removed package.

Then, triage existing issues for packages:

1. Look at <https://src.fedoraproject.org/rpms/{PACKAGE}> to see if there are
   any open Pull Requests assigned to Stewardship SIG members.
2. Look at the BugZilla component for the package to see if there are any open
   bugs, and if so, reassign them to the `orphan-extras@fedoraproject.org`
   BugZilla account if this doesn't happen automatically within a day or so.

<https://bugzilla.redhat.com/buglist.cgi?bug_status=NEW&bug_status=ASSIGNED&classification=Fedora&product=Fedora&component={PACKAGE}>

Also check if there are any existing (now wrong) default BugZilla assignee
overrides for the fedora package. Right now, this is still handled by files by
files in the `fedora-scm-requests` git repository. If there is no such file for
the package in question, then there are no overrides in place. If there is an
override for `Fedora: '@stewardship-sig'`, remove this entry from the file.

<https://pagure.io/releng/fedora-scm-requests/blob/master/f/rpms/{PACKAGE}}>

Fork this repository, make your changes, and open a Pull Request.
