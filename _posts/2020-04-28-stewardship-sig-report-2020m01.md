---
title:      "Stewardship SIG Report (January 2020)"
layout:     post
date:       "2020-04-28 14:18:00 +0200"
tags:       fedora stewardship monthly
---

We only pushed a few Java package updates in January, including some minor
updates for the Jackson stack.

First, we updated the apache parent POM to the latest version.

| package       | version | release                        | changes                             |
| ------------- | ------- | ------------------------------ | ----------------------------------- |
| apache-parent | 22      | [1.fc32][apache-parent-22-f32] | [21 → 22][apache-parent-22-changes] |

[apache-parent-22-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1431275
[apache-parent-22-changes]: https://github.com/apache/maven-apache-parent/compare/apache-21...apache-22

We also pushed the 2.10.2 releases of the Jackson stack to rawhide.

| package                 | version | release                                      | changes                                                   |
| ----------------------- | ------- | -------------------------------------------- | --------------------------------------------------------- |
| jackson-bom             | 2.10.2  | [1.fc32][jackson-bom-2.10.2-f32]             | [2.10.1 → 2.10.2][jackson-bom-2.10.2-changes]             |
| jackson-annotations     | 2.10.2  | [1.fc32][jackson-annotations-2.10.2-f32]     | [2.10.1 → 2.10.2][jackson-annotations-2.10.2-changes]     |
| jackson-core            | 2.10.2  | [1.fc32][jackson-core-2.10.2-f32]            | [2.10.1 → 2.10.2][jackson-core-2.10.2-changes]            |
| jackson-databind        | 2.10.2  | [1.fc32][jackson-databind-2.10.2-f32]        | [2.10.1 → 2.10.2][jackson-databind-2.10.2-changes]        |
| jackson-modules-base    | 2.10.2  | [1.fc32][jackson-modules-base-2.10.2-f32]    | [2.10.1 → 2.10.2][jackson-modules-base-2.10.2-changes]    |
| jackson-jaxrs-providers | 2.10.2  | [1.fc32][jackson-jaxrs-providers-2.10.2-f32] | [2.10.1 → 2.10.2][jackson-jaxrs-providers-2.10.2-changes] |

[jackson-bom-2.10.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1431279
[jackson-bom-2.10.2-changes]: https://github.com/FasterXML/jackson-bom/compare/jackson-bom-2.10.1...jackson-bom-2.10.2

[jackson-annotations-2.10.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1431286
[jackson-annotations-2.10.2-changes]: https://github.com/FasterXML/jackson-annotations/compare/jackson-annotations-2.10.1...jackson-annotations-2.10.2

[jackson-core-2.10.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1431289
[jackson-core-2.10.2-changes]: https://github.com/FasterXML/jackson-core/compare/jackson-core-2.10.1...jackson-core-2.10.2

[jackson-databind-2.10.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1431294
[jackson-databind-2.10.2-changes]: https://github.com/FasterXML/jackson-databind/compare/jackson-databind-2.10.1...jackson-databind-2.10.2

[jackson-modules-base-2.10.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1431299
[jackson-modules-base-2.10.2-changes]: https://github.com/FasterXML/jackson-modules-base/compare/jackson-modules-base-2.10.1...jackson-modules-base-2.10.2

[jackson-jaxrs-providers-2.10.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1431307
[jackson-jaxrs-providers-2.10.2-changes]: https://github.com/FasterXML/jackson-jaxrs-providers/compare/jackson-jaxrs-providers-2.10.1...jackson-jaxrs-providers-2.10.2

Last, we pushed the latest version of the Bean Validation API to rawhide.

| package             | version | release                                 | changes                                            |
| ------------------- | ------- | --------------------------------------- | -------------------------------------------------- |
| bean-validation-api | 2.0.1   | [1.fc32][bean-validation-api-2.0.1-f32] | [1.1.0 → 2.0.1][bean-validation-api-2.0.1-changes] |

[bean-validation-api-2.0.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1434188
[bean-validation-api-2.0.1-changes]: https://github.com/eclipse-ee4j/beanvalidation-api/compare/1.1.0.Final...2.0.1.Final

