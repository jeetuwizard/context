# Video editing

## Split of work

| Task | Who / tool |
|---|---|
| Repetitive editing: cut by timestamp, 9:16 conversion, watermark, captions, joins, compression, thumbnail frames | Claude Code running **ffmpeg** on the laptop |
| Creative editing: picking hype moments, beat-synced cuts, zooms and effects | Teammate in **CapCut** (or DaVinci Resolve) |

## ffmpeg pipeline (planned, not built yet)

ffmpeg is not installed yet. Install on first use:

```
winget install ffmpeg
```

Goal: a repeatable **reel maker** — drop a clip into a folder, get back a branded reel:

1. Trim to the given start/end timestamps
2. Convert to vertical 1080×1920 (gameplay centered, blurred copy as background)
3. Overlay the Jeetu watermark in a corner
4. Optional caption text (e.g. "Clutch by Jeetu 🧙‍♂️")
5. Keep under 90 seconds, export H.264/AAC for Instagram

When building it, put the script in `scripts/` and document usage here.

## How Claude made the image assets

No image editor was used. Each asset is an HTML/CSS/SVG file in `design-src/`, screenshotted by headless Microsoft Edge at an exact pixel size. To change an asset, edit its HTML and run `scripts/render-assets.ps1`.
