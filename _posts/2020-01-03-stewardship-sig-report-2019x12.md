---
title:      "Stewardship SIG Report (December 2019)"
layout:     post
date:       "2020-01-03 12:52:00 +0100"
tags:       fedora stewardship monthly
---

December was a quiet month for the Stewardship SIG. On the one hand, clocks seem
to tick slower this time of year in general, and on the other hand, some policy
decisions around the future of Modularity in fedora made us put our work on the
slow burner for now. However, there's at least some newsworthy things to share.

The maintainer of the `apache-commons-logging` package merged my proposed change
to drop support for the *Avalon* framework. This allows us to drop a few old and
no longer supported packages.

| package                | version | release                            | changes                                                          |
| ---------------------- | ------- | ---------------------------------- | ---------------------------------------------------------------- |
| apache-commons-logging | 1.2     | [19.fc32][commons-logging-1.2-f32] | [disable avalon support by default][commons-logging-1.2-changes] |

We're also working with Mat Booth to get non-modular *Eclipse* packages working
again! We started by un-retiring a few packages that are still required:

- auto
- cbi-plugins
- decentxml
- glassfish-jsp
- takari-polyglot
- xml-maven-plugin

Mat then pushed some necessary updates to the non-modular branches that were
previously only available on the modular branches. With those changes in place,
I think we're on a good path towards making sure *Eclipse* will work again soon
without having to rely on Modularity.

| package          | version | release                                                                    | changes                                                |
| ---------------- | ------- | -------------------------------------------------------------------------- | ------------------------------------------------------ |
| xml-maven-plugin | 1.0.2   | [4.fc32][xml-maven-plugin-1.0.2-f32], [4.fc31][xml-maven-plugin-1.0.2-f31] | [package unretirement][xml-maven-plugin-1.0.2-changes] |
| auto             | 1.5.4   | [1.fc32][auto-1.5.4-f32], [1.fc31][auto-1.5.4-f31]                         | [package unretirement][auto-1.5.4-changes]             |

[commons-logging-1.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1421806
[commons-logging-1.2-changes]: https://src.fedoraproject.org/rpms/apache-commons-logging/c/1ce7cf922e6e3bf36c7f3bea1656a1d56f494527?branch=master

[xml-maven-plugin-1.0.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1422154
[xml-maven-plugin-1.0.2-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-9d44b5a452
[xml-maven-plugin-1.0.2-changes]: https://src.fedoraproject.org/rpms/xml-maven-plugin/c/5d5e001678d6bc8d1746db977984f0d82c2cb816?branch=master

[auto-1.5.4-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1422811
[auto-1.5.4-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-0008b0117b
[auto-1.5.4-changes]: https://src.fedoraproject.org/rpms/auto/c/375ee3086a9e0062170d8ca4ffba77bac7e5da9a?branch=master

