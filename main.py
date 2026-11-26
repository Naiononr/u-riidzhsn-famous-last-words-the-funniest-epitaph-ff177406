#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — one original funny epitaph.

Deterministic, standard library only, no network, no randomness.
The line is a fixed string in the source.
"""

import os
import tempfile

LINE = "Here lies a man who said 'one more episode'."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        # World-readable so the grader can read it (mkstemp defaults to
        # 0600, which has got an entry rejected before).
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
