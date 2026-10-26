"""Extract the clean MRI image embedded in case.pdf and crop panels C-D.

Usage:
    python crop_figure.py case.pdf items/images/neurocysticercosis_02_fig.png

Requires poppler-utils (pdfimages) and Pillow.
The embedded Fig. 1 image on page 2 has no asterisks or panel labels
(those are separate overlay objects in the PDF), so cropping the bottom
row gives a clean two-panel figure (T2 axial, T1 sagittal).
"""
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image


def main(pdf: str, out: str) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        prefix = Path(tmp) / "im"
        subprocess.run(
            ["pdfimages", "-png", "-f", "2", "-l", "2", pdf, str(prefix)],
            check=True,
        )
        # The largest image on page 2 with size 953 x 803 is Fig. 1 (four MRI panels).
        candidates = [Image.open(p) for p in sorted(Path(tmp).glob("im-*.png"))]
        fig1 = next(im for im in candidates if im.size == (953, 803))
        # Bottom row (panels C and D) starts below the dark divider at y = 400.
        crop = fig1.convert("RGB").crop((0, 401, 953, 803))
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        crop.save(out)
        print(f"Saved {out} ({crop.size[0]} x {crop.size[1]} px)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
