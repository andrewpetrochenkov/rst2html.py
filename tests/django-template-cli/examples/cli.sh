#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set "${BASH_SOURCE[0]%/*}"/index.html
django-template-cli "$@"
