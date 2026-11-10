# Exam Rack

Unofficial student study aid for the FL Studio 2025 "Advanced Sound Designing" exam (15 Nov 2026). Not affiliated with Image-Line.

Published app (private until shared from the page's Share menu): https://claude.ai/artifact/L9vTcUsycsmPgPhPw19aNQ

## What's here
| Path | What it is |
|---|---|
| `source/` | The original markdown. **The only content source.** |
| `notes.md` | Restructured notes: full + quick notes per topic, glossary, coverage table |
| `content/flashcards.json`, `content/mcq.json` | Generated question banks (don't edit by hand) |
| `tools/build_content.py` | **Edit flashcards and MCQs here**, then rebuild |
| `tools/qa.py` | Checks the banks: minimums, answer balance, duplicates, schema |
| `tools/app_template.html` | The app's CSS, markup and JavaScript |
| `tools/build_app.py` | Inlines notes + banks into `index.html` |
| `index.html` | The finished single-file app that gets published |
| `design.md`, `design-preview.html` | Approved design spec and static preview |

## Making a change
1. Edit `notes.md`, `tools/build_content.py` or `tools/app_template.html`.
2. Rebuild and check:
   ```bash
   python tools/build_content.py
   python tools/qa.py
   python tools/build_app.py
   ```
3. Republish `index.html` to the **same** artifact. In Claude, give it the artifact link above so it updates that page instead of creating a new one.

## Known source conflicts (left out of all questions)
- Draw vs Paint key (§ 7 vs § 20)
- Right-clicking a note: delete vs Slide / Note properties (§ 7 vs § 10)
- Octave shortcut (§ 10 vs § 27)
- Sidechain: which track you right-click (§ 25 wording)
