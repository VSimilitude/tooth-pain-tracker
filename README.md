# Tooth Pain Log

A personal tooth-pain tracker. Single static page, no backend, no build step.
All entries are stored locally in your browser's `localStorage` — nothing is
ever sent to a server.

**Live site:** https://vsimilitude.github.io/tooth-pain-tracker/

## Install on iPhone

1. Open the live URL above in **Safari**.
2. Tap **Share → Add to Home Screen**.
3. Launch it from the home-screen icon. It runs full-screen and works offline.

Your entries survive closing the app and restarting the phone. Use the
**Back up** button in the History tab to export a JSON copy, and **Restore**
to merge one back in.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The entire app (HTML + CSS + JS in one file). |
| `manifest.json` | PWA metadata so it installs as a real app. |
| `sw.js` | Minimal service worker — caches the app shell for offline use. Never touches your data. |
| `icon-192.png`, `icon-512.png`, `apple-touch-icon.png` | Home-screen icons. |
| `make_icons.py` | Regenerates the icons (`python3 make_icons.py`). |

## Local development

It's a static file — just open `index.html` in a browser, or serve the folder:

```sh
python3 -m http.server 8000
# then visit http://localhost:8000/
```

> Note: `localStorage` and the service worker need a real `http(s)://` origin
> (or `localhost`). Opening via a `file://` path or an in-chat preview sandbox
> won't persist data — that's expected.
