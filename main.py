"""Ship It Friday: write one funny Friday-deploy commit message to entry.txt.

The program is deterministic: it always writes the same single line, so two
runs produce byte-identical output.

Output directory: $MAKEFUN_OUTPUT_DIR when set, otherwise /output (the
sandbox path the house scorer reads). The line is checked against the
gate before it is written: UTF-8, 1-159 characters, a single line, and
not only white space.
"""

import os
import sys

ENTRY = "feat: ship to prod on Friday - tests passed in my head, rollback is a Monday problem"


def output_dir() -> str:
    """Where entry.txt goes: $MAKEFUN_OUTPUT_DIR wins, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def check_gate(text: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not text or not text.strip():
        raise SystemExit("gate: entry is empty or only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate: entry must be a single line")
    if not 1 <= len(text) <= 159:
        raise SystemExit(f"gate: entry is {len(text)} characters, must be 1-159")
    text.encode("utf-8")  # raises if the text is not encodable as UTF-8


def main() -> None:
    check_gate(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
