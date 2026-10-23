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

## Temporary test method: AirPlay (free)

Use only for practice streams before the capture card arrives.

1. Laptop: install **5KPlayer** (free), turn on its AirPlay service, allow it through Windows Firewall.
2. iPad and laptop on the same WiFi (5 GHz preferred).
3. iPad: Control Center → Screen Mirroring → pick the laptop.
4. OBS: Sources → + → Window Capture → the 5KPlayer window.

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

Upload speed (from fast.com): _not measured yet_

## YouTube live requirements

- Verify the channel with a phone number at youtube.com/verify. Live streaming activates about **24 hours** later.
- Streaming from a computer (OBS) has **no subscriber minimum**. The 50-subscriber rule only applies to going live from the YouTube mobile app.
- Go Live button: youtube.com → **Create** (camera icon, top right) → Go Live, or directly at youtube.com/live_dashboard.
- **The first stream is always Unlisted** — check video, game audio, mic level, and buffering before going public.

## Shopping list beyond the chain (optional, in order of value)

1. USB or lapel mic — viewers forgive video quality, not bad audio
2. LAN cable router → laptop
3. Later: webcam + ring light for a facecam
