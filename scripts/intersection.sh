#!/bin/bash

set -euo pipefail

repoquery="/tmp/stewardship-sig-repoquery.txt"
maintained="/tmp/stewardship-sig-maintained.txt"
api="https://src.fedoraproject.org/api/0/group/stewardship-sig?projects=true"

if [ "$1" == "--help" ] || [ "$1" == "-h" ]; then
    echo "Usage: intersection.sh [--help] packages..."
    echo ""
    echo "Find the dependencies of a set of packages maintained by the SIG."
    exit 0
fi

# Search for all recursive dependencies (Requires) of a list of packages,
# including both Requires and BuildRequires. Only shows results for the
# current rawhide.
dnf repoquery --requires --recursive --resolve --repo=fedora \
              --repo=fedora-source --releasever=rawhide "$@" 2>/dev/null |
    sed -e 's/ [| \\\_]\+\|-[[:digit:]]\+..*\|[[:digit:]]\://g' > "$repoquery.tmp"

sort -u < "$repoquery.tmp" > "$repoquery"

# Check for an empty repoquery file as that usually indicates an error
if [ ! -s "$repoquery" ]; then
    echo Error: "$@" have no dependencies or doesn\'t exist.
    exit 1
fi

# Download the current list of SIG-maintained packages from the API
curl -s "$api" |
    jq -r '.projects[].name?' |
    sort -u > "$maintained"

# Check for an empty maintained file as that usually indicates an error
if [ ! -s "$maintained" ]; then
    echo Error: Fedora project API changed or internal failure.
    exit 1
fi

# Show the common packages and clean up after ourselves
comm -1 -2 "$repoquery" "$maintained"
rm -f "$repoquery" "$repoquery.tmp" "$maintained"
