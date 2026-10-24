# Streaming setup

## Hardware chain (final)

```
iPad (USB-C)
  └─ PiBOX India USB-C Hub 3-in-1 HDMI Adapter   (Amazon B07SVVR598)
       ├─ charger into the hub's PD port (iPad charges while streaming)
       └─ HDMI male-to-male cable                  (already owned)
            └─ PiBOX India 4K HDMI to USB 3.0 Capture Card   (Amazon B0973PR9HH)
                 └─ Windows laptop USB 3.0 port → OBS Studio → YouTube
```

The capture card shows up in Windows as a webcam. No drivers are needed. Game audio travels through the HDMI cable together with the video.

### Why this setup

- **Capture card over AirPlay:** a cable never fluctuates. AirPlay goes through the WiFi router, so a WiFi hiccup freezes or drops the stream mid-match.
- **iPad vs Android phone:** iPads with USB-C output HDMI video; most Android phones cannot (no DisplayPort Alt Mode). That's why the Android plan used scrcpy (free USB screen mirroring, Android-only) and the iPad plan uses a capture card.
- The game runs on the iPad, and Jitender plays looking at the iPad, so any delay in the laptop preview never affects gameplay.

## Without hardware (free)

Until the capture card arrives, two free options. **Recommended: direct from the iPad**, since the video goes straight to YouTube with no extra WiFi hop.

### Option A: stream directly from the iPad

1. YouTube Studio → Create → Go Live → **Stream** tab → copy the Stream URL and Stream key (keep the key private). Streaming with a key has no subscriber minimum.
2. Install **PRISM Live Studio** (free, no watermark) on the iPad; Streamlabs works the same way.
3. PRISM → Settings → Destinations → **Custom RTMP** → paste URL + key. Quality: 720p, 30 fps, ~2500–3000 kbps. Mode: **Screen**.
4. Control Center → long-press **Screen Recording** → pick PRISM → **Microphone ON** → Start Broadcast → open BGMI.
5. Stop: tap the red indicator at the top → Stop.

Game audio and mic both go out; use earphones with a mic. Set BGMI graphics to **Smooth** (not HDR) since the iPad runs the game and the encode together.

### Option B: AirPlay to the laptop, then OBS

Use when OBS features are wanted (overlays, logo, webcam).

1. Laptop: install **5KPlayer** (free), turn on its AirPlay service, allow it through Windows Firewall.
2. iPad and laptop on the same WiFi (5 GHz preferred).
3. iPad: Control Center → Screen Mirroring → pick the laptop.
4. OBS: Sources → + → Window Capture → the 5KPlayer mirror window (Capture Method "Windows 10 (1903 and up)" if it shows black).

Working on the work laptop as of 24 Oct 2026. Gotchas hit during setup:
- **AirPlay switches greyed out in 5KPlayer = Apple Bonjour missing.** 5KPlayer didn't install it. Fix: install "Bonjour Print Services for Windows" (`BonjourPSSetup.exe`) from support.apple.com/en-us/106380, then reopen 5KPlayer.
- The mirror window only exists while the iPad is actively mirroring, so it won't appear in OBS's Window Capture list until then. Don't minimize it (captures black).
- Installer check: 5KPlayer `5kplayer-64bit.exe` v6.11 is signed by Digiarty Software, Inc. (DigiCert); download only from 5kplayer.com and skip the VideoProc promotion.

## OBS configuration

| Setting | Value |
|---|---|
| Video source | Video Capture Device → PiBOX card, 1920×1080, 30 fps |
| Game audio | On the capture source: Audio Output Mode → capture/output desktop audio |
| Mic | Separate **Audio Input Capture** source; headset or USB mic, not the laptop's built-in mic |
| Stream | Settings → Stream → Service: YouTube → Connect account |
| Bitrate, upload ≥ 5 Mbps | 4500 kbps, 1920×1080, 30 fps |
| Bitrate, upload 3–5 Mbps | 2500–3000 kbps, 1280×720, 30 fps |
| Network | Laptop on a LAN cable to the router |

Measured 24 Oct 2026 on the work laptop over WiFi "wizard 5g": **upload ~85–110 Mbps, download ~128 Mbps**. Bandwidth is not a constraint.

Laptop in use: AMD Ryzen 5 7535HS, Radeon 660M, 27 GB RAM → encoder **AMD HW H.264 (AVC)** (hardware, keeps the CPU free).

Recommended OBS output for this setup: 1920×1080, 30 fps, AMD HW H.264, CBR **6000 kbps**, keyframe interval 2 s.

## YouTube live requirements

- Verify the channel with a phone number at youtube.com/verify. Live streaming activates about **24 hours** later.
- Streaming from a computer (OBS) has **no subscriber minimum**. The 50-subscriber rule only applies to going live from the YouTube mobile app.
- Go Live button: youtube.com → **Create** (camera icon, top right) → Go Live, or directly at youtube.com/live_dashboard.
- **The first stream is always Unlisted** — check video, game audio, mic level, and buffering before going public.

## Shopping list beyond the chain (optional, in order of value)

1. USB or lapel mic — viewers forgive video quality, not bad audio
2. LAN cable router → laptop
3. Later: webcam + ring light for a facecam
