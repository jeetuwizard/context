# Reel 01 — Channel promo (trailer)

An 18-second vertical trailer for the channel: 1080×1920, 30 fps, made entirely in code. It uses no gameplay footage and no copyrighted audio.

The finished MP4 is not in git (videos go to Drive): upload `2026-10-23_jeetu_channel-promo.mp4` to Drive → `03 Reels Final`.

## Timeline

| Time | Scene | Sound |
|---|---|---|
| 0–3.8 s | "100 PLAYERS" → "ONE MAP" → glitching "ONLY ONE SURVIVES" | Heartbeat, whooshes, glitch clicks |
| 3.8–6.6 s | Rotating scope; stamps "RUSH." "SNIPE." "CLUTCH." "1 v 4."; kill feed slides in | Gunshot impact on each stamp |
| 6.6–9.6 s | Zone ring shrinks over a grid, countdown 3-2-1, "NO PLACE TO HIDE" | Ticks, rising riser |
| 9.6–10.1 s | Black, "ONE NAME." | Silence, one heartbeat |
| 10.1–14.2 s | Flash, shockwave, logo slams in over light rays and embers, JEETU, THE BGMI WIZARD, "WINNER WINNER CHICKEN DINNER" typed | Big bass drop, impacts, typing ticks |
| 14.2–18 s | End card: LIVE DAILY • 8 PM, @JeetuWizard, SUBSCRIBE, Instagram handle; fade out | Pops, drone fades |

Every timing lives in constants at the top of `promo.html` and `sound.py`. They must match: change a time in one file, change it in the other.

## Rebuild

From the repo root (first time: `npm install`):

```bash
mkdir -p output/promo
python -I reels/01-channel-promo/sound.py output/promo/sound.wav
node scripts/render-reel.mjs reels/01-channel-promo/promo.html output/promo/frames 30
ffmpeg -y -framerate 30 -i output/promo/frames/frame_%05d.png -i output/promo/sound.wav \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart \
  output/promo/2026-10-23_jeetu_channel-promo.mp4
```

Frame recording takes about 3 minutes. To check a few moments first, pass preview times:
`node scripts/render-reel.mjs reels/01-channel-promo/promo.html output/check 30 1,4.5,12`

Live preview: open `promo.html` in a browser (it loops in real time).

## Posting tips

- Cover image: `cover.jpg` (frame at 13.9 s).
- On Instagram you can swap the synthesized track for a trending audio. Trending sounds get more reach, but the hits will no longer line up with the visuals, so keep the original sound for the first post.
- Suggested caption: "100 players. One map. Only one survives. 🧙‍♂️ LIVE daily 8 PM on YouTube — link in bio 🔴 #BGMI #BGMILive #JeetuWizard #WWCD"
