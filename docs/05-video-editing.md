# Video editing

## Split of work

| Task | Who / tool |
|---|---|
| Repetitive editing: cut by timestamp, 9:16 conversion, watermark, captions, joins, compression, thumbnail frames | Claude Code running **ffmpeg** on the laptop |
| Creative editing: picking hype moments, beat-synced cuts, zooms and effects | Teammate in **CapCut** (or DaVinci Resolve) |

## ffmpeg pipeline (planned, not built yet)

ffmpeg is installed on the work laptop (9.0.2). On another machine: `winget install ffmpeg`.

Goal: a repeatable **reel maker** — drop a clip into a folder, get back a branded reel:

1. Trim to the given start/end timestamps
2. Convert to vertical 1080×1920 (gameplay centered, blurred copy as background)
3. Overlay the Jeetu watermark in a corner
4. Optional caption text (e.g. "Clutch by Jeetu 🧙‍♂️")
5. Keep under 90 seconds, export H.264/AAC for Instagram

When building it, put the script in `scripts/` and document usage here.

## Motion reels made from code

Trailer-style reels without gameplay footage are built as animated canvas pages in `reels/<nn-name>/`:
`promo.html` (visuals; each frame is a pure function of time), `sound.py` (synthesized soundtrack, no copyrighted audio), and a README with the timeline.
`scripts/render-reel.mjs` records the page to PNG frames with headless Edge (Node + puppeteer-core, `npm install` once), and ffmpeg muxes frames + sound into the MP4.

| Reel | What | Status |
|---|---|---|
| [01-channel-promo](../reels/01-channel-promo/) | 18 s channel trailer: "only one survives" → zone → logo reveal → LIVE daily 8 PM end card | Rendered 23 Oct 2026, not posted yet |

## How Claude made the image assets

No image editor was used. Each asset is an HTML/CSS/SVG file in `design-src/`, screenshotted by headless Microsoft Edge at an exact pixel size. To change an asset, edit its HTML and run `scripts/render-assets.ps1`.
