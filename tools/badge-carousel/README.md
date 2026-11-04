# Tools in orbit

Transparent looping technology badges for the profile README.

Requires Python 3.10+ and Pillow (`python3 -m pip install Pillow`).

```sh
python3 generate.py
```

Optional settings: `python3 generate.py --seconds 16 --fps 15`.

Outputs: `tools-orbit.gif`, `poster.png`, and an interactive `preview.html` (open in a browser). The preview supports pause/play and reduced motion. The GIF loops continuously. Copy the regenerated GIF to `../../assets/tools-orbit.gif`.

Each badge traverses a circular track, changing size and brightness with depth. Frames reserve a transparent palette entry and clear between frames to prevent trails. No network requests are required.
