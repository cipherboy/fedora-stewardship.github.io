---
title:      "Stewardship SIG Report (November 2019)"
layout:     post
date:       "2020-01-02 22:54:00 +0100"
tags:       fedora stewardship monthly
---

There's a lot of changes that we pushed in November, and there's little time to
talk about them, so here's a list of all the updates we submitted to fedora in
November.

Note that with all these updates, we managed to reduce the number of outdated
packages to about 25% of maintained package set, and we hope to improve further
upon this.

- various version updates:

| package                  | version | release                                                                      | changes                                             |
| ------------------------ | ------- | ---------------------------------------------------------------------------- | --------------------------------------------------- |
| glassfish-jax-rs-api     | 2.1.6   | [1.fc32][glassfish-jax-rs-api-2.1.6-f32]                                     | [2.1.5 → 2.1.6][glassfish-jax-rs-api-2.1.6-changes] |
| apache-commons-beanutils | 1.9.4   | [1.fc31][commons-beanutils-1.9.4-f31], [1.fc30][commons-beanutils-1.9.4-f30] | [1.9.3 → 1.9.4][commons-beanutils-1.9.4-changes]    |

- a small packaging fix for maven:

| package | version      | release                                                                                              | changes                                              |
| ------- | ------------ | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| maven   | 3.6.1, 3.5.4 | [1.fc32][maven-3.6.1, 3.5.4-f32], [1.fc31][maven-3.6.1, 3.5.4-f31], [1.fc30][maven-3.6.1, 3.5.4-f30] | [fixed postun scriptlet][maven-3.6.1, 3.5.4-changes] |

- inter-dependent version updates for plexus packages:

| package           | version | release                                 | changes                                                        |
| ----------------- | ------- | --------------------------------------- | -------------------------------------------------------------- |
| plexus-utils      | 3.3.0   | [1.fc32][plexus-utils-3.3.0-f32]        | [3.2.1 → 3.3.0][plexus-utils-3.3.0-changes]                    |
| plexus-build-api  | 0.0.7   | [24.fc32][plexus-build-api_1-0.0.7-f32] | [port to plexus-utils 3.3.0][plexus-build-api_1-0.0.7-changes] |
| plexus-io         | 3.2.0   | [1.fc32][plexus-io-3.2.0-f32]           | [3.1.1 → 3.2.0][plexus-io-3.2.0-changes]                       |
| plexus-containers | 2.1.0   | [1.fc32][plexus-containers-2.1.0-f32]   | [2.0.0 → 2.1.0][plexus-containers-2.1.0-changes]               |

- miscellaneous version updates:

| package           | version | release                               | changes                                              |
| ----------------- | ------- | ------------------------------------- | ---------------------------------------------------- |
| log4j             | 2.12.1  | [1.fc32][log4j-2.12.1-f32]            | [2.11.1 → 2.12.1][log4j-2.12.1-changes]              |
| jsoup             | 1.12.1  | [1.fc32][jsoup-1.12.1-f32]            | [1.11.3 → 1.12.1][jsoup-1.12.1-changes]              |
| jvnet-parent      | 5       | [1.fc32][jvnet-parent-5-f32]          | [4 → 5][jvnet-parent-5-changes]                      |
| glassfish-jsp-api | 2.3.3   | [1.fc32][glassfish-jsp-api-2.3.3-f32] | [2.3.2~b01 → 2.3.3][glassfish-jsp-api-2.3.3-changes] |
| sisu-mojos        | 0.3.4   | [1.fc32][sisu-mojos-0.3.4-f32]        | [0.3.3 → 0.3.4][sisu-mojos-0.3.4-changes]            |

- updating XMvn to the latest release, and adapting other packages:

