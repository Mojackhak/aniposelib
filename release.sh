#!/usr/bin/env bash
set -euo pipefail

rm -rf dist build *.egg-info
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
echo "Artifacts are ready in dist/. Publish through the tag-driven GitHub Actions workflow."
