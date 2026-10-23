# Storage: what goes where

Two homes, each for what it's good at.

| | GitHub repo (`jeetuwizard/context`, private) | Google Drive folder |
|---|---|---|
| Link | github.com/jeetuwizard/context | [Jeetu Wizard Drive](https://drive.google.com/drive/u/1/folders/1BM1HMgl6o5xHGDHBY0xgfZjO-TuD4z9a) |
| Holds | Context docs, decisions, checklists, texts, design sources, final brand PNGs, scripts, Claude skills | Videos and anything large: raw stream recordings, clips, finished reels, thumbnails, screenshots |
| Why | Small text files, full history, Claude reads it directly | Git is bad at big video files; Drive is easy to share with teammates and open on phones |
| Who edits | Claude (through Claude Code) and Jitender | Whole team uploads |

**Rule of thumb:** if it's a video or bigger than ~10 MB, it goes to Drive. Everything else goes in the repo. The repo's `.gitignore` blocks video files so they can't be committed by accident.

## Drive folder layout

Create these subfolders inside the Drive folder:

```
Jeetu Wizard (Drive)
├── 01 Raw Recordings      full stream recordings from OBS, named YYYY-MM-DD
├── 02 Clips               highlight moments cut from recordings (teammates drop clips here)
├── 03 Reels Final         finished vertical reels, ready to post
├── 04 Thumbnails          YouTube thumbnails
└── 05 Brand Assets        copy of assets/final/ for teammates without GitHub access
```

File naming: `YYYY-MM-DD_who_what.mp4`, e.g. `2026-10-25_jeetu_1v4-clutch.mp4`. Dates first keep folders sorted.

## How Claude works with Drive

Claude Code on the laptop has no Google Drive connection, so it cannot open or upload Drive files directly. The working loop is:

1. Download the clip from Drive to the laptop (or install Google Drive for Desktop, which mirrors the folder as a normal local folder — then Claude can read and write it directly; recommended).
2. Claude processes it into the repo's `output/` folder (ignored by git).
3. Upload the result to the right Drive subfolder.

If Google Drive for Desktop is installed, record the local path of the mirrored folder here: _not set up yet_
