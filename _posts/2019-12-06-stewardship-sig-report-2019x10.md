---
title:      "Stewardship SIG Report (October 2019)"
layout:     post
date:       "2019-12-06 16:00:00"
tags:       fedora stewardship monthly
---

It's a bit late, but here's the complete run-down of what the Stewardship SIG
accomplished during the month of October.

To start off the month, we pushed some updates for the *Jackson* stack to fix
security issues that are present in versions earlier than 2.10.

| package             | version                              | release                                                                                                                      | changes                                              |
| ------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| jackson-parent      | [2.10][jackson-parent-2.10]          | [1.fc32][jackson-parent-2.10-f32], [1.fc31][jackson-parent-2.10-f31], [1.fc30][jackson-parent-2.10-f30]                      | [2.9.1.2 → 2.10][jackson-parent-2.10-changes]        |
| jackson-bom         | [2.10.0][jackson-bom-2.10.0]         | [1.fc32][jackson-bom-2.10.0-f32], [1.fc31][jackson-bom-2.10.0-f31], [1.fc30][jackson-bom-2.10.0-f30]                         | [2.9.9 → 2.10.0][jackson-bom-2.10.0-changes]         |
| jackson-annotations | [2.10.0][jackson-annotations-2.10.0] | [1.fc32][jackson-annotations-2.10.0-f32], [1.fc31][jackson-annotations-2.10.0-f31], [1.fc30][jackson-annotations-2.10.0-f30] | [2.9.9 → 2.10.0][jackson-annotations-2.10.0-changes] |
| jackson-core        | [2.10.0][jackson-core-2.10.0]        | [1.fc32][jackson-core-2.10.0-f32], [1.fc31][jackson-core-2.10.0-f31], [1.fc30][jackson-core-2.10.0-f30]                      | [2.9.9 → 2.10.0][jackson-core-2.10.0-changes]        |
| jackson-databind    | [2.10.0][jackson-databind-2.10.0]    | [1.fc32][jackson-databind-2.10.0-f32], [1.fc31][jackson-databind-2.10.0-f31], [1.fc30][jackson-databind-2.10.0-f30]          | [2.9.9.3 → 2.10.0][jackson-databind-2.10.0-changes]  |

