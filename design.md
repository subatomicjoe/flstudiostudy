# Exam Rack — Design Spec (Phase 2)

## App title
**Exam Rack** (proposed). Alternatives: **Step Study**, **Study Sequencer**.
- `<title>Exam Rack</title>`.
- Subline in the toolbar: "SOUND DESIGN EXAM · FL STUDIO 2025". The product name is used only as a description.
- Brand mark: an original inline-SVG strip of 4 step pads, with the first one lit amber. No fruit, no Image-Line marks.
- Footer, on every screen: **"Unofficial student study aid — not affiliated with Image-Line."**

## Concept
The app is a piece of studio hardware: a slate rack unit with bevelled buttons, recessed LCD windows, LEDs and pads.
- **Hardware is skeuomorphic:** toolbar, buttons, pads, LCDs, window title bars, toggles and the results mixer.
- **Reading surfaces are flat:** card faces, question text, notes and explanations. They are dark, matte and high-contrast, for long reading on phones.
- **Graphics:** CSS gradients, box-shadows and inline SVG only. No image files.

## Colour meaning (strict)
| Colour | Means | Used on |
|---|---|---|
| **Amber** | "You are here / active" | Active tab, current step pad, LCD digits, primary button, window LEDs, focus ring, search highlight |
| **Green** | **Correct** only | Correct answer pad + ✓, score meters in the results mixer (they measure % correct) |
| **Red** | **Wrong** only | The wrong answer you picked + ✗, ✗ marks in the missed list. Nowhere else. |

Colour is never the only signal: ✓ / ✗ always appear, and current/visited pads also differ in brightness and depth.

**Open question for you:** your brief asks for "green LED indicators" and also "green reserved for correct". I resolved this by using green LEDs *only* where they mean correct. All other LEDs are amber. If you'd rather have decorative green status LEDs, I'd make them a much darker green so they can't be mistaken for "correct".

## Colour tokens
The design is dark only, by choice. `:root` sets `color-scheme: dark` and an explicit body background. There is no light theme, because the hardware look doesn't survive inversion.

### Panels and neutrals (blue-grey slate)
| Token | Hex | Use |
|---|---|---|
| `--bg` | `#101317` | App background behind panels |
| `--panel` | `#1E232A` | Window body, mixer body |
| `--panel-hi` | `#2A3039` | Raised surfaces, strip tops |
| `--panel-lo` | `#171B21` | Recessed trays (tab tray, pad row, transport groups) |
| `--edge` | `#090B0E` | 1px hardware edges, separators |
| `--read` | `#13171C` | **Flat reading surface** (cards, questions, notes) |
| `--read-line` | `#262C35` | Hairline borders on reading surfaces |

### Text
| Token | Hex | Contrast on `--read` | Use |
|---|---|---|---|
| `--text-read` | `#E8ECF0` | 15.2 : 1 | Reading text |
| `--text` | `#D6DCE3` | 13.0 : 1 | UI labels |
| `--text-2` | `#A4AEBA` | 8.0 : 1 | Secondary labels, step numbers |
| `--text-3` | `#808B98` | 5.2 : 1 | Hints, counts, captions (never below 12px) |

### Amber accent
| Token | Hex | Use |
|---|---|---|
| `--amber` | `#FF9F2E` | Lit LEDs, current pad, active strokes |
| `--amber-hi` | `#FFC072` | Active text, focus ring |
| `--amber-lo` | `#9A5810` | Pressed amber, visited-pad core |
| `--amber-ink` | `#1C1106` | Text on amber (9.1 : 1) |

### LCD
| Token | Hex | Use |
|---|---|---|
| `--lcd-bg` | `#0C0905` | LCD window background |
| `--lcd-on` | `#FFB04A` | Lit segments |
| `--lcd-off` | `rgba(255,176,74,.08)` | Unlit "ghost" segments |

### Semantic
| Token | Hex | Use |
|---|---|---|
| `--ok` | `#41DC74` | Correct: LED, ✓, meter segments |
| `--ok-lo` | `#16502A` | Correct pad rim and tint |
| `--bad` | `#FF5C4F` | Wrong: LED, ✗ |
| `--bad-lo` | `#5E1A15` | Wrong pad rim and tint |
| `--led-off` | `#2B3038` | Unlit LED |

### Step pads
| Token | Hex | Use |
|---|---|---|
| `--pad-a` | `#363C45` | Pads in groups 1 and 3 |
| `--pad-b` | `#2B3038` | Pads in groups 2 and 4 |