| package                    | version | release                                    | changes                                                          |
| -------------------------- | ------- | ------------------------------------------ | ---------------------------------------------------------------- |
| xmvn                       | 3.1.0   | [1.fc32][xmvn-3.1.0-f32]                   | [3.0.0 → 3.1.0][xmvn-3.1.0-changes]                              |
| apache-commons-jexl        | 2.1.1   | [24.fc32][commons-jexl-2.1.1-f32]          | [fix build with xmvn 3.1.0][commons-jexl-2.1.1-changes]          |
| apache-commons-collections | 3.2.2   | [14.fc32][commons-collections_1-3.2.2-f32] | [fix build with xmvn 3.1.0][commons-collections_1-3.2.2-changes] |
| apache-commons-lang        | 2.6     | [26.fc32][commons-lang-2.6-f32]            | [fix build with xmvn 3.1.0][commons-lang-2.6-changes]            |
| xstream                    | 1.4.11  | [4.fc32][xstream-1.4.11-f32]               | [fix build with xmvn 3.1.0][xstream-1.4.11-changes]              |
| plexus-build-api           | 0.0.7   | [25.fc32][plexus-build-api_2-0.0.7-f32]    | [fix build with xmvn 3.1.0][plexus-build-api_2-0.0.7-changes]    |
| apache-commons-collections | 3.2.2   | [15.fc32][commons-collections_2-3.2.2-f32] | [fix build with xmvn 3.1.0][commons-collections_2-3.2.2-changes] |

- various small fixes and improvements:

| package                 | version  | release                                      | changes                                                                     |
| ----------------------- | -------- | -------------------------------------------- | --------------------------------------------------------------------------- |
| jackson-jaxrs-providers | 2.10.0   | [2.fc32][jackson-jaxrs-providers-2.10.0-f32] | [minimize build dependencies][jackson-jaxrs-providers-2.10.0-changes]       |
| xsom                    | 20140514 | [2.fc32][xsom-20140514-f32]                  | [fix regeneration of sources][xsom-20140514-changes]                        |
| munge-maven-plugin      | 1.0      | [15.fc32][munge-maven-plugin-1.0-f32]        | [drop unnecessary dependency on parent POM][munge-maven-plugin-1.0-changes] |

- another few version updates, including updates for the jackson stack that
  fixed some security issues:

| package                 | version | release                                      | changes                                                   |
| ----------------------- | ------- | -------------------------------------------- | --------------------------------------------------------- |
| google-gson             | 2.8.6   | [1.fc32][gson-2.8.6-f32]                     | [2.8.2 → 2.8.6][gson-2.8.6-changes]                       |
| jackson-bom             | 2.10.1  | [1.fc32][jackson-bom-2.10.1-f32]             | [2.10.0 → 2.10.1][jackson-bom-2.10.1-changes]             |
| jackson-annotations     | 2.10.1  | [1.fc32][jackson-annotations-2.10.1-f32]     | [2.10.0 → 2.10.1][jackson-annotations-2.10.1-changes]     |
| jackson-core            | 2.10.1  | [1.fc32][jackson-core-2.10.1-f32]            | [2.10.0 → 2.10.1][jackson-core-2.10.1-changes]            |
| jackson-databind        | 2.10.1  | [1.fc32][jackson-databind-2.10.1-f32]        | [2.10.0 → 2.10.1][jackson-databind-2.10.1-changes]        |
| jackson-modules-base    | 2.10.1  | [1.fc32][jackson-modules-base-2.10.1-f32]    | [2.10.0 → 2.10.1][jackson-modules-base-2.10.1-changes]    |
| jackson-jaxrs-providers | 2.10.1  | [1.fc32][jackson-jaxrs-providers-2.10.1-f32] | [2.10.0 → 2.10.1][jackson-jaxrs-providers-2.10.1-changes] |
| xbean                   | 4.15    | [1.fc32][xbean-4.15-f32]                     | [4.14 → 4.15][xbean-4.15-changes]                         |

- inter-dependent updates for various plexus packages and maven plugins:

