The operating doctrine: the default pipeline, role delegation map, handoff protocol, QA gates, and external-writing discipline.

# protean-doctrine

The operating doctrine ingredient of the Protean Kit distribution. It carries the
default five-stage pipeline, the universal role delegation map, the standard
handoff protocol, the quality gates, the verification and tone discipline, and
the external-writing contract.

## What it installs and where

`install.sh` copies these tree-relative paths into the target directory, keeping
their relative layout:

| Path | Contents |
|---|---|
| `skills/protean-operating-doctrine/` | the doctrine skill |
| `skills/external-writing-discipline/` | the writing-discipline skill and its reference |
| `gates/protean-doctrine/` | the two gates and the leak blocklist |

## Install

```bash
bash install.sh --target <dir>
```

Preview without writing anything:

```bash
bash install.sh --target <dir> --dry-run
```

The installer uses Bash and coreutils only, makes zero network calls, prints
every path it writes, and refuses to run without `--target`. A dry run prints the
planned paths and writes no file and no directory.

Installs alone with this command, resolving only its required dependencies listed
in its manifest entry. Optional relationships are reported, not fetched.

## Requirements and recommendations

Requires none. Recommends none. This is the bottom of the dependency graph: it
constrains nothing else and nothing else is needed to use it.

## Use

Read `skills/protean-operating-doctrine/SKILL.md` first. It is always active for
any project run with the Protean pipeline and defines the stage order, the
ownership boundaries, and the gates a change must pass. Read
`skills/external-writing-discipline/SKILL.md` before posting prose to a human.

## Gates

| Gate | Command |
|---|---|
| internal-name gate | `python3 gates/protean-doctrine/check-internal-names.py .` |
| dangling-reference gate | `python3 gates/protean-doctrine/check-no-dangling-refs.py .` |

Both gates are stdlib-only, accept `--help`, exit 0 on a clean tree, and exit
non-zero on a violation. `tests/test_gates.py` exercises each gate against a
clean tree and against an injected bad fixture.

## Offline and cache behaviour

Used through the composer, this ingredient is fetched once from its pinned tag
and reused from a content-addressed cache keyed by commit SHA. `--offline`
performs zero network calls and fails closed when the cache entry is absent.

## Limits and open items

The doctrine ships procedure only. It does not ship platform mechanics for any
surface, and it names no host, credential, or internal path. No unresolved item
is carried by this ingredient.

## License

MIT. The committed `LICENSE` file is authoritative.
