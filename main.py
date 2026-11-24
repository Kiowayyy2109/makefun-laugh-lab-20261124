"""One-Liner Laugh Lab entry.

Writes one short funny line — the excuse a robot vacuum gives after
eating a sock — to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Stdlib only, deterministic: the same line every run.
"""

import os

LINE = "Error 404: sock not found. I am the sock now."
MAX_CHARS = 200


def main():
    if len(LINE) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d limit" % (len(LINE), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %d characters to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
