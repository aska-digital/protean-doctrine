# Changelog

All notable changes to this repository are recorded here. The format is a short
entry per release: what changed, why, and how it was verified.

## 1.0.1

- **What:** correct the continuous-integration workflow matrix expression. The
  value was written with doubled braces, which made the expression invalid and
  would have stopped the job from running.
- **Why released as a patch, not as an edit:** the `v1.0.0` tag is published, and
  a published tag is never re-pointed. The correction ships as `v1.0.1`.
- **Verification:** the workflow parses as YAML and the matrix expression resolves;
  the declared gates and the test suite pass unchanged.

## 1.0.0

- **What:** the first release of the `protean-doctrine` ingredient: the capability payload,
  the machine descriptor `protean-ingredient.json`, the standalone installer
  `install.sh`, the declared gates under `gates/protean-doctrine/`, and the test suite under
  `tests/`.
- **Why:** the capability was previously reachable only from inside a private
  working tree. This repository is its single public home, installable on its own.
- **Verification:** the declared gates and `python3 -m unittest discover -s tests`
  pass from a clean checkout of this commit. See the pull request body for the
  commands and their output.
- **Contract:** `The operating doctrine: the default pipeline, role delegation map, handoff protocol, QA gates, and external-writing discipline.`
- **License:** MIT. The committed `LICENSE` file is authoritative.
