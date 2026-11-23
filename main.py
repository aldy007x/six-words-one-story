#!/usr/bin/env python3
"""Six Words, One Story -- make.fun bounty entry.

Writes the six-word story to /output/entry.txt, exactly as the
bounty requires: one complete story in exactly six words.
"""

import os

STORY = "He finally arrived home. Nobody remembered."

# The gate requires 1-60 characters; the brief requires exactly six words.
assert len(STORY.split()) == 6, "story must be exactly six words"
assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
