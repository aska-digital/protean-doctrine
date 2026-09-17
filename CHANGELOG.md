# Changelog

All notable changes to this repository are recorded here. The format is a short
entry per release: what changed, why, and how it was verified.

## 1.1.0

- **What:** add section 13.1, *Continual contribution - the standing duty, made mechanical*, to
  the operating-doctrine skill. Section 13 already made contribution a standing duty; 13.1 gives
  the duty a clock and a stop condition: the two modes (an always-on internal mode, and an
  external mode off by default behind one flag), the idle predicate that starts a bounded lane,
  what a lane must carry before it contributes, who audits it, and what is never done.
- **Why:** a standing duty with no trigger is a preference. The duty needed a defined moment to
  run, a definition of when it must not run, and an audit that no author can perform on their own
  work.
- **Division of the feature:** this section carries the duty and the pointers. The rule lives in
  the `protean-control-plane` skill, the value and the enforcement command live in the
  contribution-state record and gate of the `protean-ops` ingredient, and the drafting and
  rendering mechanics live with the GitHub workflow pack and the draft pipeline. No bounded value
  is restated here, so there is no second home for a threshold.
- **Evidence class:** [VERIFIED - internal operating record] for the bounded values and the
  mode definitions.
- **Verification:** `python3 gates/protean-doctrine/check-internal-names.py .`,
  `python3 gates/protean-doctrine/check-no-dangling-refs.py .`, and
  `python3 -m unittest discover -s tests` pass from a clean checkout of this commit. The new
  section cites the other ingredients by name only, so no local reference is added that a
  doctrine-only install cannot resolve.
- **Descriptor note:** this entry also brings the descriptor, the installer banner, and the skill
  frontmatter to one version (`1.1.0`). They had drifted apart, and a single version is what the
  composer needs to pin.
- **License:** MIT. The committed `LICENSE` file is authoritative.

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
