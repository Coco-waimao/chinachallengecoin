"""Pillow image processor: convert all images to 600x400 (1.5:1) banner format.

Strategy:
- For each image, keep aspect ratio and fit inside 600x400 centered.
- Fill the remaining padding with the average color sampled from the image's
  top/bottom/left/right edge pixels, so the result looks like a natural
  extension of the photo background.
- Save as high-quality progressive JPEG (quality 88, optimize).

Note: The padding is solid (edge color) rather than blurred. This keeps the
file small and renders cleanly at any size. Since most source photos have a
clean studio background, the seam is invisible in practice.
"""

import os
import glob
from PIL import Image

TARGET_W, TARGET_H = 600, 400


def edge_color(im):
    """Return average RGB color from the four edges of the image."""
    w, h = im.size
    edge_pixels = []
    # top and bottom rows
    for x in range(0, w, max(1, w // 20)):
        edge_pixels.append(im.getpixel((x, 0))[:3])
        edge_pixels.append(im.getpixel((x, h - 1))[:3])
    # left and right columns
    for y in range(0, h, max(1, h // 20)):
        edge_pixels.append(im.getpixel((0, y))[:3])
        edge_pixels.append(im.getpixel((w - 1, y))[:3])
    r = sum(p[0] for p in edge_pixels) // len(edge_pixels)
    g = sum(p[1] for p in edge_pixels) // len(edge_pixels)
    b = sum(p[2] for p in edge_pixels) // len(edge_pixels)
    return (r, g, b)


def to_banner(src, dst, size=(TARGET_W, TARGET_H), quality=88):
    im = Image.open(src).convert("RGB")
    bg = edge_color(im)

    # Resize source to fit inside target while preserving aspect ratio
    src_w, src_h = im.size
    ratio = min(size[0] / src_w, size[1] / src_h)
    new_w = int(src_w * ratio)
    new_h = int(src_h * ratio)
    fitted = im.resize((new_w, new_h), Image.LANCZOS)

    # Place fitted on a target-sized canvas with edge-color background
    canvas = Image.new("RGB", size, bg)
    off_x = (size[0] - new_w) // 2
    off_y = (size[1] - new_h) // 2
    canvas.paste(fitted, (off_x, off_y))

    canvas.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
    return os.path.getsize(dst)


def process_file(src, dst, size=(TARGET_W, TARGET_H), quality=88):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.abspath(src) == os.path.abspath(dst):
        # In-place: write to temp then replace
        tmp = dst + ".tmp.jpg"
        to_banner(src, tmp, size, quality)
        os.replace(tmp, dst)
    else:
        to_banner(src, dst, size, quality)


if __name__ == "__main__":
    pass
