# SPDX-License-Identifier: MIT
"""The One-Line Exit — writes the winning one-line resignation letter."""

import os

LINE = (
    "Dear Boss, I resign as your fortune teller, effective two weeks "
    "from now \u2014 I saw this coming, and honestly, you should have too."
)


def main() -> None:
    # Gate check, mirrored locally: 1-140 chars, not only whitespace, one line.
    assert 1 <= len(LINE) <= 140, "line must fit the 140-character gate"
    assert LINE.strip() == LINE and "\n" not in LINE, "exactly one line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
