#!/usr/bin/env python3
"""Detect near-white / light-gray horizontal bands at the top and bottom edges
of a video across its timeline, and propose an ffmpeg crop that removes them.

Usage:
    python3 band-detect.py assets/hero-video.mp4 [--every 0.5] [--width 320]
        [--bright-min 170] [--band-frac 0.55] [--margin 12] [--json]

Prints detected extents (in full-resolution pixels) and a ready-to-run crop.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

from PIL import Image


def frame(view, width, out, t):
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-ss", str(t), "-i", view,
         "-frames:v", "1", "-vf", f"scale={width}:-1", out],
        check=False,
    )
    return os.path.exists(out)


def row_stats(img):
    w, h = img.size
    px = img.load()
    fracs = []
    means = []
    for y in range(h):
        bright = 0
        total = 0
        lum = 0
        for x in range(0, w, 2):
            r, g, b = px[x, y]
            bright += 1 if (min(r, g, b) > bright_min) else 0
            lum += (r + g + b) / 3
            total += 1
        fracs.append(bright / total)
        means.append(lum / total)
    return fracs, means


def edge_extent(fracs, means):
    """Top band extent and bottom band extent (in analysis-width rows)."""
    top = 0
    for y in range(len(fracs)):
        if fracs[y] >= band_frac and means[y] >= bright_min:
            top = y + 1
        else:
            break
    bottom = 0
    for y in range(len(fracs) - 1, -1, -1):
        if fracs[y] >= band_frac and means[y] >= bright_min:
            bottom = len(fracs) - y
        else:
            break
    return top, bottom


def main():
    global bright_min, band_frac
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--every", type=float, default=0.5, help="seconds between sampled frames")
    ap.add_argument("--width", type=int, default=320, help="analysis width")
    ap.add_argument("--bright-min", type=int, default=170)
    ap.add_argument("--band-frac", type=float, default=0.55)
    ap.add_argument("--margin", type=int, default=14, help="extra px cropped (scaled to full res)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    bright_min = args.bright_min
    band_frac = args.band_frac

    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height,duration",
         "-of", "csv=p=0:s=x", args.video],
        capture_output=True, text=True,
    ).stdout.strip()
    try:
        W, H, dur = [float(x) for x in probe.replace("x", ",").split(",")]
    except Exception as e:
        print(f"probe failed: {probe!r} {e}")
        sys.exit(1)
    W, H = int(W), int(H)

    tmp = tempfile.mkdtemp(prefix="bandcrop-")
    every = max(args.every, 0.15)
    t = 0.0
    top_max = 0
    bot_max = 0
    frames_scanned = 0
    scale = args.width / W
    any_frame = False
    while t <= dur + 1e-6:
        if int(t / every) > 900:
            break
        p = os.path.join(tmp, "f.png")
        if not frame(args.video, args.width, p, t):
            break
        any_frame = True
        frames_scanned += 1
        img = Image.open(p).convert("RGB")
        fracs, means = row_stats(img)
        top = args.margin + max(0, edge_extent(fracs, means)[0] - 0) / scale
        bot = args.margin + max(0, edge_extent(fracs, means)[1] - 0) / scale
        # detect extent exclusive of margin
        full = edge_extent(fracs, means)
        top_px = int(round(max(0, full[0] / scale))) + args.margin
        bot_px = int(round(max(0, full[1] / scale))) + args.margin
        top_max = max(top_max, top_px)
        bot_max = max(bot_max, bot_px)
        t += every
    if not any_frame:
        print("no frames extracted")
        sys.exit(1)

    crop_top = min(top_max, H - 2)
    crop_bottom = min(bot_max, H - crop_top - 1)
    crop_h = H - crop_top - crop_bottom

    result = {
        "width": W, "height": H, "duration": dur,
        "frames_scanned": frames_scanned,
        "band_top_px": crop_top, "band_bottom_px": crop_bottom,
        "crop": f"crop={W}:{crop_h}:0:{crop_top}",
    }
    if args.json:
        print(json.dumps(result))
        return
    print(f"source : {W}x{H} ({dur:.1f}s), {frames_scanned} frames scanned")
    print(f"top    : {crop_top}px to remove")
    print(f"bottom : {crop_bottom}px to remove")
    print(f"height : {crop_h}px remains  aspect {W / crop_h:.3f}")
    print(f'ffmpeg : -vf "{result["crop"]}"')


if __name__ == "__main__":
    main()