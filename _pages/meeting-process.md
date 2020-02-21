---
title:      Meeting Process
layout:     page
permalink:  /meetings/
updated:    2020-02-21
---

This page documents the process for the fortnightly IRC meetings.


## Preparation

A few days before the next meeting, open a [new ticket] in our tracking project
on pagure using the `meeting_details` template, filling out the details, and
using `Meeting #NN on YYYY-MM-DD` as the title. Modify the template contents as
necessary, and tag the ticket with `meeting`.

[new ticket]: https://pagure.io/stewardship-sig/new_issue?template=meeting_details&title=Meeting%20%23NN%20on%20YYYY-MM-DD

There's also a regular event for the meeting registered in `fedocal`, which
needs to be adjusted, should the meeting time change at any point.


## Meeting

To start the meeting, use the following commands (which get processed by
`meetbot`):

- `#startmeeting Stewardship SIG Meeting (YYYY-MM-DD)`
- `#meetingname stewardship-sig`

Then proceed with the meeting. The following `meetbot` commands are useful:

- `#chair USER [USER ...]`: recognise attendees that are present and give them
  access to `meetbot` commands
- `#topic TOPIC`: set the current topic
- `#info`: include general information in the meeting minutes
- `#link URL [DESCRIPTION]`: include a URL in the meeting minutes, with an
   optional description
- `#action USER DESCRIPTION`: assign an action to a user, this shows up in the
  meeting log
- `#agree DECISION DESCRIPTION`: include the result of a vote in the meeting
  minutes
- `#undo`: undo the last `meetbot` action

To end the meeting, use `#endmeeting`. `meetbot` will respond with links to the
meeting minutes and logs. Copy these to the meeting ticket on pagure and close
the ticket.

Further information about meetings are available from the useful [Meeting Guide]
on the fedoraproject Wiki. It's also easy to query [`zodbot`][zodbot] for
information related to fedora.

[Meeting Guide]: https://fedoraproject.org/wiki/Meeting:Guide
[zodbot]: https://fedoraproject.org/wiki/Zodbot


## Old meetings

Old `stewardship-sig` meeting minutes and logs can be found by
[querying meetbot][meeting-logs].

[meeting-logs]: https://meetbot.fedoraproject.org/sresults/?group_id=stewardship-sig&type=team


## Ticket template

Ticket templates can be accessed and modified in the "internal" git repo for the
pagure project, where tickets and templates are stored. If the template becomes
outdated, just clone the ticket repository, modify the template, commit your
changes, and push them.