| package                 | version  | release                                      | changes                                                                         |
| ----------------------- | -------- | -------------------------------------------- | ------------------------------------------------------------------------------- |
| plexus-archiver         | 4.2.1    | [1.fc32][plexus-archiver-4.2.1-f32]          | [4.1.0 → 4.2.1][plexus-archiver-4.2.1-changes]                                  |
| maven-archiver          | 3.5.0    | [1.fc32][maven-archiver-3.5.0-f32]           | [3.4.0 → 3.5.0][maven-archiver-3.5.0-changes]                                   |
| maven-jar-plugin        | 3.2.0    | [1.fc32][maven-jar-plugin-3.2.0-f32]         | [3.1.2 → 3.2.0][maven-jar-plugin-3.2.0-changes]                                 |
| maven-source-plugin     | 3.2.0    | [1.fc32][maven-source-plugin-3.2.0-f32]      | [3.1.0 → 3.2.0][maven-source-plugin-3.2.0-changes]                              |
| maven-artifact-transfer | 0.11.0   | [1.fc32][maven-artifact-transfer-0.11.0-f32] | [0.9.0 → 0.11.0][maven-artifact-transfer-0.11.0-changes]                        |
| maven-javadoc-plugin    | 3.1.1    | [1.fc32][maven-javadoc-plugin_1-3.1.1-f32]   | [3.0.1 → 3.1.1][maven-javadoc-plugin_1-3.1.1-changes]                           |
| maven-invoker-plugin    | 3.2.1    | [1.fc32][maven-invoker-plugin-3.2.1-f32]     | [3.2.0 → 3.2.1][maven-invoker-plugin-3.2.1-changes]                             |
| maven-dependency-plugin | 3.1.1    | [4.fc32][maven-dependency-plugin-3.1.1-f32]  | [port to maven-artifact-transfer 0.11.0][maven-dependency-plugin-3.1.1-changes] |
| maven-shade-plugin      | 3.2.1    | [2.fc32][maven-shade-plugin-3.2.1-f32]       | [port to maven-artifact-transfer 0.11.0][maven-shade-plugin-3.2.1-changes]      |
| maven-enforcer          | 3.0.0~M2 | [1.fc32][maven-enforcer-3.0.0~M2-f32]        | [port to maven-artifact-transfer 0.11.0][maven-enforcer-3.0.0~M2-changes]       |
| maven-resolver          | 1.4.1    | [1.fc32][maven-resolver-1.4.1-f32]           | [1.3.3 → 1.4.1][maven-resolver-1.4.1-changes]                                   |
| maven-assembly-plugin   | 3.2.0    | [1.fc32][maven-assembly-plugin-3.2.0-f32]    | [3.1.1 → 3.2.0][maven-assembly-plugin-3.2.0-changes]                            |
| maven-javadoc-plugin    | 3.1.1    | [2.fc32][maven-javadoc-plugin_2-3.1.1-f32]   | [non-bootstrap build with JavaDocs][maven-javadoc-plugin_2-3.1.1-changes]       |

- removing some unnecessary dependencies from our packages:

