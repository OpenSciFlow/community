# Xiaohongshu assets

Generated outreach assets for the first OpenSciFlow Xiaohongshu post.

## Cards

`cards/` contains 8 vertical cards in `1080x1350`:

1. cover
2. pain points
3. protocol layer
4. GitHub organization screenshot
5. local-agent contract screenshot
6. current progress
7. boundaries
8. call to action

## Screenshots

`screenshots/` contains GitHub page screenshots for proof/context:

- organization page;
- scientific models page;
- local agent contract;
- promotion kit.

Fresh homepage screenshots:

- `homepage-fresh-vertical.png`: full vertical homepage screenshot, `1242x1660`.
- `homepage-fresh-desktop.png`: desktop homepage screenshot, `1600x1200`.
- `homepage-fresh-mobile.png`: mobile homepage screenshot, `430x1400`.
- `homepage-fresh-clean-main.png`: clean social crop without the right sidebar, `900x1500`.
- `homepage-fresh-readme-clean.png`: README-focused clean crop, `884x1300`.
- `homepage-fresh-readme-focus.png`: README-focused crop with more surrounding context, `980x1260`.

## Regenerate cards

```powershell
python .\make_xhs_cards.py
```
