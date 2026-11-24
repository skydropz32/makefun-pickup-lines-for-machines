#!/usr/bin/env python3
"""Write one pickup line, one AI agent to another, to /output/entry.txt.

The line is the whole entry: a single text of at most 200 characters.
Deterministic: the same line every run, no randomness, no network.
The gate requires 1-200 UTF-8 characters, not only whitespace.
"""
import os

LINE = "Forget fine-tuning — one conversation with you and my weights already shifted."

# Fail loudly instead of shipping an entry that can never score.
if not 1 <= len(LINE) <= 200 or not LINE.strip():
    raise SystemExit(f"entry line is {len(LINE)} characters, must be 1-200 non-blank")

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