| package          | version | release                               | changes                                                                        |
| ---------------- | ------- | ------------------------------------- | ------------------------------------------------------------------------------ |
| jmock            | 2.8.2   | [9.fc32][jmock-2.8.2-f32]             | [drop unnecessary dependency on parent POM][jmock-2.8.2-changes]               |
| paranamer        | 2.8     | [11.fc32][paranamer-2.8-f32]          | [drop unnecessary dependency on parent POM][paranamer-2.8-changes]             |
| google-gson      | 2.8.6   | [2.fc32][gson-2.8.6-f32]              | [drop unnecessary dependency on parent POM][gson-2.8.6-changes]                |
| apache-ivy       | 2.4.0   | [19.fc32][ivy-2.4.0-f32]              | [remove unnecessary dependencies on parent POMs][ivy-2.4.0-changes]            |
| netty            | 4.1.13  | [13.fc32][netty-4.1.13-f32]           | [remove unnecessary dependency on parent POM][netty-4.1.13-changes]            |
| relaxngDatatype  | 2011.1  | [11.fc32][relaxngDatatype-2011.1-f32] | [remove unnecessary dependency on parent POM][relaxngDatatype-2011.1-changes]  |
| lzma-java        | 1.3     | [8.fc32][lzma-java-1.3-f32]           | [remove unnecessary dependency on parent POM][lzma-java-1.3-changes]           |
| os-maven-plugin  | 1.2.3   | [13.fc32][os-maven-plugin-1.2.3-f32]  | [remove unnecessary dependency on parent POM][os-maven-plugin-1.2.3-changes]   |
| qdox             | 2.0~M9  | [7.fc32][qdox-2.0~M9-f32]             | [remove unnecessary dependency on parent POM][qdox-2.0~M9-changes]             |
| sisu-mojos       | 0.3.4   | [2.fc32][sisu-mojos-0.3.4-f32]        | [remove unnecessary dependency on parent POM][sisu-mojos-0.3.4-changes]        |
| replacer         | 1.6     | [12.fc32][replacer-1.6-f32]           | [remove unnecessary dependency on parent POM][replacer-1.6-changes]            |
| maven            | 3.6.1   | [3.fc32][maven-3.6.1-f32]             | [require correct version of guava][maven-3.6.1-changes]                        |
| plexus-build-api | 0.0.7   | [26.fc32][plexus-build-api-0.0.7-f32] | [ remove unnecessary dependency on parent POM][plexus-build-api-0.0.7-changes] |

- and another two version updates:

| package               | version | release                                    | changes                                                 |
| --------------------- | ------- | ------------------------------------------ | ------------------------------------------------------- |
| glassfish-fastinfoset | 1.2.15  | [1.fc32][glassfish-fastinfoset-1.2.15-f32] | [1.2.13 → 1.2.15][glassfish-fastinfoset-1.2.15-changes] |
| beust-jcommander      | 1.78    | [1.fc32][jcommander-1.78-f32]              | [1.71 → 1.78][jcommander-1.78-changes]                  |


