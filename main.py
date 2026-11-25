"""Write one toaster error message to /output/entry.txt.

The entry is a single line: a deadpan error message from a kitchen
toaster that found a fork in one of its slots and refuses to work
until the owner deals with it.
"""

import os

ENTRY = "ERROR E02: Fork detected in slot 2. I refuse to work under these conditions."
OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 120


def validate_entry(text):
    """Check the entry against the competition gate before writing."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("entry is over 120 characters")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not hold control characters")
    return True


def main():
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("read-back does not match the entry")
    if written.count("\n") != 0 or written.count("\r") != 0:
        raise ValueError("written file must hold exactly one line")
    print("wrote %d characters to %s" % (len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
