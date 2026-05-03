# pace-legal

Static legal documents for Pace (https://usepace.fit), deployed via Cloudflare Pages.

## Structure

- `source/` — canonical markdown sources (the source of truth)
- `build.py` — converts markdown to HTML using the Pace template
- `template.html` — page wrapper
- `styles.css` — Pace brand styling
- `index.html`, `privacy.html`, `health-privacy.html`, `terms.html` — generated/static HTML files served at https://usepace.fit/

## Updating policies

1. Edit the markdown files in `source/`
2. Run `python3 build.py`
3. Commit and push — Cloudflare Pages auto-deploys

## Operator

Born in Tokyo Digital LLC · EIN 42-2068679
