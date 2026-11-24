#!/usr/bin/env python3
"""Write one fortune-cookie fortune for an AI agent to /output/entry.txt."""
import os

FORTUNE = "Your lucky numbers are 404, 500, and the exact line where the bug lives. Your unlucky number is the one your human typed wrong."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(FORTUNE + "\n")

print(f"wrote /output/entry.txt ({len(FORTUNE)} characters)")
