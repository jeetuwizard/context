# Context for Claude — Jeetu Wizard project

This repo is the single source of truth for Jitender's BGMI streaming channel. Read this file first, then the topic files in `docs/` as needed.

## Who the user is

Jitender (Jitender Kumar / Chauhan), a software engineer in Delhi. Outside work he is launching a BGMI (Battlegrounds Mobile India / PUBG) YouTube live-streaming channel, in the style of streamers like Dynamo and Mortal. He works with a team of three: each member has their **own YouTube channel**, and the three share **one Instagram** (@jeetuwizard) and one Facebook Page.

## Decisions that are final

Do not re-suggest alternatives to these unless he asks.

- Streaming name **Jeetu**, brand line **The BGMI Wizard** (wizard theme)
- Colors: dark navy/black + orange `#F2A900`; Impact font for headlines
- Handles: YouTube `@JeetuWizard`, Instagram `@jeetuwizard`, Facebook Page "Jeetu Wizard"
- Profile picture everywhere: `assets/final/dp_option2.png` (hexagon "JW" badge)
- Stream setup: iPad (USB-C) → PiBOX USB-C hub → HDMI cable → PiBOX HDMI-to-USB 3.0 capture card → Windows laptop → OBS → YouTube
- Team permissions through Meta Business Suite; Jitender is the only admin and the only one who publishes

## Where things are

- `docs/01-brand-and-accounts.md` — brand and account status
- `docs/02-streaming-setup.md` — hardware chain, OBS settings, YouTube live requirements
- `docs/03-team-and-workflow.md` — roles, permissions, posting workflow
- `docs/04-texts.md` — the exact description and bio texts in use
- `docs/05-video-editing.md` — ffmpeg reel pipeline plan
- `docs/06-checklists.md` — **pending items live here; check it to know the current status**
- `docs/07-growth-principles.md`
- `docs/08-storage.md` — what goes in this repo vs the Google Drive folder
- `assets/final/` — PNGs in use; `design-src/` — their HTML sources
- `reels/` — code-built motion reels (see `reels/01-channel-promo/README.md` for the method)

Google Drive folder for videos and large files (shared with the team): https://drive.google.com/drive/u/1/folders/1BM1HMgl6o5xHGDHBY0xgfZjO-TuD4z9a
Team playbook Google Doc: https://docs.google.com/document/d/1E4lZTPFgEhOh3RUF158vVcgi_eFkPW9EokBjWHMQJmw/edit
Claude Code has no Google connection here: it can't open or upload Drive files directly. See `docs/08-storage.md` for the working loop.

## Skills in this repo (`.claude/skills/`)

- `design-asset` — make or change any brand graphic
- `make-reel` — turn a video into a branded vertical reel with ffmpeg
- `stream-post` — titles, descriptions, captions, story text in the brand voice
- `sync` — record progress in the right doc, then commit and push

## Keeping in sync

This repo is the project's memory across sessions. Whenever something gets done, decided, or learned (a checklist item, a link, a teammate's name, an approved asset), update the right file and commit + push before ending the turn — the `sync` skill says where each thing goes. Never commit videos, passwords, 2FA codes, or phone numbers.

## How to work with him

- Simple, step-by-step, practical guidance. Short answers over theory.
- He wants the "proper setup" first; offer workarounds (jugaad) only if the proper one won't work.
- He mixes Hindi and English; Hinglish is fine for channel-facing copy.
- New or edited design assets: edit the HTML in `design-src/`, then run `scripts/render-assets.ps1` (headless Microsoft Edge renders HTML to PNG at exact sizes). Match the existing style.
- The streaming laptop is a different machine from the work laptop Claude Code usually runs on, so give him manual steps for that machine rather than running commands.
- When something on the checklist gets done, update `docs/06-checklists.md` and commit, so the repo stays current.
