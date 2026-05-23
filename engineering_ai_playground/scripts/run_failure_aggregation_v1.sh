#!/usr/bin/env bash
set -e

python summarize_failures.py
python tools/verify_failure_counts.py
echo "ALL GOOD"