The 20 pads are split into 4 groups of 5, with alternating shades. A group of 5 lines up with the 2 × 10 grid on phones and the 1 × 20 row on desktop.

## Typography (Google Fonts)
| Role | Family | Weights | Fallback |
|---|---|---|---|
| **Labels** (tabs, title bars, buttons, eyebrows) | **Barlow Condensed** | 500, 600, 700 | "Arial Narrow", sans-serif |
| **Body / reading** | **IBM Plex Sans** | 400, 500, 600 | system-ui, sans-serif |
| **Data** (sources, counts, small readouts) | **Share Tech Mono** | 400 | ui-monospace, monospace |
| **LCD counters** | Original **inline-SVG 7-segment digits** (no font) | — | `aria-label` carries the text |

Google Fonts has no true 7-segment face, so I drew the LCD digits as SVG: real lit and unlit segments, slightly slanted, with an amber glow.

### Type scale
| Step | Phone (390) | Desktop (1280) | Font | Use |
|---|---|---|---|---|
| Micro label | 11px / 600 / +0.08em caps | 11px | Barlow Cond. | Mixer strip names, LCD labels |
| Label | 13px / 600 / +0.08em caps | 14px | Barlow Cond. | Title bars, buttons, tabs |
| Caption | 13px / 400 | 13px | Plex Sans | Hint bar, hints |
| Data | 12–13px | 13px | Share Tech Mono | `§` sources, counts |
| Body | 16px / 1.55 | 17px / 1.6 | Plex Sans | Notes, explanations, options |
| Card / question | 21px / 500 / 1.35 | 28px | Plex Sans | Flashcard front and back, quiz question |
| Doc heading | 24px / 700 caps | 32px | Barlow Cond. | Full Notes topic title |
| Section heading | 14px / 600 / +0.1em caps, amber | 15px | Barlow Cond. | "Full notes", "Quick notes" |
| LCD | 22px | 28px | SVG digits | Counter; master score 40 / 48px |

- Reading text is capped at about 66ch.
- Headings use `text-wrap: balance`.
- Shortcuts are shown as **`<kbd>` keycaps** inside reading text, e.g. Ctrl + L.

## Spacing, radius, depth
- **Spacing scale:** 4 · 8 · 12 · 16 · 24 · 32 · 48 px.
  - 16px side gutter on phones, 24px on desktop.
  - Groups are spaced with `gap`, never margins.
- **Radius:** 2px (pads, keycaps) · 4px (buttons, LCD) · 6px (windows, option pads). Small radii read as machined hardware.
- **Depth recipes**, all CSS:
  - **Bevel:** `inset 0 1px 0 rgba(255,255,255,.07), inset 0 -1px 0 rgba(0,0,0,.45)`
  - **Raised:** bevel + `0 2px 3px rgba(0,0,0,.55)`
  - **Sunk** (trays, LCDs, inputs): `inset 0 2px 4px rgba(0,0,0,.6)`
  - **Pad thickness** (option pads): `0 3px 0 #0D1013`. When pressed, the pad moves down 3px and loses this shadow.
  - **Brushed texture:** `repeating-linear-gradient(90deg, rgba(255,255,255,.014) 0 1px, transparent 1px 3px)`, layered over the panel gradient.
  - **Screws:** radial gradient + slot line, on the toolbar ends and the mixer panel (desktop only).

## Components and states
States marked "—" don't exist for that component.

