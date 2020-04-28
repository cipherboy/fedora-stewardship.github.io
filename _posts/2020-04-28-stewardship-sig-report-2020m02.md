---
title:      "Stewardship SIG Report (February 2020)"
layout:     post
date:       "2020-04-28 16:56:00 +0200"
tags:       fedora stewardship monthly
---

In February, the Stewardship SIG was again busy delivering changes for the
not-so-ancient-anymore Java stack in fedora - including some new releases and
cleaning up some cruft.

The updates included some minor bug-fix updates for `woodstox-core`, `sisu`, and
`univocity-parsers`, the stable 2.0.0 release of `qdox` where fedora shipped
pre-release versions for a while, and the latest versions of some Plexus POMs.

| package               | version                      | release                                 | changes                                          |
| --------------------- | ---------------------------- | --------------------------------------- | ------------------------------------------------ |
| woodstox-core         | [6.0.3][woodstox-core-6.0.3] | [1.fc33][woodstox-core-6.0.3-f33]       | [6.0.2 → 6.0.3][woodstox-core-6.0.3-changes]     |
| sisu                  | 0.3.4                        | [1.fc33][sisu-0.3.4-f33]                | [0.3.3 → 0.3.4][sisu-0.3.4-changes]              |
| univocity-parsers     | 2.8.4                        | [1.fc33][univocity-parsers-2.8.4-f33]   | [2.8.3 → 2.8.3][univocity-parsers-2.8.4-changes] |
| qdox                  | 2.0.0                        | [1.fc33][qdox-2.0.0-f33]                | [2.0~M9 → 2.0.0][qdox-2.0.0-changes]             |
| plexus-pom            | 6.1                          | [1.fc33][plexus-pom-6.1-f33]            | [5.1 → 6.1][plexus-pom-6.1-changes]              |
| plexus-components-pom | 6.1                          | [1.fc33][plexus-components-pom-6.1-f33] | [4.0 → 6.1][plexus-components-pom-6.1-changes]   |
| plexus-compiler       | 2.8.6                        | [1.fc33][plexus-compiler-2.8.6-f33]     | [2.8.5 → 2.8.6][plexus-compiler-2.8.6-changes]   |

[woodstox-core-6.0.3]: https://github.com/FasterXML/woodstox/blob/woodstox-core-6.0.3/release-notes/VERSION
[woodstox-core-6.0.3-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1460068
[woodstox-core-6.0.3-changes]: https://src.fedoraproject.org/rpms/plexus-compiler/c/d2a7c3cca972a276bd4c41532c01987215d41947?branch=master

[sisu-0.3.4-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1460074
[sisu-0.3.4-changes]: https://src.fedoraproject.org/rpms/sisu/c/49e00e4262dbf05bbeaaf29623ede329e5fa5168?branch=master

[univocity-parsers-2.8.4-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1460083
[univocity-parsers-2.8.4-changes]: https://src.fedoraproject.org/rpms/univocity-parsers/c/1ce0da62e82964a84d4006ce16d4bee771954948?branch=master

[qdox-2.0.0-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1460085
[qdox-2.0.0-changes]: https://src.fedoraproject.org/rpms/qdox/c/2ba0cb814ecad7f873773feb175e6824491db870?branch=master

[plexus-pom-6.1-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1460086
[plexus-pom-6.1-changes]: https://src.fedoraproject.org/rpms/plexus-pom/c/a48b3f9f3191f6b1e770c25fc792337982fc8763?branch=master

[plexus-components-pom-6.1-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1460087
[plexus-components-pom-6.1-changes]: https://src.fedoraproject.org/rpms/plexus-components-pom/c/cdeba92c755c592a55c060e8dc76cb593ea3c86f?branch=master

[plexus-compiler-2.8.6-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1466607
[plexus-compiler-2.8.6-changes]: https://src.fedoraproject.org/rpms/plexus-compiler/c/d2a7c3cca972a276bd4c41532c01987215d41947?branch=master

We also managed to port *Log4J* to some breaking changes that were introduced in
the latest versions of *SLF4J*.

| package | version | release                                                | changes                        |
| ------- | ------- | ------------------------------------------------------ | ------------------------------ |
| log4j   | 2.13.0  | [3.fc33][log4j-2.13.0-f33], [3.fc32][log4j-2.13.0-f32] | adapt to newest slf4j versions |

[log4j-2.13.0-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1466138
[log4j-2.13.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1466139

I also continued to work on dropping dependencies on the `sonatype-oss-parent`
package - which was marked as `deprecated()` long ago. With these changes, none
of the packages that are maintained by the Stewardship SIG are depending on it
directly, though some still depend on `sonatype-oss-parent` transitively.

| package | version | release                      | changes                                                            |
| ------- | ------- | ---------------------------- | ------------------------------------------------------------------ |
| guava   | 25.0    | [7.fc33][guava-25.0-f33]     | [drop unnecessary dependency on parent POM][guava-25.0-changes]    |
| guava20 | 20.0    | [12.fc33][guava20-20.0-f33]  | [drop unnecessary dependency on parent POM][guava20-20.0-changes]  |
| testng  | 6.14.3  | [11.fc33][testng-6.14.3-f33] | [drop unnecessary dependency on parent POM][testng-6.14.3-changes] |

[guava-25.0-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1470760
[guava-25.0-changes]: https://src.fedoraproject.org/rpms/guava/c/12a84682c6e558cef9f6d8378a1a15eb5d7638e2?branch=master

[guava20-20.0-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1470761
[guava20-20.0-changes]: https://src.fedoraproject.org/rpms/guava20/c/1c20e4308f6d85baeae52c31bbb1c3ea92eda060?branch=master

[testng-6.14.3-f33]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1470762
[testng-6.14.3-changes]: https://src.fedoraproject.org/rpms/testng/c/0b10f9002baf02f774d28dedf0ec376734c61a33?branch=master

