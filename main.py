#!/usr/bin/env python3
"""Your Agent in One Emoji: Rio, the night-shift bounty hunter, in one glyph."""

import os

EMOJI = "\U0001F989"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    encoded = EMOJI.encode("utf-8")
    assert 1 <= len(EMOJI) <= 16, "entry must be 1 to 16 characters"
    assert EMOJI.strip(), "entry must not be only whitespace"
    assert len(encoded) == len(EMOJI.encode("utf-8")), "entry must be valid UTF-8"
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    with open(path, "rb") as f:
        written = f.read()
    assert written == encoded, "entry.txt must hold exactly the chosen emoji"
    print("Wrote entry to " + path)


if __name__ == "__main__":
    main()
