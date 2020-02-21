---
title:      "Stewardship SIG Report (September 2019)"
layout:     post
date:       "2019-10-25 12:13:00"
tags:       fedora stewardship monthly
---

The month of September was a bit more quiet regarding the activity of the
Stewardship SIG, though we again managed to push some important changes and
updates, both to reduce the number of packages we possibly need to maintain, and
to bring the whole stack into better shape and more up-to-date again.

We removed some unused functionality from our packages, which let us trim the
dependency tree some more. Notably, by dropping the direct dependency of
*Maven* on `logback`, our packages no longer require *Groovy* or *Gradle*, not
even transitively.

The support for Markdown in the `doxia` maven modules was also removed in
preparation for version updates, which would introduce not-yet-packaged
dependencies for the Markdown support anyway.

The unused support for `memoryfilesystem` was removed from `assertj-core` to
further reduce the number of packages we need to maintain.

| package               | version | release                                                | changes                                                         |
| --------------------- | ------- | ------------------------------------------------------ | --------------------------------------------------------------- |
| maven                 | 3.5.4   | [12.fc32][maven-3.5.4-f32], [12.fc31][maven-3.5.4-f31] | [remove dependency on logback][maven-3.5.4-changes]             |
| maven-doxia-sitetools | 1.7.5   | [6.fc32][maven-doxia-sitetools-1.7.5-f32]              | [disable markdown support][maven-doxia-sitetools-1.7.5-changes] |
| maven-doxia           | 1.7     | [12.fc32][maven-doxia-1.7-f32]                         | [disable itext support][maven-doxia-1.7-changes]                |
| assertj-core          | 3.8.0   | [6.fc32][assertj-core-3.8.0-f32]                       | [drop memoryfilesystem dependency][assertj-core-3.8.0-changes]  |

