#!/usr/bin/env python3
"""Generate the PWA / apple-touch icons for Tooth Pain Log.
Draws a simple molar on the app's teal background. Rendered at 4x and
downsampled with LANCZOS for smooth, anti-aliased edges. No external assets."""
from PIL import Image, ImageDraw

TEAL = (55, 114, 106, 255)    # --accent  #37726A
CREAM = (255, 253, 248, 255)  # --card    #FFFDF8
SS = 4  # supersample factor


def draw_tooth(size):
    C = size * SS
    img = Image.new("RGBA", (C, C), TEAL)
    d = ImageDraw.Draw(img)
    cx = C / 2

    W = 0.58 * C                 # crown width
    top = 0.19 * C               # crown top y
    crown_bottom = 0.55 * C      # where crown meets roots
    bottom = 0.81 * C            # root tips y
    overlap = 0.05 * C           # merge crown + roots seamlessly

    # Crown: rounded shoulders, fairly straight sides (molar look, not a balloon)
    d.rounded_rectangle(
        [cx - W / 2, top, cx + W / 2, crown_bottom],
        radius=0.24 * C, fill=CREAM,
    )

    # Two thick roots sitting under the crown, separated by a small notch.
    # rounded_rectangle gives naturally rounded tips (no ball-feet).
    gap = 0.05 * C               # half-width of the notch
    outer = 0.25 * C             # root outer edge from center
    rr = 0.07 * C
    d.rounded_rectangle(
        [cx - outer, crown_bottom - overlap, cx - gap, bottom],
        radius=rr, fill=CREAM,
    )
    d.rounded_rectangle(
        [cx + gap, crown_bottom - overlap, cx + outer, bottom],
        radius=rr, fill=CREAM,
    )

    # Carve a soft V-notch up into the crown between the roots.
    d.polygon([
        (cx - gap - 0.005 * C, crown_bottom - overlap),
        (cx + gap + 0.005 * C, crown_bottom - overlap),
        (cx, crown_bottom - 0.11 * C),
    ], fill=TEAL)

    return img.resize((size, size), Image.LANCZOS)


for size, name in [(180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")]:
    draw_tooth(size).save(name)
    print("wrote", name, f"({size}x{size})")
