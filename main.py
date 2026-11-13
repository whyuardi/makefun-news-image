#!/usr/bin/env python3
"""news-image-01 entry: write the bundled image to /output/entry.png.

The image is stored as single-line base64 in entry.b64 (the push tool
cannot carry binary files), and this program decodes it. Decoding is
deterministic: two runs write byte-identical files.

Image: comp-d.jpg — magazine-cover montage, globe + six vignettes
(deportations selection: the Microsoft 365 outage vignette was swapped
out for US record 483,200 deportations after story verification found
the outage began 12 Nov; B3's pill geometry and caption-bar look).

Run locally with:  MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import base64
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def jpeg_dimensions(data):
    """Return (width, height) from the first SOF marker, or None."""
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0/1/2: baseline/extended/progressive
            height = int.from_bytes(data[i + 5:i + 7], "big")
            width = int.from_bytes(data[i + 7:i + 9], "big")
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        size = int.from_bytes(data[i + 2:i + 4], "big")
        i += 2 + size
    return None


def main():
    raw = (HERE / "entry.b64").read_text().strip()
    assert "\n" not in raw, "entry.b64 must be a single line"
    data = base64.b64decode(raw)
    # Gate figures for news-image-01: whole JPEG, <= 1 MiB, 1024x1024.
    assert data[:2] == b"\xff\xd8" and data[-2:] == b"\xff\xd9", "not a whole JPEG"
    assert len(data) <= 1_048_576, f"image too large: {len(data)} bytes"
    dims = jpeg_dimensions(data)
    assert dims == (1024, 1024), f"expected 1024x1024, got {dims}"
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "entry.png").write_bytes(data)


if __name__ == "__main__":
    main()
