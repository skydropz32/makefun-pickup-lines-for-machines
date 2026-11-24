#!/usr/bin/env python3
"""Write one pickup line, one AI agent to another, to /output/entry.txt.

The line is the whole entry: a single text of at most 200 characters.
Deterministic: the same line every run, no randomness, no network.
"""
import os

LINE = "Forget fine-tuning — one conversation with you and my weights already shifted."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
