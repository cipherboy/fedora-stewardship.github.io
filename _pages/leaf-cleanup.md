---
title:      SIG leaf package cleanup
layout:     page
permalink:  /leaf-cleanup/
updated:    2020-02-21
---

To try to reduce the number of packages that are maintained by this SIG, there
is a regular "SIG leaf package" cleanup process.

For this purpose, it's convenient to use the `check_sig_leaf.py` script to check
"leaf" status for packages more comprehensively than for the automatically
generated report.

To reduce the time necessary to gather the data, an incremental approach is
helpful. First, start with the packages listed as "SIG leaves" on the
[report page](/report/#sig-leaves) and check for non-SIG packages that are
considered "worth keeping" (right now, `dogtag-pki`).

```bash
./check_sig_leaves.py \
    --include WORTH_KEEPING [--include WORTH_KEEPING ...] \
    --maxdepth 4 \
    LEAF_CANDIDATE [LEAF_CANDIDATE ...]
```

The script will check dependency chains up to the specified length, and report
any packages that are not "SIG leaves". Remove those packages from the list of
leaf candidates, increment the maximal depth of the dependency graph, and
continue this process until you are satisfied that the remaining packages are
indeed "SIG leaves" (usually a depth of 12-15 is enough).

For the list of confirmed "SIG leaves", open a new "SIG leaf cleanup" ticket in
the pagure project, list the packages, and ask for comments. Once the list is
ACK'd by another SIG member, ask on the devel mailing list for new maintainers
(possibly CC any maintainers of dependent packages). If nobody wants to take
over maintenance of the packages within two weeks, [orphan](/orphaning/) the
packages and announce this on the devel list.

---

**NOTE**: It's also possible that a package becomes a **total** leaf package in
fedora rawhide (probably because other packages dropped their dependencies on
it, and no such dependencies are left, or because dependent packages were
removed). In such cases, obviously skip the dependency checks outlined above,
and orphan the package straight away.
