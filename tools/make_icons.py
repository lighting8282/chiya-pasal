"""Draw the Chiya Pasal app icons (a cup of chiya on the stall's crimson).

Run from the repo root:  python tools/make_icons.py
Writes icons/icon-192.png, icons/icon-512.png and icons/apple-touch-icon.png.
The art stays inside the middle 60% so Android's round/squircle masks never clip it.
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw

S = 1024  # draw large, then scale down for smooth edges
CRIMSON = (196, 18, 47)
WHITE = (255, 255, 255)
TEA = (200, 141, 88)
STEAM = (255, 214, 222)


def draw() -> Image.Image:
    im = Image.new("RGB", (S, S), CRIMSON)
    d = ImageDraw.Draw(im)
    w = 34  # outline width
    # saucer
    d.ellipse((262, 668, 762, 748), fill=WHITE)
    # cup body: a rounded bowl
    d.rounded_rectangle((300, 400, 680, 690), radius=150, fill=WHITE)
    d.rectangle((300, 400, 680, 540), fill=WHITE)
    # tea surface
    d.ellipse((300, 368, 680, 432), fill=WHITE)
    d.ellipse((330, 380, 650, 424), fill=TEA)
    # handle
    d.ellipse((620, 450, 770, 600), outline=WHITE, width=w + 8)
    # steam: three soft S-curves rising from the cup
    for x0 in (410, 490, 570):
        pts = [(x0 + 22 * math.sin((y - 340) / 32), y) for y in range(340, 205, -4)]
        d.line(pts, fill=STEAM, width=w, joint="curve")
        for px, py in (pts[0], pts[-1]):
            d.ellipse((px - w / 2, py - w / 2, px + w / 2, py + w / 2), fill=STEAM)
    return im


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "icons"
    out.mkdir(exist_ok=True)
    art = draw()
    for name, px in (("icon-512.png", 512), ("icon-192.png", 192), ("apple-touch-icon.png", 180)):
        art.resize((px, px), Image.LANCZOS).save(out / name, optimize=True)
        print("wrote", out / name)


if __name__ == "__main__":
    main()
