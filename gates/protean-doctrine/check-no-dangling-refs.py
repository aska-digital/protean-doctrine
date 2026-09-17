#!/usr/bin/env python3
"""check-no-dangling-refs.py - every local reference a shipped skill makes must resolve.

Scans every Markdown file in the repository for (a) relative Markdown links and
(b) inline code spans that look like repository paths, and fails when the target
does not exist on disk. A skill that cites a module it does not ship is a defect:
the reader is sent to a file that was never installed.

Usage: python3 gates/check-no-dangling-refs.py [path/to/repo]
Exit: 0 every reference resolves; 1 at least one dangling reference.
"""
import os
import re
import sys

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv"}
# Path-like code spans must start with one of these repository-relative roots.
ROOTS = ("skills/", "scripts/", "gates/", "tests/", "templates/", "records/",
         "docs/", "build/", "examples/")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
CODE_RE = re.compile(r"`([^`\n]+)`")


def local_targets(text):
    for match in LINK_RE.finditer(text):
        target = match.group(1)
        if "://" in target or target.startswith(("mailto:", "#")):
            continue
        yield target.split("#", 1)[0]
    for match in CODE_RE.finditer(text):
        candidate = match.group(1).strip()
        if candidate.startswith(ROOTS):
            yield candidate.split("#", 1)[0]


def main():
    repo = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    if "--help" in sys.argv:
        print(__doc__.strip())
        return 0
    dangling = []
    scanned = 0
    for root, dirs, files in os.walk(repo):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            if not name.endswith((".md", ".tmpl")):
                continue
            abspath = os.path.join(root, name)
            rel = os.path.relpath(abspath, repo).replace(os.sep, "/")
            scanned += 1
            with open(abspath, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            for target in local_targets(text):
                if not target:
                    continue
                probe = target.rstrip("/")
                if not os.path.exists(os.path.join(repo, probe)):
                    dangling.append((rel, target))
    if dangling:
        print("DANGLING REFERENCE: " + str(len(dangling)) + " finding(s)")
        for rel, target in dangling[:40]:
            print("  " + rel + " -> " + target)
        return 1
    print("clean: " + str(scanned) + " markdown files, every local reference resolves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
