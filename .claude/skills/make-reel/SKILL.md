---
name: make-reel
description: Turn a gameplay recording or clip into a branded vertical Instagram/YouTube Shorts reel with ffmpeg (trim, 9:16, blurred background, watermark, optional caption). Use when the user gives a video file or asks for a reel, short, clip, or highlight.
---

# Make a reel

## Setup (first time on a machine)

Check `ffmpeg -version`. If missing: `winget install ffmpeg`, then open a new shell so it's on PATH.

## Inputs to get from the user

- Source video path (or a file in the Google Drive mirror, see `docs/08-storage.md`)
- Start and end timestamps (reels: 15–30 s ideal, under 90 s)
- Who made the play (for the caption credit) and optional caption text

## Recipe

Write outputs to `output/` in the repo root (git-ignored). Name: `YYYY-MM-DD_who_what.mp4`.

```bash
ffmpeg -ss START -to END -i "INPUT.mp4" -i assets/final/watermark_subscribe.png -filter_complex \
"[0:v]split[a][b];\
[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:5[bg];\
[b]scale=1080:-2[fg];\
[bg][fg]overlay=(W-w)/2:(H-h)/2[v1];\
[1:v]scale=150:-1[wm];\
[v1][wm]overlay=W-w-40:H-h-260[v]" \
-map "[v]" -map 0:a? -c:v libx264 -preset veryfast -crf 20 -c:a aac -b:a 160k -movflags +faststart "output/NAME.mp4"
```

- Gameplay sits full-width in the middle; a blurred, zoomed copy fills the top and bottom.
- The watermark sits bottom-right, above Instagram's caption area.
- For caption text, add a `drawtext` filter (font `C:/Windows/Fonts/impact.ttf`, white, orange `#F2A900` box or border), placed in the top blurred band.
- Slow motion on a moment: `setpts=2.0*PTS` on video and `atempo=0.5` on audio for that segment.

## Verify before handing over

- `ffprobe` the output: 1080×1920, has audio, duration as expected.
- Extract one frame (`ffmpeg -ss 2 -i out.mp4 -frames:v 1 output/check.png`) and look at it with the Read tool.

## Hand-off

Give the full output path, and remind the user to upload it to Drive `03 Reels Final`. Suggested caption: credit the player, e.g. "Clutch by @name 🧙‍♂️ — full stream on YouTube, link in bio", plus `#BGMI #JeetuWizard #WWCD`.

## Trailer / promo reels without footage

For an advertisement-style reel with no gameplay, follow the method in `reels/01-channel-promo/`: copy the folder to `reels/<nn-name>/`, change the timeline constants, scenes, and text in `promo.html` and the matching event times in `sound.py`, preview a few moments, then render (steps in that folder's README). Check a contact sheet of preview frames and the waveform before handing over.

When the pipeline is turned into a reusable script, save it in `scripts/` and update `docs/05-video-editing.md`.