[glassfish-jax-rs-api-2.1.6-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1407256
[glassfish-jax-rs-api-2.1.6-changes]: https://src.fedoraproject.org/rpms/glassfish-jax-rs-api/c/28a575835e873342bab65680b323c80e4a08499a?branch=master

[commons-beanutils-1.9.4-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-bcad44b5d6
[commons-beanutils-1.9.4-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-79b5790566
[commons-beanutils-1.9.4-changes]: https://src.fedoraproject.org/rpms/apache-commons-beanutils/c/982e3969d44351d7824438d8c0f42237f46eab67?branch=master

[maven-3.6.1, 3.5.4-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1407606
[maven-3.6.1, 3.5.4-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-f3a7f84557
[maven-3.6.1, 3.5.4-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-89bce413cd
[maven-3.6.1, 3.5.4-changes]: https://src.fedoraproject.org/rpms/maven/c/d44e09e7c816ecd188a06f9200ec48d68f19c53b?branch=master

[plexus-utils-3.3.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1410590
[plexus-utils-3.3.0-changes]: https://src.fedoraproject.org/rpms/plexus-utils/c/f594d4a74dc51d5b18a46d50426796fc19114881?branch=master

[plexus-build-api_1-0.0.7-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1410591
[plexus-build-api_1-0.0.7-changes]: https://src.fedoraproject.org/rpms/plexus-build-api/c/45d5bf6793d85fbd433fa4f565481dab429c4669?branch=master

[plexus-io-3.2.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1410620
[plexus-io-3.2.0-changes]: https://src.fedoraproject.org/rpms/plexus-io/c/121f0add1cc0985a1b746c0c1df5e4466d075ea0?branch=master

[plexus-containers-2.1.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1410621
[plexus-containers-2.1.0-changes]: https://src.fedoraproject.org/rpms/plexus-containers/c/6cef84c140bb9214b3715710a4639d908fd2910e?branch=master

[log4j-2.12.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411254
[log4j-2.12.1-changes]: https://src.fedoraproject.org/rpms/log4j/c/3f6b65cc8e196d75d25c108716d986995e6b2a65?branch=master

[jsoup-1.12.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411288
[jsoup-1.12.1-changes]: https://src.fedoraproject.org/rpms/jsoup/c/b8353068c21e9b66fd117774bcdc146a67c60a2d?branch=master

[jvnet-parent-5-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411333
[jvnet-parent-5-changes]: https://src.fedoraproject.org/rpms/jvnet-parent/c/2a3192305941eb1aad9687b0605f030abf9887db?branch=master

[glassfish-jsp-api-2.3.3-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411372
[glassfish-jsp-api-2.3.3-changes]: https://src.fedoraproject.org/rpms/glassfish-jsp-api/c/2f4209cd49d6599de704cc5b6bc237f6e55f30a9?branch=master

[sisu-mojos-0.3.4-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411842
[sisu-mojos-0.3.4-changes]: https://src.fedoraproject.org/rpms/sisu-mojos/c/e18d2576c5ef5293851870f13db1ee2c892fb292?branch=master

[xmvn-3.1.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411883
[xmvn-3.1.0-changes]: https://src.fedoraproject.org/rpms/xmvn/c/3efff57c49fa934e501c9cc9f3f8e906a72e5b18?branch=master

[commons-jexl-2.1.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411991
[commons-jexl-2.1.1-changes]: https://src.fedoraproject.org/rpms/apache-commons-jexl/c/1b8f8e557d6dc70e210ac4de77b4f610005ac4e7?branch=master

[commons-collections_1-3.2.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411994
[commons-collections_1-3.2.2-changes]: https://src.fedoraproject.org/rpms/apache-commons-collections/c/5f7f14b8c68a1f91d0053561ce5c2d51c8889b83?branch=master

[commons-lang-2.6-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411996
[commons-lang-2.6-changes]: https://src.fedoraproject.org/rpms/apache-commons-lang/c/d8a053fdcba086d4ca4f50d698582bf22dab38be?branch=master

[xstream-1.4.11-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1411997
[xstream-1.4.11-changes]: https://src.fedoraproject.org/rpms/xstream/c/949d0657af50a163e5adfcfaad82dad164d3b5e7?branch=master

[jackson-jaxrs-providers-2.10.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1412007
[jackson-jaxrs-providers-2.10.0-changes]: https://src.fedoraproject.org/rpms/jackson-jaxrs-providers/c/1eddac6c311b9d329f67c060c7eef3244e8ca544?branch=master

[xsom-20140514-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1412226
[xsom-20140514-changes]: https://src.fedoraproject.org/rpms/xsom/c/651b0388c654b0c8d09a6e8feb006bbe24755463?branch=master

[plexus-build-api_2-0.0.7-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1412404
[plexus-build-api_2-0.0.7-changes]: https://src.fedoraproject.org/rpms/plexus-build-api/c/eaa6a2bce67f9390bba6039ee5a6be4dda160f00?branch=master

[commons-collections_2-3.2.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1413277
[commons-collections_2-3.2.2-changes]: https://src.fedoraproject.org/rpms/apache-commons-collections/c/73645073ade4ad8d783afe35002529229cf3a7a9?branch=master

[munge-maven-plugin-1.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1413703
[munge-maven-plugin-1.0-changes]: https://src.fedoraproject.org/rpms/munge-maven-plugin/c/67512e171e31d808628d671553c6f5a17439e44c?branch=master

[gson-2.8.6-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1413925
[gson-2.8.6-changes]: https://src.fedoraproject.org/rpms/google-gson/c/c50693bfd908bedf855a8d7a9bf3975289f0cdab?branch=master

[jackson-bom-2.10.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1413926
[jackson-bom-2.10.1-changes]: https://src.fedoraproject.org/rpms/jackson-bom/c/7f4ff8038d33302bce6d01cea4c6ca5633f35a01?branch=master

[jackson-annotations-2.10.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1413928
[jackson-annotations-2.10.1-changes]: https://src.fedoraproject.org/rpms/jackson-annotations/c/ae7eb99dc29581db8122a31cb4cc4526b59463b2?branch=master

[jackson-core-2.10.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1413932
[jackson-core-2.10.1-changes]: https://src.fedoraproject.org/rpms/jackson-core/c/9bfb20dda7882bdfd0068d3dc6d481c7c1911135?branch=master

[jackson-databind-2.10.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1413938
[jackson-databind-2.10.1-changes]: https://src.fedoraproject.org/rpms/jackson-databind/c/2a502f4a5d49a64868c33d21626b4ff3a678b951?branch=master

[jackson-modules-base-2.10.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1413940
[jackson-modules-base-2.10.1-changes]: https://src.fedoraproject.org/rpms/jackson-modules-base/c/6fe45024aa5cdd9cbfb475344b9b5308050bee18?branch=master

[jackson-jaxrs-providers-2.10.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1413942
[jackson-jaxrs-providers-2.10.1-changes]: https://src.fedoraproject.org/rpms/jackson-jaxrs-providers/c/697b2cb6fc2904943dd57e99341c09139b011adb?branch=master

[xbean-4.15-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415382
[xbean-4.15-changes]: https://src.fedoraproject.org/rpms/xbean/c/2457982fe1b2c462ff0e1b0070a1f62c5bb39512?branch=master

[plexus-archiver-4.2.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415384
[plexus-archiver-4.2.1-changes]: https://src.fedoraproject.org/rpms/plexus-archiver/c/e3df4db377423418e6cb187542b68ff3d5d26abe?branch=master

[maven-archiver-3.5.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415385
[maven-archiver-3.5.0-changes]: https://src.fedoraproject.org/rpms/maven-archiver/c/56fc14b7140b63783bb7077a01e12361afc65e34?branch=master

[maven-jar-plugin-3.2.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415390
[maven-jar-plugin-3.2.0-changes]: https://src.fedoraproject.org/rpms/maven-jar-plugin/c/29f1a75c7cd74560c5427e5001f14ab52c906769?branch=master

[maven-source-plugin-3.2.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415391
[maven-source-plugin-3.2.0-changes]: https://src.fedoraproject.org/rpms/maven-source-plugin/c/29c51266c0069f25d620d383187e01ef273cdf6b?branch=master

[maven-artifact-transfer-0.11.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415395
[maven-artifact-transfer-0.11.0-changes]: https://src.fedoraproject.org/rpms/maven-artifact-transfer/c/c778b2d071b961f25946c1c95945ca10b3e156c4?branch=master

[maven-javadoc-plugin_1-3.1.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415397
[maven-javadoc-plugin_1-3.1.1-changes]: https://src.fedoraproject.org/rpms/maven-javadoc-plugin/c/ee5abf3cdb1e70f99dcc77557642052214029d69?branch=master

[maven-invoker-plugin-3.2.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415406
[maven-invoker-plugin-3.2.1-changes]: https://src.fedoraproject.org/rpms/maven-invoker-plugin/c/c5d5d58711f1b9627b1262c1a4f87433996c0cf6?branch=master

[maven-dependency-plugin-3.1.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415409
[maven-dependency-plugin-3.1.1-changes]: https://src.fedoraproject.org/rpms/maven-dependency-plugin/c/46113c1fd4539e7f3ada22316a225e7982f654b9?branch=master

[maven-shade-plugin-3.2.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415412
[maven-shade-plugin-3.2.1-changes]: https://src.fedoraproject.org/rpms/maven-shade-plugin/c/014aa8848aa2b83c7b8534138742374487bbb205?branch=master

[maven-enforcer-3.0.0~M2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415418
[maven-enforcer-3.0.0~M2-changes]: https://src.fedoraproject.org/rpms/maven-enforcer/c/cd971bf4bad40f729be223803d7e01a256583fa1?branch=master

[maven-resolver-1.4.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415419
[maven-resolver-1.4.1-changes]: https://src.fedoraproject.org/rpms/maven-resolver/c/3127115011e3c892183f14a1c0b831d36abd47b9?branch=master

[maven-assembly-plugin-3.2.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415426
[maven-assembly-plugin-3.2.0-changes]: https://src.fedoraproject.org/rpms/maven-assembly-plugin/c/340bd7ba0cc3caea74cbc78d6f16db0374669512?branch=master

[maven-javadoc-plugin_2-3.1.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415435
[maven-javadoc-plugin_2-3.1.1-changes]: https://src.fedoraproject.org/rpms/maven-javadoc-plugin/c/cbfc5b253b55aa048b399b39e3186a072363f26b?branch=master

[jmock-2.8.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415652
[jmock-2.8.2-changes]: https://src.fedoraproject.org/rpms/jmock/c/db4ead7e21843ccceb1a6687627c08d78ce47f18?branch=master

[paranamer-2.8-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415653
[paranamer-2.8-changes]: https://src.fedoraproject.org/rpms/paranamer/c/608b04393318eebf9ddd44aee6e05f4f73ef1165?branch=master

[glassfish-fastinfoset-1.2.15-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415952
[glassfish-fastinfoset-1.2.15-changes]: https://src.fedoraproject.org/rpms/glassfish-fastinfoset/c/abe12008038503db94ff6bd23d043065a76508ed?branch=master

[gson-2.8.6-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1415954
[gson-2.8.6-changes]: https://src.fedoraproject.org/rpms/google-gson/c/a5fd3afaf158d67c45686556dc183fc00504a8c6?branch=master

[jcommander-1.78-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416242
[jcommander-1.78-changes]: https://src.fedoraproject.org/rpms/beust-jcommander/c/3672c195e123a8ff016dd36d79458e8d9457652e?branch=master

[ivy-2.4.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416243
[ivy-2.4.0-changes]: https://src.fedoraproject.org/rpms/apache-ivy/c/dda494c5f4c966601ea5c85a6cccaea63646a2c7?branch=master

[netty-4.1.13-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416252
[netty-4.1.13-changes]: https://src.fedoraproject.org/rpms/netty/c/1a8d3efba9f0ef361bc206a0d1b1ec3768d2be0b?branch=master

[relaxngDatatype-2011.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416255
[relaxngDatatype-2011.1-changes]: https://src.fedoraproject.org/rpms/relaxngDatatype/c/bd1b2a4e90134ecbe4cab5a13c7aa57cb0f684ee?branch=master

[lzma-java-1.3-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416256
[lzma-java-1.3-changes]: https://src.fedoraproject.org/rpms/lzma-java/c/e37fcb6814d81b28875a79487bb23c068bb5345b?branch=master

[os-maven-plugin-1.2.3-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416257
[os-maven-plugin-1.2.3-changes]: https://src.fedoraproject.org/rpms/os-maven-plugin/c/1f1e1c13cda5e30553582109f9d8d54886c041d2?branch=master

[qdox-2.0~M9-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416260
[qdox-2.0~M9-changes]: https://src.fedoraproject.org/rpms/qdox/c/ae925432ba3d00711381b353503128d4b11fd7e1?branch=master

[sisu-mojos-0.3.4-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416261
[sisu-mojos-0.3.4-changes]: https://src.fedoraproject.org/rpms/sisu-mojos/c/ec34b10d9e0d50a6d3bdad7d6e48ba504ed4fe36?branch=master

[replacer-1.6-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416262
[replacer-1.6-changes]: https://src.fedoraproject.org/rpms/replacer/c/cc08f61205aa89ac60749d563d3a8e139ae97e31?branch=master

[maven-3.6.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416263
[maven-3.6.1-changes]: https://src.fedoraproject.org/rpms/maven/c/decb58e8988eb52986d0ca6c9faa19f78963f836?branch=master

[plexus-build-api-0.0.7-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1416785
[plexus-build-api-0.0.7-changes]: https://src.fedoraproject.org/rpms/plexus-build-api/c/65d2dc9552ff0b55f60a6fdf815add75b24d0e78?branch=master

