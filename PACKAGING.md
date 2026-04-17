# Mojackhak Fork Release Contract

This document defines the packaging and release policy for the Mojackhak fork of Aniposelib.

## Scope

This fork keeps the upstream distribution and import names:

- distribution name: `aniposelib`
- import name: `aniposelib`

## Fork Identity

Required package metadata:

- `url` points to `https://github.com/Mojackhak/aniposelib`
- project URLs include both the fork repository and the upstream repository
- package description explicitly identifies this build as the Mojackhak fork

## Versioning

Use PEP 440 compatible post releases for fork packaging:

- upstream base: `0.7.12`
- first fork release: `0.7.12.post1`
- later fork releases: `0.7.12.postN`

## Tags

Use annotated tags for release points.

Tag format:

- `mojackhak-aniposelib-v<version>`

Example:

- `mojackhak-aniposelib-v0.7.12.post1`

## Release Artifacts

Each release tag must produce:

- source distribution
- wheel
- GitHub Release entry with uploaded artifacts

## Validation

Each release build must validate:

- `python -m build`
- `python -m twine check dist/*`
- `import aniposelib`
