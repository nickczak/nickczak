#!/usr/bin/env python3
"""Generate an offline browser animation and a seamless README GIF.

Install Pillow, then run: python3 generate.py
Outputs are written alongside this script. No network requests are needed.
"""
import argparse
import json
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

TOOLS = [
    ('C++', '#00599C'), ('Java', '#ED8B00'), ('Python', '#3776AB'),
    ('SQL', '#336791'), ('TypeScript', '#3178C6'), ('JavaScript', '#B59B00'),
    ('Spring Boot', '#50852C'), ('PostgreSQL', '#4169E1'), ('SQLite', '#00758F'),
    ('DynamoDB', '#4053D6'), ('Angular', '#DD0031'), ('React', '#087E9B'),
    ('AWS Lambda', '#BD6900'), ('API Gateway', '#B76A00'), ('Cognito', '#DD344C'),
    ('AWS SAM', '#BD6900'), ('Docker', '#2496ED'), ('GitHub Actions', '#2088FF'),
    ('Linux', '#7D6900'), ('Git', '#F05032'), ('CMake', '#064F8C'),
    ('Valgrind', '#6B3FA0'), ('Catch2', '#43802A'), ('pytest', '#0A9EDC'),
    ('JUnit', '#25A162'),
]
ROOT = Path(__file__).resolve().parent
W, H = 1000, 340


def position(index, angle):
    # Three circular tracks; each badge traverses the full front/back orbit.
    track = index % 3
    row = index // 3
    count = len(TOOLS[track::3])
    theta = angle + row * math.tau / count + track * .38
    depth = math.sin(theta)
    scale = .67 + .32 * (depth + 1) / 2
    return W / 2 + 370 * math.cos(theta), H / 2 + (track - 1) * 75 + 40 * depth, depth, scale


def font(size):
    try:
        return ImageFont.truetype('DejaVuSans.ttf', size)
    except OSError:
        return ImageFont.load_default(size=size)


def render(angle):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    items = [(position(i, angle), name, color) for i, (name, color) in enumerate(TOOLS)]
    for (x, y, depth, scale), name, color in sorted(items, key=lambda item: item[0][2]):
        f = font(round(20 * scale))
        width = d.textlength(name, font=f) + 44 * scale
        height = 44 * scale
        rgb = tuple(int(color[j:j + 2], 16) for j in (1, 3, 5))
        fg = (255, 255, 255)
        box = (x - width / 2, y - height / 2, x + width / 2, y + height / 2)
        d.rounded_rectangle(box, radius=round(7 * scale), fill=rgb)
        d.text((x, y), name, font=f, fill=fg, anchor='mm')
    return im


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds', type=float, default=16)
    parser.add_argument('--fps', type=int, default=50)
    args = parser.parse_args()
    if args.seconds <= 0 or not 1 <= args.fps <= 50:
        parser.error('seconds must be positive; fps must be between 1 and 50')
    html = (ROOT / 'template.html').read_text()
    (ROOT / 'preview.html').write_text(html.replace('__TOOLS__', json.dumps(TOOLS)).replace('__SECONDS__', str(args.seconds)))
    count = max(2, round(args.seconds * args.fps))
    # Reserve index 255 for fully transparent pixels. Restore the background
    # after each frame so moving badges do not leave trails.
    # Include every exact badge color, rather than sampling a single frame.
    # A fixed palette and fixed fills prevent shade changes during the orbit.
    colors = [tuple(int(color[j:j + 2], 16) for j in (1, 3, 5)) for _, color in TOOLS]
    colors += [(255, 255, 255)] + [(v, v, v) for v in range(0, 256, 8)]
    palette = Image.new('P', (1, 1))
    entries = [channel for color in colors for channel in color]
    palette.putpalette(entries + [0] * (768 - len(entries)))
    indexed = []
    for i in range(count):
        frame = render(math.tau * i / count).resize((800, 272), Image.Resampling.NEAREST)
        quantized = frame.convert('RGB').quantize(palette=palette, dither=Image.Dither.NONE)
        mask = frame.getchannel('A').point(lambda alpha: 255 if alpha == 0 else 0)
        quantized.paste(255, mask=mask)
        quantized.info['transparency'] = 255
        indexed.append(quantized)
    indexed[0].save(ROOT / 'tools-orbit.gif', save_all=True, append_images=indexed[1:],
                    duration=round(100 / args.fps) * 10, loop=0, optimize=False,
                    transparency=255, background=255, disposal=2)
    render(.8).save(ROOT / 'poster.png')
    print(f'Created preview.html, tools-orbit.gif ({count} frames), and poster.png')


if __name__ == '__main__':
    main()
