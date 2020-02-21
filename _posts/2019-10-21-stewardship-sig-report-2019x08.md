---
title:      "Stewardship SIG Report (August 2019)"
layout:     post
date:       "2019-10-21 11:08:00"
tags:       fedora stewardship monthly
---

Whoop, this report is a bit late, but I still want to give a summary of what the
Stewardship SIG has been up to in August. TL;DR: We reduced the number of
outdated packages from about 55% to about 45% and introduced some changes to
limit the number of packages that we're going to have to maintain in the future.

We started by removing some unused functionality from a few packages (especially
dropping the dependency on the *Spring* framework, which was removed from fedora
at the beginning of August due to it failing to build from source since fedora
29.

| package      | version | release                      | changes                                                 |
| ------------ | ------- | ---------------------------- | ------------------------------------------------------- |
| google-guice | 4.1     | [16.fc31][guice-4.1-f31]     | [disable support for spring and JPA][guice-4.1-changes] |
| snakeyaml    | 1.17    | [9.fc31][snakeyaml-1.17-f31] | [drop spring dependency][snakeyaml-1.17-changes]        |
| xbean        | 4.9     | [5.fc31][xbean-4.9-f31]      | [drop spring and groovy support][xbean-4.9-changes]     |

[guice-4.1-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1343990
[guice-4.1-changes]: https://src.fedoraproject.org/rpms/google-guice/c/13bea8c

[snakeyaml-1.17-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1344671
[snakeyaml-1.17-changes]: https://src.fedoraproject.org/rpms/snakeyaml/c/a4c9564?branch=master

[xbean-4.9-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1344672
[xbean-4.9-changes]: https://src.fedoraproject.org/rpms/xbean/c/0f0d3fb?branch=master

We also started working on getting some packages updated to the latest versions.
Most of our packages haven't been touched since 2017, so there's a lot of
outstanding new releases pending, and this is only a small start.

| package               | version              | release                                 | changes                                            |
| --------------------- | -------------------- | --------------------------------------- | -------------------------------------------------- |
| ant                   | [1.10.6][ant-1.10.6] | [1.fc31][ant-1.10.6-f31]                | [1.10.5 → 1.10.6][ant-1.10.6-changes]              |
| jna                   | [5.4.0][jna-5.4.0]   | [1.fc31][jna-5.4.0-f31]                 | [4.5.1 → 5.4.0][jna-5.4.0-changes]                 |
| apache-logging-parent | 2                    | [1.fc31][apache-logging-parent-2-f31]   | [1 → 2][apache-logging-parent-2-changes]           |
| apache-mime4j         | 0.8.3                | [1.fc31][apache-mime4j-0.8.3-f31]       | [0.8.1 → 0.8.3][apache-mime4j-0.8.3-changes]       |
| apache-rat            | 0.13                 | [1.fc31][apache-rat-0.13-f31]           | [0.12 → 0.13][apache-rat-0.13-changes]             |
| bean-validation-api   | 2.0.1                | [1.fc31][bean-validation-api-2.0.1-f31] | [1.1.0 → 2.0.1][bean-validation-api-2.0.1-changes] |
| woodstox-core         | 5.2.1                | [1.fc31][woodstox-core-5.2.1-f31]       | [5.0.3 → 5.2.1][woodstox-core-5.2.1-changes]       |
| plexus-io             | 3.1.1                | [1.fc31][plexus-io-3.1.1-f31]           | [3.0.0 → 3.1.1][plexus-io-3.1.1-changes]           |
| google-guice          | 4.2.2                | [1.fc31][google-guice-4.2.2-f31]        | [4.1 → 4.2.2][google-guice-4.2.2-changes]          |

[ant-1.10.6]: https://github.com/apache/ant/blob/rel/1.10.6/WHATSNEW
[ant-1.10.6-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1345039
[ant-1.10.6-changes]: https://github.com/apache/ant/compare/rel/1.10.5...rel/1.10.6

[jna-5.4.0]: https://github.com/java-native-access/jna/blob/5.4.0/CHANGES.md#release-540
[jna-5.4.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1347296
[jna-5.4.0-changes]: https://github.com/java-native-access/jna/compare/4.5.1...5.4.0

[apache-logging-parent-2-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1348266
[apache-logging-parent-2-changes]: https://src.fedoraproject.org/rpms/apache-logging-parent/c/7e96eaf?branch=master

[apache-mime4j-0.8.3-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1348272
[apache-mime4j-0.8.3-changes]: https://src.fedoraproject.org/rpms/apache-mime4j/c/c3347de?branch=master

[apache-rat-0.13-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1348277
[apache-rat-0.13-changes]: https://src.fedoraproject.org/rpms/apache-rat/c/e0b97f2?branch=master

[bean-validation-api-2.0.1-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1348940
[bean-validation-api-2.0.1-changes]: https://src.fedoraproject.org/rpms/bean-validation-api/c/983ad99?branch=master

[woodstox-core-5.2.1-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1348943
[woodstox-core-5.2.1-changes]: https://src.fedoraproject.org/rpms/woodstox-core/c/a23fec2?branch=master

[plexus-io-3.1.1-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1350164
[plexus-io-3.1.1-changes]: https://src.fedoraproject.org/rpms/plexus-io/c/3658975?branch=master

[google-guice-4.2.2-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1350367
[google-guice-4.2.2-changes]: https://src.fedoraproject.org/rpms/google-guice/c/b972e61?branch=master

Meeting in person at flock in Budapest, we also finally decided that we couldn't
continue maintaining *Gradle* and the build system support for it any longer due
to numerous issues (including *Gradle* failing to build since fedora 30, the
package being massively outdated, and newer versions requiring even more yet
unpackaged dependencies). So we dropped support for builind packages with
*Gradle* from both `xmvn` and `javapackages-tools` for fedora 31 and later.

Maintainers of packages that get built with *Gradle* will have to adapt (it's
usually possible to convert builds to use *Maven* instead, which is already the
way it works for some existing fedora packages).

| package            | version | release                                | changes                                                         |
| ------------------ | ------- | -------------------------------------- | --------------------------------------------------------------- |
| xmvn               | 3.0.0   | [25.fc31][xmvn-3.0.0-f31-1]            | [disabled support for gradle][xmvn-3.0.0-changes-1]             |
| javapackages-tools | 5.3.0   | [6.fc31][javapackages-tools-5.3.0-f31] | [disabled support for gradle][javapackages-tools-5.3.0-changes] |

[xmvn-3.0.0-f31-1]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1351433
[xmvn-3.0.0-changes-1]: https://src.fedoraproject.org/rpms/xmvn/c/6f9dba2?branch=master

[javapackages-tools-5.3.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1351436
[javapackages-tools-5.3.0-changes]: https://src.fedoraproject.org/rpms/javapackages-tools/c/08b8c55?branch=master

Then we pushed some more changes to packages to remove additional dependencies,
so we don't have to keep adopting more and more packages to keep things working.
We made sure to only remove functionality that wasn't in use in other fedora
packages.

| package                 | version | release                                                                  | changes                                                         |
| ----------------------- | ------- | ------------------------------------------------------------------------ | --------------------------------------------------------------- |
| apache-commons-compress | 1.18    | [6.fc32][commons-compress-1.18-f32], [6.fc31][commons-compress-1.18-f31] | [drop powermock dependency][commons-compress-1.18-changes]      |
| bsf                     | 2.4.0   | [34.fc32][bsf-2.4.0-f32], [34.fc31][bsf-2.4.0-f31]                       | [removed rhino dependency][bsf-2.4.0-changes]                   |
| apache-ivy              | 2.4.0   | [18.fc32][ivy-2.4.0-f32], [18.fc31][ivy-2.4.0-f31]                       | [disable ssh, bouncycastle, and vfs support][ivy-2.4.0-changes] |

[commons-compress-1.18-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1355795
[commons-compress-1.18-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1355797
[commons-compress-1.18-changes]: https://src.fedoraproject.org/rpms/apache-commons-compress/c/b83cadb?branch=master

[bsf-2.4.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1361640
[bsf-2.4.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1361641
[bsf-2.4.0-changes]: https://src.fedoraproject.org/rpms/bsf/c/9c09a74?branch=master

[ivy-2.4.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1361642
[ivy-2.4.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1361652
[ivy-2.4.0-changes]: https://src.fedoraproject.org/rpms/apache-ivy/c/a0ed095?branch=master

Then started a second round of version updates, which brought the percentage of
outdated packages to below 50% (which is progress).

| package                   | version | release                                                                                      | changes                                                  |
| ------------------------- | ------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| jboss-annotations-1.2-api | 1.0.2   | [1.fc32][jboss-annotations-1.2-api-1.0.2-f32], [1.fc31][jboss-annotations-1.2-api-1.0.2-f31] | [1.0.0 → 1.0.2][jboss-annotations-1.2-api-1.0.2-changes] |
| jboss-connector-1.7-api   | 1.0.1   | [1.fc32][jboss-connector-1.7-api-1.0.1-f32], [1.fc31][jboss-connector-1.7-api-1.0.1-f31]     | [1.0.0 → 1.0.1][jboss-connector-1.7-api-1.0.1-changes]   |
| jboss-el-2.2-api          | 1.0.5   | [1.fc32][jboss-el-2.2-api-1.0.5-f32], [1.fc31][jboss-el-2.2-api-1.0.5-f31]                   | [1.0.2 → 1.0.5][jboss-el-2.2-api-1.0.5-changes]          |
| plexus-archiver           | 4.1.0   | [1.fc32][plexus-archiver-4.1.0-f32], [1.fc31][plexus-archiver-4.1.0-f31]                     | [3.6.0 → 4.1.0][plexus-archiver-4.1.0-changes]           |
| maven-archiver            | 3.4.0   | [1.fc32][maven-archiver-3.4.0-f32], [1.fc31][maven-archiver-3.4.0-f31]                       | [3.2.0 → 3.4.0][maven-archiver-3.4.0-changes]            |
| maven-assembly-plugin     | 3.1.1   | [1.fc32][maven-assembly-plugin-3.1.1-f32], [1.fc31][maven-assembly-plugin-3.1.1-f31]         | [3.1.0 → 3.1.1][maven-assembly-plugin-3.1.1-changes]     |

[jboss-annotations-1.2-api-1.0.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363609
[jboss-annotations-1.2-api-1.0.2-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363610
[jboss-annotations-1.2-api-1.0.2-changes]: https://src.fedoraproject.org/rpms/jboss-annotations-1.2-api/c/c376725?branch=master

[jboss-connector-1.7-api-1.0.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363611
[jboss-connector-1.7-api-1.0.1-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363612
[jboss-connector-1.7-api-1.0.1-changes]: https://src.fedoraproject.org/rpms/jboss-connector-1.7-api/c/a0aa1cd?branch=master

[jboss-el-2.2-api-1.0.5-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363614
[jboss-el-2.2-api-1.0.5-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363615
[jboss-el-2.2-api-1.0.5-changes]: https://src.fedoraproject.org/rpms/jboss-el-2.2-api/c/8bcd3b0?branch=master

[plexus-archiver-4.1.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363617
[plexus-archiver-4.1.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363620
[plexus-archiver-4.1.0-changes]: https://src.fedoraproject.org/rpms/plexus-archiver/c/3139555?branch=master

[maven-archiver-3.4.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363621
[maven-archiver-3.4.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363622
[maven-archiver-3.4.0-changes]: https://src.fedoraproject.org/rpms/maven-archiver/c/c8499fe?branch=master

[maven-assembly-plugin-3.1.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363628
[maven-assembly-plugin-3.1.1-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363629
[maven-assembly-plugin-3.1.1-changes]: https://src.fedoraproject.org/rpms/maven-assembly-plugin/c/9005753?branch=master

We also updated `flex` to the latest version and pushed a patch to adapt `qdox`
to these changes.

| package | version | release                                              | changes                                 |
| ------- | ------- | ---------------------------------------------------- | --------------------------------------- |
| jflex   | 1.7.0   | [1.fc32][jflex-1.7.0-f32], [1.fc31][jflex-1.7.0-f31] | [1.6.1 → 1.7.0][jflex-1.7.0-changes]    |
| qdox    | 2.0     | [6.M9.fc32][qdox-2.0-f32], [6.M9.fc31][qdox-2.0-f31] | [port to jflex 1.7.0][qdox-2.0-changes] |

[jflex-1.7.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363631
[jflex-1.7.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363635
[jflex-1.7.0-changes]: https://src.fedoraproject.org/rpms/jflex/c/9c333c1?branch=master

[qdox-2.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363648
[qdox-2.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363649
[qdox-2.0-changes]: https://src.fedoraproject.org/rpms/qdox/c/0510036?branch=master

A third round of easy version updates followed, where we still pushed our
changes to both rawhide and the pre-beta fedora 31 branch.

| package                   | version | release                                                                                        | changes                                                   |
| ------------------------- | ------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| maven-dependency-analyzer | 1.11.1  | [1.fc32][maven-dependency-analyzer-1.11.1-f32], [1.fc31][maven-dependency-analyzer-1.11.1-f31] | [1.10 → 1.11.1][maven-dependency-analyzer-1.11.1-changes] |
| maven-shade-plugin        | 3.2.1   | [1.fc32][maven-shade-plugin-3.2.1-f32], [1.fc31][maven-shade-plugin-3.2.1-f31]                 | [3.1.1 → 3.2.1][maven-shade-plugin-3.2.1-changes]         |
| modello                   | 1.10.0  | [1.fc32][modello-1.10.0-f32], [1.fc31][modello-1.10.0-f31]                                     | [1.9.1 → 1.10.0][modello-1.10.0-changes]                  |
| plexus-containers         | 2.0.0   | [1.fc32][plexus-containers-2.0.0-f32], [1.fc31][plexus-containers-2.0.0-f31]                   | [1.7.1 → 2.0.0][plexus-containers-2.0.0-changes]          |
| plexus-compiler           | 2.8.5   | [1.fc32][plexus-compiler-2.8.5-f32], [1.fc31][plexus-compiler-2.8.5-f31]                       | [2.8.2 → 2.8.5][plexus-compiler-2.8.5-changes]            |
| plexus-components-pom     | 4.0     | [1.fc32][plexus-components-pom-4.0-f32], [1.fc31][plexus-components-pom-4.0-f31]               | [1.3.1 → 4.0][plexus-components-pom-4.0-changes]          |
| xbean                     | 4.14    | [1.fc32][xbean-4.14-f32], [1.fc31][xbean-4.14-f31]                                             | [4.9 → 4.14][xbean-4.14-changes]                          |
| felix-utils               | 1.11.2  | [1.fc32][felix-utils-1.11.2-f32], [1.fc31][felix-utils-1.11.2-f31]                             | [1.10.4 → 1.11.2][felix-utils-1.11.2-changes]             |

[maven-dependency-analyzer-1.11.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363646
[maven-dependency-analyzer-1.11.1-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363650
[maven-dependency-analyzer-1.11.1-changes]: https://src.fedoraproject.org/rpms/maven-dependency-analyzer/c/08c39bb?branch=master

[maven-shade-plugin-3.2.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363651
[maven-shade-plugin-3.2.1-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363652
[maven-shade-plugin-3.2.1-changes]: https://src.fedoraproject.org/rpms/maven-shade-plugin/c/8e755cd?branch=master

[modello-1.10.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363683
[modello-1.10.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363684
[modello-1.10.0-changes]: https://src.fedoraproject.org/rpms/modello/c/68a0f6e?branch=master

[plexus-containers-2.0.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363686
[plexus-containers-2.0.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363687
[plexus-containers-2.0.0-changes]: https://src.fedoraproject.org/rpms/plexus-containers/c/e23e892?branch=master

[plexus-compiler-2.8.5-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363855
[plexus-compiler-2.8.5-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363857
[plexus-compiler-2.8.5-changes]: https://src.fedoraproject.org/rpms/plexus-compiler/c/de297aa?branch=master

[plexus-components-pom-4.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363860
[plexus-components-pom-4.0-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363861
[plexus-components-pom-4.0-changes]: https://src.fedoraproject.org/rpms/plexus-components-pom/c/6514c44?branch=master

[xbean-4.14-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363863
[xbean-4.14-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1363864
[xbean-4.14-changes]: https://src.fedoraproject.org/rpms/xbean/c/4e35e4c?branch=master

[felix-utils-1.11.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1365546
[felix-utils-1.11.2-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1365547
[felix-utils-1.11.2-changes]: https://src.fedoraproject.org/rpms/felix-utils/c/eecd442?branch=master

In preparation for other updates we worked to update `xmlunit` to the latest
major version, and pushed a patch for `xmvn` to adapt to this new version.

| package | version | release                                                  | changes                                   |
| ------- | ------- | -------------------------------------------------------- | ----------------------------------------- |
| xmlunit | 2.6.3   | [1.fc32][xmlunit-2.6.3-f32], [1.fc31][xmlunit-2.6.3-f31] | [1.6 → 2.6.3][xmlunit-2.6.3-changes]      |
| xmvn    | 3.0.0   | [26.fc32][xmvn-3.0.0-f32-2], [26.fc31][xmvn-3.0.0-f31-2] | [port to xmlunit 2][xmvn-3.0.0-changes-2] |

[xmlunit-2.6.3-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1364020
[xmlunit-2.6.3-f31]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1364022
[xmlunit-2.6.3-changes]: https://src.fedoraproject.org/rpms/xmlunit/c/bf396e3?branch=master

[xmvn-3.0.0-f32-2]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1364029
[xmvn-3.0.0-f31-2]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1364033
[xmvn-3.0.0-changes-2]: https://src.fedoraproject.org/rpms/xmvn/c/e9d12f3?branch=master

We also updated `snakeyaml` to the latest version, which contained some minor
changes in API. I pushed a patch for `jruby` to adapt to these changes. No other
packages were affected.

| package   | version                | release                                                    | changes                                         |
| --------- | ---------------------- | ---------------------------------------------------------- | ----------------------------------------------- |
| snakeyaml | [1.25][snakeyaml-1.25] | [1.fc32][snakeyaml-1.25-f32], [1.fc31][snakeyaml-1.25-f31] | [1.17 → 1.25][snakeyaml-1.25-changes]           |
| jruby     | 1.7.22                 | [10.fc32][jruby-1.7.22-f32], [10.fc31][jruby-1.7.22-f31]   | [port to snakeyaml 1.20+][jruby-1.7.22-changes] |

[snakeyaml-1.25]: https://bitbucket.org/asomov/snakeyaml/wiki/Changes
[snakeyaml-1.25-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1366966
[snakeyaml-1.25-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-d9e71a1069
[snakeyaml-1.25-changes]: https://src.fedoraproject.org/rpms/snakeyaml/c/8d086ed?branch=master

[jruby-1.7.22-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1368509
[jruby-1.7.22-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-d9e71a1069
[jruby-1.7.22-changes]: https://src.fedoraproject.org/rpms/jruby/c/bc51f0b?branch=master

Last, we disabled some more unused features in two packages to make sure we
don't depend on packages that are going to be removed due to the 6-week-orphan
retirement process.

| package               | version | release                                                                              | changes                                                                      |
| --------------------- | ------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| httpcomponents-client | 4.5.7   | [3.fc32][httpcomponents-client-4.5.7-f32], [3.fc31][httpcomponents-client-4.5.7-f31] | [disable memcached and ehcache support][httpcomponents-client-4.5.7-changes] |
| maven-wagon           | 3.3.3   | [3.fc32][maven-wagon-3.3.3-f32], [3.fc31][maven-wagon-3.3.3-f31]                     | [disable SSH support][maven-wagon-3.3.3-changes]                             |

[httpcomponents-client-4.5.7-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1368502
[httpcomponents-client-4.5.7-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-c025346b78
[httpcomponents-client-4.5.7-changes]: https://src.fedoraproject.org/rpms/httpcomponents-client/c/c7b4545?branch=master

[maven-wagon-3.3.3-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1368503
[maven-wagon-3.3.3-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-034a9fc5b5
[maven-wagon-3.3.3-changes]: https://src.fedoraproject.org/rpms/maven-wagon/c/6f4b911?branch=master