[jackson-parent-2.10]: https://github.com/FasterXML/jackson-parent/blob/jackson-parent-2.10/release-notes/VERSION
[jackson-parent-2.10-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1396138
[jackson-parent-2.10-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-cf87377f5f
[jackson-parent-2.10-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-b171554877
[jackson-parent-2.10-changes]: https://github.com/FasterXML/jackson-parent/compare/jackson-parent-2.9.1.2...jackson-parent-2.10

[jackson-bom-2.10.0]: https://github.com/FasterXML/jackson-bom/blob/jackson-bom-2.10.0/release-notes/VERSION
[jackson-bom-2.10.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1396152
[jackson-bom-2.10.0-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-cf87377f5f
[jackson-bom-2.10.0-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-b171554877
[jackson-bom-2.10.0-changes]: https://github.com/FasterXML/jackson-bom/compare/jackson-bom-2.9.9...jackson-bom-2.10.0

[jackson-annotations-2.10.0]: https://github.com/FasterXML/jackson-annotations/blob/jackson-annotations-2.10.0-try-3/release-notes/VERSION-2.x
[jackson-annotations-2.10.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1396173
[jackson-annotations-2.10.0-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-cf87377f5f
[jackson-annotations-2.10.0-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-b171554877
[jackson-annotations-2.10.0-changes]: https://github.com/FasterXML/jackson-annotations/compare/jackson-annotations-2.9.9...jackson-annotations-2.10.0-try-3

[jackson-core-2.10.0]: https://github.com/FasterXML/jackson-core/blob/jackson-core-2.10.0/release-notes/VERSION-2.x
[jackson-core-2.10.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1396179
[jackson-core-2.10.0-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-cf87377f5f
[jackson-core-2.10.0-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-b171554877
[jackson-core-2.10.0-changes]: https://github.com/FasterXML/jackson-core/compare/jackson-core-2.9.9...jackson-core-2.10.0

[jackson-databind-2.10.0]: https://github.com/FasterXML/jackson-databind/blob/jackson-databind-2.10.0/release-notes/VERSION-2.x
[jackson-databind-2.10.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1396183
[jackson-databind-2.10.0-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-cf87377f5f
[jackson-databind-2.10.0-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-b171554877
[jackson-databind-2.10.0-changes]: https://github.com/FasterXML/jackson-databind/compare/jackson-databind-2.9.9.3...jackson-databind-2.10.0

I created a new package for `univocity-output-tester`, the absence of which was
previously the reason for the disabled test suite in the `univocity-parsers`
package. In the next update for it, the test suite will be enabled.

| package                 | version | release                                   | changes                                                  |
| ----------------------- | ------- | ----------------------------------------- | -------------------------------------------------------- |
| univocity-output-tester | 2.1     | [1.fc32][univocity-output-tester-2.1-f32] | [Initial packaging][univocity-output-tester-2.1-changes] |

[univocity-output-tester-2.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1397308
[univocity-output-tester-2.1-changes]: https://src.fedoraproject.org/rpms/univocity-output-tester

Next, I moved on to fixing some FTBFS issues. `paranamer` started to fail to
build a while ago due to it not depending on `ant` directly, but relying on it
transitively - that transitive dependency got removed at some point, so it just
had to be added in directly.

I also moved both `netty3`, `grizzly` and `grizzly-npn` away from the retired
*felix* OSGi implementation, since everything should use OSGi 7.0.0 from
`osgi-core` now.

| package     | version | release                                                    | changes                                                 |
| ----------- | ------- | ---------------------------------------------------------- | ------------------------------------------------------- |
| paranamer   | 2.8     | [10.fc32][paranamer-2.8-f32], [10.fc31][paranamer-2.8-f31] | [fix FTBFS issue on fedora 31+][paranamer-2.8-changes]  |
| netty3      | 3.10.6  | [8.fc32][netty3-3.10.6-f32]                                | [migrate away from felix OSGi][netty3-3.10.6-changes]   |
| grizzly-npn | 1.2     | [11.fc32][grizzly-npn-1.2-f32]                             | [migrate away from felix OSGi][grizzly-npn-1.2-changes] |
| grizzly     | 2.3.24  | [9.fc32][grizzly-2.3.24-f32]                               | [migrate away from felix OSGi][grizzly-2.3.24-changes]  |

[paranamer-2.8-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1397633
[paranamer-2.8-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-75c8e129ee
[paranamer-2.8-changes]: https://src.fedoraproject.org/rpms/paranamer/c/e3a2a19?branch=master

[netty3-3.10.6-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1397701
[netty3-3.10.6-changes]: https://src.fedoraproject.org/rpms/netty3/c/0ae6abc?branch=master

[grizzly-npn-1.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1397712
[grizzly-npn-1.2-changes]: https://src.fedoraproject.org/rpms/grizzly-npn/c/5d73894?branch=master

[grizzly-2.3.24-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400359
[grizzly-2.3.24-changes]: https://src.fedoraproject.org/rpms/grizzly/c/6ebde6d656cefa426983d2491a21934799a50406?branch=master

Next, I pushed minor updates for two of our packages (`aalto-xml` and
`commons-beanutils`) to rawhide:

| package                  | version                  | release                               | changes                                          |
| ------------------------ | ------------------------ | ------------------------------------- | ------------------------------------------------ |
| aalto-xml                | [1.2.2][aalto-xml-1.2.2] | [1.fc32][aalto-xml-1.2.2-f32]         | [1.0.0 → 1.2.2][aalto-xml-1.2.2-changes]         |
| apache-commons-beanutils | 1.9.4                    | [1.fc32][commons-beanutils-1.9.4-f32] | [1.9.3 → 1.9.4][commons-beanutils-1.9.4-changes] |

[aalto-xml-1.2.2]: https://github.com/FasterXML/aalto-xml/blob/aalto-xml-1.2.2/release-notes/VERSION
[aalto-xml-1.2.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1399385
[aalto-xml-1.2.2-changes]: https://github.com/FasterXML/aalto-xml/compare/aalto-xml-1.0.0...aalto-xml-1.2.2

[commons-beanutils-1.9.4-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1399392
[commons-beanutils-1.9.4-changes]: https://src.fedoraproject.org/rpms/apache-commons-beanutils/c/982e396?branch=master

After we updated `commons-compress` to the latest version in rawhide, we got a
report about a security issue in versions prior to 1.19, so we pushed that
change for the stable fedora releases as well.

| package                 | version | release                                                                                                       | changes                                      |
| ----------------------- | ------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| apache-commons-compress | 1.19    | [1.fc32][commons-compress-1.19-f32], [1.fc31][commons-compress-1.19-f31], [1.fc30][commons-compress-1.19-f30] | [1.18 → 1.19][commons-compress-1.19-changes] |

[commons-compress-1.19-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1399396
[commons-compress-1.19-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-da0eac1eb6
[commons-compress-1.19-f30]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-c96a8d12b0
[commons-compress-1.19-changes]: https://src.fedoraproject.org/rpms/apache-commons-compress/c/2888e52?branch=master

I went on to work on the unretirement of some packages that are still required
for the DogTag-PKI stack (via `resteasy`). The three packages in question went
through package re-review since they had been retired for a few months already.

| package                   | version | release                                                                                        | changes                                                         |
| ------------------------- | ------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| jboss-transaction-1.1-api | 1.0.1   | [19.fc32][jboss-transaction-1.1-api-1.0.1-f32], [19.fc31][jboss-transaction-1.1-api-1.0.1-f31] | [package unretirement][jboss-transaction-1.1-api-1.0.1-changes] |
| jandex                    | 2.1.1   | [1.fc32][jandex-2.1.1-f32], [1.fc31][jandex-2.1.1-f31]                                         | [package unretirement][jandex-2.1.1-changes]                    |
| maven-osgi                | 0.2.0   | [18.fc32][maven-osgi-0.2.0-f32], [18.fc31][maven-osgi-0.2.0-f31]                               | [package unretirement][maven-osgi-0.2.0-changes]                |

[jboss-transaction-1.1-api-1.0.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400008
[jboss-transaction-1.1-api-1.0.1-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-44f7c83dd1
[jboss-transaction-1.1-api-1.0.1-changes]: https://src.fedoraproject.org/rpms/jboss-transaction-1.1-api/c/35f1b5af86f3a665bc6ea5c1983f2530391d8cf0?branch=master

[jandex-2.1.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400011
[jandex-2.1.1-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-13f1c27914
[jandex-2.1.1-changes]: https://src.fedoraproject.org/rpms/jandex/c/fe5c6ec44b752e0596be1c2e62bee6b4a89d99b5?branch=master

[maven-osgi-0.2.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400014
[maven-osgi-0.2.0-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-6ff5c442a3
[maven-osgi-0.2.0-changes]: https://src.fedoraproject.org/rpms/maven-osgi/c/724b5f26304d176eb3344fb1cc0da4ca6a0263b5?branch=master

Next, I fixed new FTBFS issues for three of our packages by dropping unnecessary
dependencies on the `maven-release-plugin` and `buildnumber-maven-plugin`, since
both of these packages recently became non-installable in rawhide due to broken
dependencies.

| package               | version | release                                    | changes                                                           |
| --------------------- | ------- | ------------------------------------------ | ----------------------------------------------------------------- |
| hibernate-jpa-2.0-api | 1.0.1   | [25.fc32][hibernate-jpa-2.0-api-1.0.1-f32] | [fix FTBFS issue on rawhide][hibernate-jpa-2.0-api-1.0.1-changes] |
| picketbox-xacml       | 2.0.8   | [8.fc32][picketbox-xacml-2.0.8-f32]        | [fix FTBFS issue on rawhide][picketbox-xacml-2.0.8-changes]       |
| mimepull              | 1.9.6   | [10.fc32][mimepull-1.9.6-f32]              | [fix FTBFS issue on rawhide][mimepull-1.9.6-changes]              |

[hibernate-jpa-2.0-api-1.0.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400043
[hibernate-jpa-2.0-api-1.0.1-changes]: https://src.fedoraproject.org/rpms/hibernate-jpa-2.0-api/c/b18c4c891984fd98a7582c18cda7803bc9797672?branch=master

[picketbox-xacml-2.0.8-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400071
[picketbox-xacml-2.0.8-changes]: https://src.fedoraproject.org/rpms/picketbox-xacml/c/e56696cf05f2dcd039a8efb3e982f44dcc604dd3?branch=master

[mimepull-1.9.6-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400074
[mimepull-1.9.6-changes]: https://src.fedoraproject.org/rpms/mimepull/c/65504ea998a095fd677f38237fd3ec1e66e46d40?branch=master

And then came a long list of almost-alphabetical package updates for rawhide.
Guess in which order I worked through the list of outdated packages 😉️

| package                    | version | release                                        | changes                                                   |
| -------------------------- | ------- | ---------------------------------------------- | --------------------------------------------------------- |
| apache-commons-daemon      | 1.2.2   | [1.fc32][commons-daemon-1.2.2-f32]             | [1.2.0 → 1.2.2][commons-daemon-1.2.2-changes]             |
| apache-commons-vfs         | 2.4.1   | [1.fc32][commons-vfs-2.4.1-f32]                | [2.1 → 2.4.1][commons-vfs-2.4.1-changes]                  |
| bcel                       | 6.4.1   | [1.fc32][bcel-6.4.1-f32]                       | [6.3.1 → 6.4.1][bcel-6.4.1-changes]                       |
| compress-lzf               | 1.0.4   | [1.fc32][compress-lzf-1.0.4-f32]               | [1.0.3 → 1.0.4][compress-lzf-1.0.4-changes]               |
| fasterxml-oss-parent       | 38      | [1.fc32][fasterxml-oss-parent-38-f32]          | [34 → 38][fasterxml-oss-parent-38-changes]                |
| fusesource-pom             | 1.12    | [1.fc32][fusesource-pom-1.12-f32]              | [1.11 → 1.12][fusesource-pom-1.12-changes]                |
| hawtjni                    | 1.17    | [1.fc32][hawtjni-1.17-f32]                     | [1.16 → 1.17][hawtjni-1.17-changes]                       |
| jansi-native               | 1.8     | [1.fc32][jansi-native-1.8-f32]                 | [1.7 → 1.8][jansi-native-1.8-changes]                     |
| jboss-el-3.0-api           | 1.0.13  | [1.fc32][jboss-el-3.0-api-1.0.13-f32]          | [1.0.5 → 1.0.13][jboss-el-3.0-api-1.0.13-changes]         |
| jboss-interceptors-1.2-api | 1.0.1   | [1.fc32][jboss-interceptors-1.2-api-1.0.1-f32] | [1.0.0 → 1.0.1][jboss-interceptors-1.2-api-1.0.1-changes] |
| jboss-jsp-2.3-api          | 1.0.3   | [1.fc32][jboss-jsp-2.3-api-1.0.3-f32]          | [1.0.1 → 1.0.3][jboss-jsp-2.3-api-1.0.3-changes]          |
| jboss-logging              | 3.4.1   | [1.fc32][jboss-logging-3.4.1-f32]              | [3.3.0 → 3.4.1][jboss-logging-3.4.1-changes]              |
| jboss-servlet-3.1-api      | 1.0.2   | [1.fc32][jboss-servlet-3.1-api-1.0.2-f32]      | [1.0.0 → 1.0.2][jboss-servlet-3.1-api-1.0.2-changes]      |
| jettison                   | 1.4.0   | [1.fc32][jettison-1.4.0-f32]                   | [1.3.7 → 1.4.0][jettison-1.4.0-changes]                   |
| jboss-transaction-1.2-api  | 1.1.1   | [1.fc32][jboss-transaction-1.2-api-1.1.1-f32]  | [1.0.1 → 1.1.1][jboss-transaction-1.2-api-1.1.1-changes]  |
| junit5                     | 5.5.2   | [1.fc32][junit5-5.5.2-f32]                     | [5.4.2 → 5.5.2][junit5-5.5.2-changes]                     |

[commons-daemon-1.2.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400243
[commons-daemon-1.2.2-changes]: https://src.fedoraproject.org/rpms/apache-commons-daemon/c/854f875723f351012a3ee0871ac546e73c07c17f?branch=master

[commons-vfs-2.4.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400245
[commons-vfs-2.4.1-changes]: https://src.fedoraproject.org/rpms/apache-commons-vfs/c/a278a08b8689a876c580f31442a9e08285b13b01?branch=master

[bcel-6.4.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400249
[bcel-6.4.1-changes]: https://src.fedoraproject.org/rpms/bcel/c/1f242b6e285dfad54ac93f31018e7813bf28916d?branch=master

[compress-lzf-1.0.4-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400251
[compress-lzf-1.0.4-changes]: https://src.fedoraproject.org/rpms/compress-lzf/c/b0ada817f79ac6feeebb12f066e934430990b404?branch=master

[fasterxml-oss-parent-38-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400255
[fasterxml-oss-parent-38-changes]: https://src.fedoraproject.org/rpms/fasterxml-oss-parent/c/1c86b1de37300b44b22ea2a6355549189aea6db3?branch=master

[fusesource-pom-1.12-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400258
[fusesource-pom-1.12-changes]: https://src.fedoraproject.org/rpms/fusesource-pom/c/2bdfb0212be1b7300e77bf1efb5d49dd727e2221?branch=master

[hawtjni-1.17-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400261
[hawtjni-1.17-changes]: https://src.fedoraproject.org/rpms/hawtjni/c/c6c56b3e1a5eb705c8ba50c5fc0d6e7c939dc99f?branch=master

[jansi-native-1.8-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400262
[jansi-native-1.8-changes]: https://src.fedoraproject.org/rpms/jansi-native/c/7bdf6329e4a7f8e85fc6468f4eee43d8c8826120?branch=master

[jboss-el-3.0-api-1.0.13-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400263
[jboss-el-3.0-api-1.0.13-changes]: https://src.fedoraproject.org/rpms/jboss-el-3.0-api/c/9d88e2edf6575edd95ff300d912e820fd1d4eb4c?branch=master

[jboss-interceptors-1.2-api-1.0.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400268
[jboss-interceptors-1.2-api-1.0.1-changes]: https://src.fedoraproject.org/rpms/jboss-interceptors-1.2-api/c/8ab2d872cb9f504bb605b1058b769f0bdf757a38?branch=master

[jboss-jsp-2.3-api-1.0.3-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400270
[jboss-jsp-2.3-api-1.0.3-changes]: https://src.fedoraproject.org/rpms/jboss-jsp-2.3-api/c/ee4e690606bf5d90f2b274b380e59c1021b3d6d7?branch=master

[jboss-logging-3.4.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400272
[jboss-logging-3.4.1-changes]: https://src.fedoraproject.org/rpms/jboss-logging/c/41e10416ec3eb2e715ddd929a7433448d8722b7d?branch=master

[jboss-servlet-3.1-api-1.0.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400273
[jboss-servlet-3.1-api-1.0.2-changes]: https://src.fedoraproject.org/rpms/jboss-servlet-3.1-api/c/d1007a6e48881eb846cae1b27a4b48e50fb5f0d0?branch=master

[jettison-1.4.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400276
[jettison-1.4.0-changes]: https://src.fedoraproject.org/rpms/jettison/c/c7ad1c78f23d713702fbab89c28b31c72760f704?branch=master

[jboss-transaction-1.2-api-1.1.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400277
[jboss-transaction-1.2-api-1.1.1-changes]: https://src.fedoraproject.org/rpms/jboss-transaction-1.2-api/c/c035c776492bc93be1a14ee0aafb148a9550a5e6?branch=master

[junit5-5.5.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400278
[junit5-5.5.2-changes]: https://src.fedoraproject.org/rpms/junit5/c/5a58d7d5207cd1e3637b6c52812e5caf26d2e305?branch=master

We also decided to drop FOP support in `maven-doxia` since it isn't used by any
fedora package and only introduced a dependency on FOP, which is currently
broken in fedora and might get removed completely soon.

| package               | version | release                                 | changes                                                   |
| --------------------- | ------- | --------------------------------------- | --------------------------------------------------------- |
| maven-doxia-sitetools | 1.9     | [2.fc32][maven-doxia-sitetools-1.9-f32] | [disabled FOP support][maven-doxia-sitetools-1.9-changes] |
| maven-doxia           | 1.9     | [3.fc32][maven-doxia-1.9-f32]           | [disabled FOP support][maven-doxia-1.9-changes]           |

[maven-doxia-sitetools-1.9-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400279
[maven-doxia-sitetools-1.9-changes]: https://src.fedoraproject.org/rpms/maven-doxia-sitetools/c/42c24ad69ac0d62a9565cada6be96e13542a1f29?branch=master

[maven-doxia-1.9-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400301
[maven-doxia-1.9-changes]: https://src.fedoraproject.org/rpms/maven-doxia/c/f954caac3296ec23af05e3fd482e801362497c6c?branch=master

Here, the list of almost-alphabetical package updates for rawhide continues.

| package                 | version                          | release                                   | changes                                                             |
| ----------------------- | -------------------------------- | ----------------------------------------- | ------------------------------------------------------------------- |
| plexus-interactivity    | 1.0                              | [1.fc32][plexus-interactivity-1.0-f32]    | [1.0~alpha6 → 1.0][plexus-interactivity-1.0-changes]                |
| plexus-languages        | 1.0.3                            | [1.fc32][plexus-languages-1.0.3-f32]      | [0.9.10 → 1.0.3][plexus-languages-1.0.3-changes]                    |
| maven-compiler-plugin   | 3.8.1                            | [3.fc32][maven-compiler-plugin-3.8.1-f32] | [port to plexus-languages 1.0][maven-compiler-plugin-3.8.1-changes] |
| plexus-resources        | 1.1.0                            | [1.fc32][plexus-resources-1.1.0-f32]      | [1.0~alpha7 → 1.1.0][plexus-resources-1.1.0-changes]                |
| plexus-utils            | 3.2.1                            | [1.fc32][plexus-utils-3.2.1-f32]          | [3.2.0 → 3.2.1][plexus-utils-3.2.1-changes]                         |
| shrinkwrap              | 1.2.6                            | [1.fc32][shrinkwrap-1.2.6-f32]            | [1.2.3 → 1.2.6][shrinkwrap-1.2.6-changes]                           |
| sonatype-plugins-parent | 9                                | [1.fc32][sonatype-plugins-parent-9-f32]   | [8 → 9][sonatype-plugins-parent-9-changes]                          |
| stax2-api               | 4.2                              | [1.fc32][stax2-api-4.2-f32]               | [4.0.0 → 4.2][stax2-api-4.2-changes]                                |
| univocity-parsers       | [2.8.3][univocity-parsers-2.8.3] | [1.fc32][univocity-parsers-2.8.3-f32]     | [2.5.5 → 2.8.3][univocity-parsers-2.8.3-changes]                    |
| weld-parent             | 39                               | [1.fc32][weld-parent-39-f32]              | [34 → 39][weld-parent-39-changes]                                   |

[plexus-interactivity-1.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400282
[plexus-interactivity-1.0-changes]: https://src.fedoraproject.org/rpms/plexus-interactivity/c/9fc39d863473a4f2d5476e5abdda6214893302a7?branch=master

[plexus-languages-1.0.3-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400283
[plexus-languages-1.0.3-changes]: https://src.fedoraproject.org/rpms/plexus-languages/c/82498229c3896c27866075286f257673e9ed602f?branch=master

[maven-compiler-plugin-3.8.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400341
[maven-compiler-plugin-3.8.1-changes]: https://src.fedoraproject.org/rpms/maven-compiler-plugin/c/f20eb5a72261e94dd67dafaa3d9e9f3574213540?branch=master

[plexus-resources-1.1.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400288
[plexus-resources-1.1.0-changes]: https://src.fedoraproject.org/rpms/plexus-resources/c/c60d2a527958b920669d3b53890298fe7b952500?branch=master

[plexus-utils-3.2.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400289
[plexus-utils-3.2.1-changes]: https://src.fedoraproject.org/rpms/plexus-utils/c/9bb5adca81d7b367db46f74e314c8124d07ac6cf?branch=master

[shrinkwrap-1.2.6-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400291
[shrinkwrap-1.2.6-changes]: https://src.fedoraproject.org/rpms/shrinkwrap/c/0833bac0b2fd8d3ccbcef5452550cbe658de18cc?branch=master

[sonatype-plugins-parent-9-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400292
[sonatype-plugins-parent-9-changes]: https://src.fedoraproject.org/rpms/sonatype-plugins-parent/c/3d52e4267841bf4e83af8fc1dcd81453efea65d5?branch=master

[stax2-api-4.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400293
[stax2-api-4.2-changes]: https://src.fedoraproject.org/rpms/stax2-api/c/59024355fbaca1c55122db231d2a381747f207d6?branch=master

[univocity-parsers-2.8.3-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400294
[univocity-parsers-2.8.3-changes]: https://src.fedoraproject.org/rpms/univocity-parsers/c/2f9219871eb1185be8b3883418108a55edcbbf40?branch=master

[weld-parent-39-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400296
[weld-parent-39-changes]: https://src.fedoraproject.org/rpms/weld-parent/c/97ef1048dcd957f285dc0d4a63a39d3f8d24f42e?branch=master

We also worked on some small improvements for `snakeyaml` -- first, I backported
an upstream patch to fix a broken test, and second, I replaced its usage of the
`base64coder` package with directly calling the Base64 implementation that has
been present in OpenJDK since Java 8.

| package   | version | release                        | changes                                                               |
| --------- | ------- | ------------------------------ | --------------------------------------------------------------------- |
| snakeyaml | 1.25    | [2.fc32][snakeyaml_1-1.25-f32] | [backport upstream fix for a broken test][snakeyaml_1-1.25-changes]   |
| snakeyaml | 1.25    | [3.fc32][snakeyaml_2-1.25-f32] | [replace base64coder with Base64 from JDK8][snakeyaml_2-1.25-changes] |

[snakeyaml_1-1.25-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1400350
[snakeyaml_1-1.25-changes]: https://src.fedoraproject.org/rpms/snakeyaml/c/b6f623fe3aecc90acf860abf2202eb5bcadcc333?branch=master

[snakeyaml_2-1.25-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1401487
[snakeyaml_2-1.25-changes]: https://src.fedoraproject.org/rpms/snakeyaml/c/dce9f85ea3520f4e69ab34270ab346f9b8b967fd?branch=master

Last, here's the list of package updates that didn't I didn't quite manage to
prepare in alphabetical order (😆️), or where reviewing my Pull Request took a
bit longer. This list includes the noteworthy update of *Maven* to the 3.6
branch.

| package                  | version              | release                                      | changes                                               |
| ------------------------ | -------------------- | -------------------------------------------- | ----------------------------------------------------- |
| maven-enforcer           | 3.0.0~M2             | [1.fc32][maven-enforcer-3.0.0~M2-f32]        | [1.4.1 → 3.0.0~M2][maven-enforcer-3.0.0~M2-changes]   |
| woodstox-core            | 6.0.2                | [1.fc32][woodstox-core-6.0.2-f32]            | [6.0.1 → 6.0.2][woodstox-core-6.0.2-changes]          |
| xalan-j2                 | 2.7.2                | [1.fc32][xalan-j2-2.7.2-f32]                 | [2.7.1 → 2.7.2][xalan-j2-2.7.2-changes]               |
| freemarker               | 2.3.29               | [1.fc32][freemarker-2.3.29-f32]              | [2.3.28 → 2.3.29][freemarker-2.3.29-changes]          |
| plexus-pom               | 5.1                  | [1.fc32][plexus-pom-5.1-f32]                 | [5.0 → 5.1][plexus-pom-5.1-changes]                   |
| xsom                     | 20140514             | [1.fc32][xsom-20140514-f32]                  | [20110809 → 20140514][xsom-20140514-changes]          |
| maven                    | [3.6.1][maven-3.6.1] | [1.fc32][maven-3.6.1-f32]                    | [3.5.4 → 3.6.1][maven-3.6.1-changes]                  |
| glassfish-dtd-parser     | 1.4                  | [1.fc32][glassfish-dtd-parser-1.4-f32]       | [1.2.0 → 1.4][glassfish-dtd-parser-1.4-changes]       |
| glassfish-annotation-api | 1.3.2                | [1.fc32][glassfish-annotation-api-1.3.2-f32] | [1.2 → 1.3.2][glassfish-annotation-api-1.3.2-changes] |

[maven-enforcer-3.0.0~M2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1401549
[maven-enforcer-3.0.0~M2-changes]: https://src.fedoraproject.org/rpms/maven-enforcer/c/e956ca25cf233ad4672a8c75cc6154836009eb8f?branch=master

[woodstox-core-6.0.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1403333
[woodstox-core-6.0.2-changes]: https://src.fedoraproject.org/rpms/woodstox-core/c/7847b4fe67149fdcbd07fc5b9663e17431116e5f?branch=master

[xalan-j2-2.7.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1403340
[xalan-j2-2.7.2-changes]: https://src.fedoraproject.org/rpms/xalan-j2/c/e9e6176bd06e506f5c4106b37a35669b8417368a?branch=master

[freemarker-2.3.29-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1404187
[freemarker-2.3.29-changes]: https://src.fedoraproject.org/rpms/freemarker/c/9bcc855dfeb1ab67c43a001906b8e4026cec629c?branch=master

[plexus-pom-5.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1404350
[plexus-pom-5.1-changes]: https://src.fedoraproject.org/rpms/plexus-pom/c/ebe613f237560040297a3521c4db96fddc4f4af9?branch=master

[xsom-20140514-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1404363
[xsom-20140514-changes]: https://src.fedoraproject.org/rpms/xsom/c/699532754eebad5363ac1639fd61631f94622fb3?branch=master

[maven-3.6.1]: https://maven.apache.org/docs/3.6.1/release-notes.html
[maven-3.6.1-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1404702
[maven-3.6.1-changes]: https://src.fedoraproject.org/rpms/maven/c/643adf370f8a66fc93c1d282a1399038c2a9c21b?branch=master

[glassfish-dtd-parser-1.4-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1405500
[glassfish-dtd-parser-1.4-changes]: https://src.fedoraproject.org/rpms/glassfish-dtd-parser/c/91abc6fd72d4517446e18f7d6633a26aa9216773?branch=master

[glassfish-annotation-api-1.3.2-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1405502
[glassfish-annotation-api-1.3.2-changes]: https://src.fedoraproject.org/rpms/glassfish-annotation-api/c/4d67f718c294e1256037d8ec80d1669d4bee5f64?branch=master

Squeezing in one last update before the end of October, we managed to get
`glassfish-hk2` building again by dropping some of the functionality that's not
actually being used in fedora.

| package       | version | release                                                              | changes                                                                   |
| ------------- | ------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| glassfish-hk2 | 2.5.0   | [5.fc32][glassfish-hk2-2.5.0-f32], [5.fc31][glassfish-hk2-2.5.0-f31] | [disable unused functionality to fix builds][glassfish-hk2-2.5.0-changes] |

[glassfish-hk2-2.5.0-f32]: https://koji.fedoraproject.org/koji/buildinfo?buildID=1403602
[glassfish-hk2-2.5.0-f31]: https://bodhi.fedoraproject.org/updates/FEDORA-2019-a0e393f792
[glassfish-hk2-2.5.0-changes]: https://src.fedoraproject.org/rpms/glassfish-hk2/c/9f094f4e2b20a7b5a4a6af78ecf4a952f417159c?branch=master