[maven-3.5.4-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1368951
[maven-3.5.4-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-7ada4c6760
[maven-3.5.4-changes]: https://src.fedoraproject.org/rpms/maven/c/1c4ff04

[maven-doxia-sitetools-1.7.5-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1369964
[maven-doxia-sitetools-1.7.5-changes]: https://src.fedoraproject.org/rpms/maven-doxia-sitetools/c/4331b73

[maven-doxia-1.7-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1370812
[maven-doxia-1.7-changes]: https://src.fedoraproject.org/rpms/maven-doxia/c/2068b8c

[assertj-core-3.8.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1377433
[assertj-core-3.8.0-changes]: https://src.fedoraproject.org/rpms/assertj-core/c/3c91d13?branch=master

We also worked on getting updates for *Jackson* out fast, since some security
vulnerabilities for `jackson-databind` were recently published
([CVE-2019-12086], [CVE-2019-12384], [CVE-2019-12814], [CVE-2019-14379],
[CVE-2019-14439]). These have all been fixed with the 2.9.9.3 release of
`jackson-databind`, which required updating its sister projects to 2.9.9 as
well.

[CVE-2019-12086]: https://nvd.nist.gov/vuln/detail/CVE-2019-12086
[CVE-2019-12384]: https://nvd.nist.gov/vuln/detail/CVE-2019-12384
[CVE-2019-12814]: https://nvd.nist.gov/vuln/detail/CVE-2019-12814
[CVE-2019-14379]: https://nvd.nist.gov/vuln/detail/CVE-2019-14379
[CVE-2019-14439]: https://nvd.nist.gov/vuln/detail/CVE-2019-14439

| package             | version | release                                                                                                                                                            | changes                                             |
| ------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| jackson-bom         | 2.9.9   | [1.fc32][jackson-bom-2.9.9-f32], [1.fc31][jackson-bom-2.9.9-f31], [1.fc30][jackson-bom-2.9.9-f30], [1.fc29][jackson-bom-2.9.9-f29]                                 | [2.9.8 → 2.9.9][jackson-bom-2.9.9-changes]          |
| jackson-annotations | 2.9.9   | [1.fc32][jackson-annotations-2.9.9-f32], [1.fc31][jackson-annotations-2.9.9-f31], [1.fc30][jackson-annotations-2.9.9-f30], [1.fc29][jackson-annotations-2.9.9-f29] | [2.9.8 → 2.9.9][jackson-annotations-2.9.9-changes]  |
| jackson-core        | 2.9.9   | [1.fc32][jackson-core-2.9.9-f32], [1.fc31][jackson-core-2.9.9-f31], [1.fc30][jackson-core-2.9.9-f30], [1.fc29][jackson-core-2.9.9-f29]                             | [2.9.8 → 2.9.9][jackson-core-2.9.9-changes]         |
| jackson-databind    | 2.9.9.3 | [1.fc32][jackson-databind-2.9.9.3-f32], [1.fc31][jackson-databind-2.9.9.3-f31], [1.fc30][jackson-databind-2.9.9.3-f30], [1.fc29][jackson-databind-2.9.9.3-f29]     | [2.9.8 → 2.9.9.3][jackson-databind-2.9.9.3-changes] |

[jackson-bom-2.9.9-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1377297
[jackson-bom-2.9.9-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-99ff6aa32c
[jackson-bom-2.9.9-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-ae6a703b8f
[jackson-bom-2.9.9-f29]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-fb23eccc03
[jackson-bom-2.9.9-changes]: https://src.fedoraproject.org/rpms/jackson-bom/c/7a10125?branch=master

[jackson-annotations-2.9.9-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1377300
[jackson-annotations-2.9.9-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-99ff6aa32c
[jackson-annotations-2.9.9-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-ae6a703b8f
[jackson-annotations-2.9.9-f29]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-fb23eccc03
[jackson-annotations-2.9.9-changes]: https://src.fedoraproject.org/rpms/jackson-annotations/c/8f44d49?branch=master

[jackson-core-2.9.9-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1377306
[jackson-core-2.9.9-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-99ff6aa32c
[jackson-core-2.9.9-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-ae6a703b8f
[jackson-core-2.9.9-f29]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-fb23eccc03
[jackson-core-2.9.9-changes]: https://src.fedoraproject.org/rpms/jackson-core/c/4cd0224?branch=master

[jackson-databind-2.9.9.3-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1377313
[jackson-databind-2.9.9.3-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-99ff6aa32c
[jackson-databind-2.9.9.3-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-ae6a703b8f
[jackson-databind-2.9.9.3-f29]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-fb23eccc03
[jackson-databind-2.9.9.3-changes]: https://src.fedoraproject.org/rpms/jackson-databind/c/65ccbd1?branch=master

We also managed to finally update some packages related to `maven-invoker` to
their latest versions, which required a coordinated update to `maven-invoker`,
`maven-invoker-plugin`, and a patch to port `xmvn` to these new versions.

| package              | version | release                                  | changes                                            |
| -------------------- | ------- | ---------------------------------------- | -------------------------------------------------- |
| maven-invoker        | 3.0.1   | [1.fc32][maven-invoker-3.0.1-f32]        | [2.2 → 3.0.1][maven-invoker-3.0.1-changes]         |
| maven-invoker-plugin | 3.2.0   | [1.fc32][maven-invoker-plugin-3.2.0-f32] | [1.10 → 3.2.0][maven-invoker-plugin-3.2.0-changes] |
| xmvn                 | 3.0.0   | [27.fc32][xmvn-3.0.0-f32]                | [port to maven-invoker 3.0.1][xmvn-3.0.0-changes]  |

[maven-invoker-3.0.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1377873
[maven-invoker-3.0.1-changes]: https://src.fedoraproject.org/rpms/maven-invoker/c/dd215d5?branch=master

[maven-invoker-plugin-3.2.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1377883
[maven-invoker-plugin-3.2.0-changes]: https://src.fedoraproject.org/rpms/maven-invoker-plugin/c/8066fef?branch=master

[xmvn-3.0.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1377889
[xmvn-3.0.0-changes]: https://src.fedoraproject.org/rpms/xmvn/c/23e9795?branch=master

Recently, the old *Felix* OSGi implementation was retired from fedora, in favor
of *OSGi Core* 7.0.0, and all packages using the old *Felix* implementation
needed to migrate. With some help from Mat Booth I pushed the necessary changes
to all our packages (and some others as well, not listed below).

| package                 | version | release                                    | changes                                                            |
| ----------------------- | ------- | ------------------------------------------ | ------------------------------------------------------------------ |
| apache-commons-compress | 1.18    | [7.fc32][apache-commons-compress-1.18-f32] | [migrate to osgi-core][apache-commons-compress-1.18-changes]       |
| snappy-java             | 1.1.2.4 | [13.fc32][snappy-java-1.1.2.4-f32]         | [migrate to osgi-core][snappy-java-1.1.2.4-changes]                |
| xbean                   | 4.14    | [2.fc32][xbean-4.14-f32]                   | [migrate to osgi-core][xbean-4.14-changes]                         |
| woodstox-core           | 6.0.1   | [2.fc32][woodstox-core-6.0.1-f32]          | [5.2.1 → 6.0.1 and migrate to OSGi 7][woodstox-core-6.0.1-changes] |

[apache-commons-compress-1.18-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1379928
[apache-commons-compress-1.18-changes]: https://src.fedoraproject.org/rpms/apache-commons-compress/c/ac6ae23?branch=master

[snappy-java-1.1.2.4-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1379940
[snappy-java-1.1.2.4-changes]: https://src.fedoraproject.org/rpms/snappy-java/c/2fb3050?branch=master

[xbean-4.14-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1379943
[xbean-4.14-changes]: https://src.fedoraproject.org/rpms/xbean/c/bcac7a2?branch=master

[woodstox-core-6.0.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1380098
[woodstox-core-6.0.1-changes]: https://src.fedoraproject.org/rpms/woodstox-core/c/a23fec..454dc8

Last, we were able to update both `maven-doxia` and `maven-doxia-sitetools` to
their latest versions. As mentioned above, this meant disabling the (unused)
support for Markdown, since the library that's used for Markdown support was
changed from `pegdown` (which was packaged for fedora) to `flexmark`, which
isn't available in fedora.

| package               | version | release                                   | changes                                              |
| --------------------- | ------- | ----------------------------------------- | ---------------------------------------------------- |
| maven-doxia           | 1.9     | [1.fc32][maven-doxia-1.9-f32]             | [1.7 → 1.9][maven-doxia-1.9-changes]                 |
| maven-doxia-sitetools | 1.9.1   | [1.fc32][maven-doxia-sitetools-1.9.1-f32] | [1.7.5 → 1.9.1][maven-doxia-sitetools-1.9.1-changes] |

[maven-doxia-1.9-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1379996
[maven-doxia-1.9-changes]: https://src.fedoraproject.org/rpms/maven-doxia/c/5fc7c79?branch=master

[maven-doxia-sitetools-1.9.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1380026
[maven-doxia-sitetools-1.9.1-changes]: https://src.fedoraproject.org/rpms/maven-doxia-sitetools/c/0b96bac?branch=master

