# Tools in orbit

Transparent looping technology badges for the profile README.

The compact GIF is 800 × 272 pixels, with flattened orbits and closer track spacing (previously 800 × 496).

Requires Python 3.10+ and Pillow (`python3 -m pip install Pillow`).

```sh
python3 generate.py
```

The default export is 50 fps (20 ms per frame), with an unchanged 16-second orbit. GIF timing uses 10 ms increments, so steady 60 fps is not representable. The browser preview uses display-synced animation.

Optional settings: `python3 generate.py --seconds 16 --fps 50`.

Outputs: `tools-orbit.gif`, `poster.png`, and an interactive `preview.html` (open in a browser). The preview supports pause/play and reduced motion. The GIF loops continuously. Copy the regenerated GIF to `../../assets/tools-orbit.gif`.

Each badge traverses a circular track, changing size with depth. Frames reserve a transparent palette entry and clear between frames to prevent trails. Foreground badges keep their full color. Background badges fade smoothly to 62% brightness, with dedicated shades for every badge in the fixed palette to avoid hue flicker. The GIF background stays transparent. No network requests are required.
