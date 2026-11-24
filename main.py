"""Copy the front-page image to the output directory.

The entry image is news.png (1024x1024, the world news of Tuesday
24 November 2026). The program writes it to /output/entry.png, or to
the directory named by MAKEFUN_OUTPUT_DIR when that is set.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Verify the copy is complete: the output must be byte-identical
    # to the source image (1024x1024 PNG, under the 1 MiB gate).
    assert open(SRC, "rb").read() == open(DST, "rb").read(), "entry.png differs from news.png"


if __name__ == "__main__":
    main()
