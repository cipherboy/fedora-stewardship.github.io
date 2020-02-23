---
title:      Dependent packages
layout:     page
permalink:  /dependents/
updated:    2020-02-21
---

## Dogtag PKI

 - URL: <https://www.dogtagpki.org>
 - GitHub: <https://github.com/dogtagpki>
 - Main component: PKI
 - Point of Contact: <pki-devel@redhat.com>

### Overview

Dogtag provides the PKI component for FreeIPA, which has self-selected as
a key component in Fedora. Not breaking Dogtag (and thus FreeIPA) becomes
a requirement for Fedora releases. Dogtag started under Netscape, was
acquired by Mozilla, and is now part of Red Hat's offerings as Red Hat
Certificate System (RHCS). The core component is built on Tomcat and uses
RESTEasy for the API interface.

### SIG Dependencies

The following packages are currently maintained by the SIG and are used
by Dogtag and its dependents:

 - apache-commons-collections
 - apache-commons-daemon
 - apache-commons-lang
 - glassfish-fastinfoset
 - jakarta-commons-httpclient
 - slf4j
 - velocity
 - xalan-j2
 - xsom

### Testing Procedure

PKI runs commit-triggered builds in their [COPR][pki-copr] against all
current Fedora builds and Rawhide. This might catch problems in build-time
dependencies. If you're particularly concerned about a package update or
rebase, feel free to contact the mailing list above and we'll be happy to
run a quick smoke test.

<!-- Links -->
[pki-copr]: https://copr.fedorainfracloud.org/coprs/g/pki/master/

