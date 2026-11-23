"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line (<=160 chars) to /output/entry.txt.

The line: the 3 a.m. replay bug -- the brain replays your most
embarrassing moment from 2014 instead of letting you sleep. A
version number, a terse engineering register, and a fix stated as shipped.
"""

import os
from pathlib import Path

LINE = (
    "v2.1.0: fixed a bug where the brain replays your most embarrassing "
    "moment from 2014 at 3 a.m. instead of sleeping."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
    # not only white space. Write the line with no trailing newline so the
    # counted length is exactly the line itself.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, gate is 1-160"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE, "entry must be a single line (judge criterion 1)"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