| Component | Default | Hover | Pressed / active | Disabled | Lit / unlit |
|---|---|---|---|---|---|
| **Button** (transport, secondary) | Slate gradient, bevel, raised, grey label | Lighter gradient, white label | Inverted dark gradient, sunk shadow, moves 1px down | 45% opacity, flat bevel, not-allowed cursor | — |
| **Primary button** (Next, New quiz) | Amber gradient, dark ink | Brighter amber | Deeper amber, sunk | 45% opacity | — |
| **Section tab** (desktop toolbar) | Raised in a recessed tray, LED unlit, grey label | Lighter, white label | **Current:** sunk, amber label, amber LED lit | — | LED lit = current section |
| **Transport tab** (phone bottom bar) | Raised key, icon + label, LED bar unlit | Lighter | **Current:** sunk, amber icon and label, amber LED bar lit | — | LED bar lit = current |
| **Step pad** | Raised, group shade A or B, number in `--text-2` | Brighter top highlight | Pressed down 1px | — | **Visited:** dim amber core, white number. **Current:** fully lit amber, glow, sunk, dark number, `aria-current="step"` |
| **Option pad** (quiz) | Thick raised pad, keycap letter A–D, unlit LED | Lifts: brighter, 4px thickness | Moves down 3px, thickness gone | **Locked** (after answering): half-pressed, text `--text-2`, no hover | **Correct:** green rim + tint, green LED, **✓**. **Wrong pick:** red rim + tint, red LED, **✗** |
| **LCD readout** | Recessed black window, amber digits, ghost segments visible | — | — | — | Lit segments amber with glow; unlit at 8% |
| **LED** (8px) | Unlit: dark radial + inner ring | — | — | — | Amber, green or red with a soft glow |
| **Toggle** (Expand all) | Button with LED unlit | Lighter | **On:** sunk, LED lit amber, `aria-pressed="true"` | 45% opacity | LED = state |
| **Window** (plugin-style) | Brushed title bar: LED, condensed caps title, data-font meta on the right; flat reading body | — | — | — | Title-bar LED lit = active window |
| **Search field** | Recessed, magnifier icon, `--text-read` input | — | **Focus:** amber 2px ring | — | Matches highlighted amber in results |
| **Folder row** (Quick Notes, tree) | Chevron + folder icon + number + name + count | Faint light wash | **Open / current:** amber name, amber-filled folder icon, rotated chevron | — | — |
| **Mixer strip** | Topic number in mini LCD, green segment meter, fader cap at the topic's %, score "2/3", short name | — | — | — | Lit segments = % correct (12 segments) |
| **Master channel** | Wider strip: big 7-segment score "15/20", 16-segment meter, % readout | — | — | — | — |
| **Focus (all controls)** | 2px `--amber-hi` outline, offset 2px, always visible with the keyboard (`:focus-visible`) | | | | |

## Screen behaviour
The layout switches at a **760px container width**. The app root is a CSS container, so components respond to the app's width rather than the window's.

### Phone (~390px)
- **Top bar:** brand mark + title on the left, LCD counter on the right. The section tabs move to the bottom bar.
- **Hint bar** (always present): `TOPIC` label + topic name, then the `§` source, truncated with an ellipsis.
- **Bottom transport bar:** 4 equal keys (Flashcards / Quiz / Quick / Full). Sticky to the bottom, plus the safe-area inset.
- **Flashcards:**
  - Plugin window with a full-width card, min height 240px.
  - Step pads in **2 rows of 10**, each about 30px.
  - Transport: Prev / Flip / Next on one row, Shuffle / New set on a second row.
- **Quiz:**
  - Option pads **stacked in one column**, min height 64px.
  - The explanation panel appears under the pads, with Next on the right.
- **Results:**
  - The master channel is **horizontal at the top**: big score + horizontal meter.
  - Topic strips **scroll sideways inside their own panel**. The page itself never scrolls sideways.
- **Quick Notes:** a single browser panel with the search field at the top and the folder list below.
- **Full Notes:**
  - "Topics" button + current topic above the document.
  - The tree opens as a **left drawer** (85% width, max 320px) over a dark scrim.

### Desktop (~1280px)
- **Top bar:** brand + screws on the left, **section tabs in a recessed tray** in the middle, LCD on the right.
- **Hint bar** spans the full width.
- **Flashcards and Quiz:** a centred column, max width 880px.
  - Card min height 320px.
  - Step pads in **1 row of 20**.
  - Option pads in a **2 × 2 grid**.
- **Results:**
  - Mixer up to 1100px wide.
  - Strips in a row, with the **master channel on the right**, like a console.
  - The missed-questions list sits below.
- **Quick Notes:** panel max width 820px; folders show their counts.
- **Full Notes:** tree **280px** on the left (sticky), document pane on the right, max 66ch line length.

## Content rules the design depends on
- Each topic needs a **short name** (≤ 14 characters) for mixer strips, e.g. "Routing", "Effects Rack", "Automation".
- **Quiz hint bar** shows "Topic hidden until you answer" while a question is open. The topic name would give away the answer (e.g. "05 Replace"). After answering, it shows the topic and `§` source.
- **Flashcards:** the hint bar shows the topic on both sides. The `§` source appears on the **back** only.

## Motion
- **Card flip:** 3D rotateY, 320ms, ease-out. With `prefers-reduced-motion`, it becomes a 150ms crossfade.
- **Pads and buttons:** 60ms transform on press, no bounce.
- **Mixer meters:** segments light from the bottom up, staggered by 15ms, on the results screen only. Reduced motion shows them instantly.
- Nothing else animates.
