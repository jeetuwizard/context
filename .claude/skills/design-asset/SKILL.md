---
name: design-asset
description: Create or change a Jeetu Wizard brand image (banner, profile picture, watermark, thumbnail, Facebook cover, milestone post, overlay). Use whenever the user asks for a new graphic or a change to an existing one.
---

# Design a brand asset

All images are HTML/CSS/SVG files in `design-src/`, rendered to PNG by headless Microsoft Edge. No image editor is involved.

## Style rules (match the existing assets)

- Background: dark navy/black (`#0b0e13`, `#10141c`, `#1c2230`) with subtle radial glows
- Accent: orange `#F2A900`, secondary `#FF5E00`, darker shade for 3D text shadow `#C47800`
- Headlines: `Impact, 'Arial Black', sans-serif`, uppercase, white with orange glow + offset shadow
- Small labels: `'Segoe UI'`, bold, wide letter-spacing, orange
- Motifs: wizard hat (SVG path in `design-src/watermark.html`), crosshairs, diagonal orange stripes, "WWCD"
- "JEE" white + "TU" orange is the name treatment on the banner

## Sizes

| Asset | Pixels | Notes |
|---|---|---|
| YouTube banner | 2560×1440 | Text must stay inside the centered 1546×423 safe area |
| Profile picture | 800×800 | Shown as a tiny circle; keep it bold and simple |
| YouTube watermark | 150×150 | Transparent background |
| YouTube thumbnail | 1280×720 | |
| Facebook cover | 1640×624 (shows ~820×312 on desktop) | Keep important content centered |
| Instagram post | 1080×1080; reel cover 1080×1920 | |

## Steps

1. Copy the closest existing file in `design-src/` as a starting point, or edit it in place for a change.
2. For a new asset, add a line for it to the `$jobs` list in `scripts/render-assets.ps1` (output path, size, transparent or not).
3. Render: `powershell -ExecutionPolicy Bypass -File scripts\render-assets.ps1`
4. Open the PNG with the Read tool and look at it before showing the user. Fix overlaps, clipping, or text outside safe areas.
5. Tell the user the full path of the PNG and where to upload it.
6. Once the user approves, commit and push (see the `sync` skill). Rejected options go to `assets/alternates/`.
