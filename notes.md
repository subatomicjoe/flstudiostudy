# FL Studio 2025 — Exam Notes
### Advanced Sound Designing: Points to be Focused

**Source:** `deepseek_markdown_20261110_3ab88d.md` (only source used). Every section has a `§` reference to the source heading.
**Topic list:** The source is a "Points to be Focused" list of 27 numbered topics. All 27 are priority topics, in the source's order.

**Legend:**
- ⚠ **SOURCE CONFLICT**: two parts of the source disagree. Check with your lecturer before the exam.
- ◐ **THIN**: the source gives very little detail on this.

---

## 1. FL Studio Interface
*§ 1. FL Studio Interface*

### Full notes
FL Studio uses a **multi-window workflow**. You don't need to memorise every menu, but you **must** know the **five core windows** and their shortcuts. Every production task involves switching between them.

| Window | Shortcut | What it's for |
|---|---|---|
| **Playlist** | `F5` | The **song timeline**: arrange patterns, audio clips and automation |
| **Channel Rack** | `F6` | Load **instruments and samples**; program **drums and patterns** |
| **Piano Roll** | `F7` | Write **melodies, chords and basslines** |
| **Mixer** | `F9` | **Routing**, **volume balancing** and **effects processing** |
| **Browser** | `Alt/Opt + F8` | Browse **samples, presets and plugins** |

**Reset the layout:** if windows get lost or rearranged, press **`Shift + Ctrl + H`** to return to the default layout.

**Common confusions**
- The **Browser** is `Alt/Opt + F8`. Plain **`F8`** opens the **Plugin Picker** (§ 26), which is a different window.
- The Mixer is **`F9`**, not F8.
- The shortcuts run in order: F5 Playlist → F6 Channel Rack → F7 Piano Roll. Then F8 is skipped and F9 is the Mixer.

### Quick notes
- `F5` Playlist: the song timeline
- `F6` Channel Rack: instruments, samples, drum patterns
- `F7` Piano Roll: melodies, chords, basslines
- `F9` Mixer: routing, volume, effects
- `Alt/Opt + F8` Browser: samples, presets, plugins
- `Shift + Ctrl + H` resets the window layout

---

## 2. Channel Rack
*§ 2. Channel Rack*

### Full notes
The **Channel Rack** is the **central hub for all sound sources**.
- Each **row** is a **Channel**: one instrument or one sample.
- On the right side is the **Step Sequencer**, for quickly programming **drum patterns**.

**Key operations**
- **Add an instrument:** click the **`+` button** at the bottom, or **drag a plugin** from the Browser or the Plugin Picker into the Channel Rack.
- **Open channel settings:** **left-click the channel name** to open that instrument's detailed settings panel.
- **Mute:** click the **green light** on the left of each channel.
- **Solo:** **right-click** the green light.

**Common confusions**
- Green light: **left-click mutes**, **right-click solos**. Mixer tracks work the same way (§ 17).
- Clicking the **channel name** opens its settings. **Right-clicking** a channel opens the menu with **Insert**, **Replace**, **Load Sample** and **Piano roll** (§ 3, 4, 5, 7).

### Quick notes
- Central hub for all sound sources; one row = one Channel
- Step Sequencer on the right = quick drum patterns
- Add instrument: `+` at the bottom, or drag from Browser / Plugin Picker
- Left-click channel name → settings panel
- Green light: click = mute, right-click = solo

---

## 3. Sampler Channels
*§ 3. Sampler Channels*

### Full notes
Drag an **audio file (WAV / MP3)** directly into the Channel Rack and FL Studio **automatically creates a Sampler Channel**.
- It is the **basic channel type for playing one-shot audio**: drum hits, sound effects, vocal chops.

**Key operations**
- **Play it:** the Sampler appears in the Channel Rack. Trigger it from the **Step Sequencer**, or open its **Piano Roll** to play it **chromatically** (at different pitches).
- **Replace the sample:** **right-click** the Sampler channel → **Load Sample**.
- **Settings panel:** has **envelope**, **looping** and **pitch** controls.

**Common confusions**
- **Load Sample** swaps the *audio file* inside a Sampler.
- **Replace** (§ 5) swaps the *whole instrument* in a channel and keeps its notes.
- The Sampler is a **Generator** plugin (§ 26), because it produces sound.

### Quick notes
- Drag a WAV/MP3 into the Channel Rack → a Sampler Channel is created automatically
- Used for one-shots: drum hits, SFX, vocal chops
- Trigger from Step Sequencer, or play chromatically from its Piano Roll
- Swap the audio: right-click → Load Sample
- Settings: envelope, looping, pitch

---

## 4. Insert ◐
*§ 4. Insert*

### Full notes
**Insert** adds a **new instrument channel** to the Channel Rack, **above the currently selected channel**. Existing channels are **not affected**.

**How to use**
1. **Right-click any channel button** → **Insert >** → choose an instrument from the list.
2. If the instrument isn't listed, click **More...** to open the **full plugin picker**, then **double-click** to add it.

**Common confusions**
- **Insert** (Channel Rack) adds a *new* channel. **Replace** (§ 5) changes an *existing* one.
- New channels go **above** the selected channel, not at the bottom.
- "Insert" has two meanings in the source. This is the **Channel Rack command**. A **Mixer Insert** (§ 16, § 27) is a *mixer track*.

### Quick notes
- Insert = add a new instrument channel above the selected one
- Existing channels are untouched
- Right-click channel button → Insert > → pick instrument
- Not listed? More... → full plugin picker → double-click

---

## 5. Replace ◐
*§ 5. Replace*

### Full notes
**Replace** swaps the instrument in an **existing channel** for a different one, **while keeping all notes and pattern data** intact.

**How to use:** right-click the channel you want to change → **Replace >** → select the new instrument.

**Typical use cases**
- You programmed a drum pattern with a **temporary kick sample**. Later you replace it with a better kick **without redrawing the rhythm**.
- You swap a **placeholder synth** for your final sound.

**Common confusions**
- **Replace** keeps your notes and swaps the instrument. **Insert** (§ 4) creates a new, empty channel.
- **Load Sample** (§ 3) changes only the audio file of a Sampler.

### Quick notes
- Replace = swap the instrument, keep all notes and pattern data
- Right-click channel → Replace > → new instrument
- Use: swap a temporary kick or a placeholder synth without redrawing

---

## 6. Browser Panel
*§ 6. Browser Panel*

### Full notes
The **Browser** (`Alt/Opt + F8`) is your **single entry point for all media**. It works like a **file explorer** for everything FL Studio can use.

**Main sections**

| Section | Contents |
|---|---|
| **Packs** | **Stock** samples, loops and presets that come with FL Studio |
| **Sounds** | Additional sample content from **FL Cloud** (if your edition includes access) |
| **Plugin database** | All installed **instruments and effects**, organised **by category** |
| **Current project** | Samples and files **already used in the open project** |

**How to use**
- **Drag and drop** from the Browser into the **Channel Rack**, **Playlist** or **Mixer**.
- **Preview** a sample by clicking it (depending on your preview settings).

**Common confusions**
- **Packs** = stock content that ships with FL Studio. **Sounds** = FL Cloud content, only if your edition includes it.
- **Plugin database** is linked to the Plugin Picker (§ 26).
- **Current project** shows only what this project already uses.

### Quick notes
- `Alt/Opt + F8`: single entry point for all media, like a file explorer
- Packs = stock samples, loops, presets
- Sounds = FL Cloud content (if your edition includes it)
- Plugin database = installed instruments & effects by category
- Current project = files already used in this project
- Drag into Channel Rack, Playlist or Mixer; click to preview

---

## 7. Piano Roll
*§ 7. Piano Roll*

### Full notes
The **Piano Roll** (`F7`) is FL Studio's **core melody and chord editor**.
- **Every channel has its own Piano Roll.**
- To open one: **right-click a channel → Piano roll**.

**Essential tool shortcuts (Windows)**

| Tool | Shortcut | What it does |
|---|---|---|
| **Draw** (pencil) | `B` | Place individual notes; right-click to delete |
| **Paint** (brush) | `P` | Draw **continuous streams** of notes (great for **hi-hat rolls**) |
| **Delete** (eraser) | `D` | **Drag over** notes to remove them |
| **Select** | `E` | Box-select or click-select notes for **batch edits** |
| **Slice** | `C` | **Cut a note into two** at the clicked point |

**Tip:** in **Draw mode, right-clicking a note deletes it**, so you don't need to switch to the eraser.

> ⚠ **SOURCE CONFLICT 1 (Draw vs Paint key).** § 7 gives **Draw = `B`** and **Paint = `P`** in the Piano Roll. § 20 calls **`P` "Draw mode"** in the Playlist. The source never says whether the two windows use different keys. **Confirm which key is Draw before the exam.**
>
> ⚠ **SOURCE CONFLICT 2 (right-click a note).** § 7 says right-clicking a note in Draw mode **deletes** it. § 10 says right-clicking a note gives **Slide** and **Note properties**. The source doesn't explain when each applies.

**Common confusions**
- **Slice (`C`)** cuts one *note* in two. **Chop** in the Playlist (§ 22) slices *clips*. **Chop chords (`Alt + U`)** (§ 9) turns a chord into an arpeggio.
- **Paint** draws a stream of notes. **Draw** places single notes.

### Quick notes
- `F7`: core melody/chord editor; every channel has its own Piano Roll
- Open one: right-click channel → Piano roll
- Draw `B` · Paint `P` · Delete `D` · Select `E` · Slice `C` (⚠ see conflict)
- Paint = continuous note streams (hi-hat rolls)
- Right-click a note in Draw mode deletes it

---

## 8. Chords & Melodies
*§ 8. Chords & Melodies*

### Full notes
FL Studio has tools that generate chords and melodic ideas quickly, so you don't have to draw notes one by one.

- **Stamp tool (chord stamps)**
  - Open it with the **Stamp tool (hand icon)** in the Piano Roll toolbar, or press **`Alt + C`**.
  - Choose a **chord type** (major, minor, maj7, sus2, etc.) from the dropdown.
  - **Click a root note** to place the full chord instantly.
- **Strumize (`Alt + S`)**: slightly **offsets the notes of a chord** to create a natural, **guitar-like strum**.
- **Bassline Mode (2025 feature)**
  - Part of the **Chord Progression Tool**.
  - Generates a **matching bassline** based on your current chord progression, so you can pair chords with a bass part in seconds.

**Common confusions**
- **Strumize (`Alt + S`)** offsets chord notes slightly; the chord stays a chord. **Chop chords (`Alt + U`)** (§ 9) turns a held chord into a *stream* of notes.
- **Stamp** places one chord at the root note you click. The **Chord Progression Tool** generates *progressions*, and its **Bassline Mode** adds a bassline.
- Bassline Mode belongs to the **Chord Progression Tool**, not the Stamp tool.

### Quick notes
- Stamp tool: hand icon or `Alt + C` → pick chord type → click root note
- Chord types include major, minor, maj7, sus2
- Strumize `Alt + S`: offsets chord notes into a guitar-like strum
- 2025: Chord Progression Tool's Bassline Mode generates a matching bassline

---

## 9. Piano Roll Tools (Basic)
*§ 9. Piano Roll Tools (Basic)*

### Full notes
Everyday helpers that make Piano Roll editing faster:

- **Scale Highlighting**
  - Menu: **`Helpers > Scale highlighting`**.
  - Choose a **key and scale**. Notes **outside the scale are dimmed**, so you avoid "wrong" notes.
- **Ghost Channels (`Alt + V`)**
  - While editing one channel, **faintly shows notes from other channels**.
  - Perfect for aligning a **bassline to chords**, or writing a **melody against a drum groove**.
- **Chop chords (`Alt + U`)**: turns a **held chord into an arpeggiated stream** of notes.
- **Riff Machine (`Alt + E`)**: **generates melodic motifs and variations** from your existing progression. Useful for breaking **writer's block**.

**Common confusions**
- Scale Highlighting **dims** out-of-scale notes.
- Ghost Channels shows *other* channels' notes faintly. It's for reference while writing.
- Shortcut set to memorise: **`Alt + V`** Ghost · **`Alt + U`** Chop · **`Alt + E`** Riff Machine · **`Alt + S`** Strumize (§ 8) · **`Alt + C`** Stamp (§ 8) · **`Alt + R`** randomise velocity (§ 10).

### Quick notes
- Scale highlighting: Helpers > Scale highlighting; out-of-scale notes dimmed
- Ghost Channels `Alt + V`: faintly show other channels' notes
- Chop chords `Alt + U`: held chord → arpeggiated stream
- Riff Machine `Alt + E`: generates motifs/variations; beats writer's block

---

## 10. Notes
*§ 10. Notes*

### Full notes
Every note in the Piano Roll can be edited in detail, not just its pitch and length.

- **Transpose**
  - Select notes, then **`Shift + ↑/↓`** moves them by a **semitone**.
  - **`Ctrl + Shift + ↑/↓`** moves them by an **octave**.
- **Velocity**
  - Select notes and **drag the vertical bars** in the **velocity pane** at the bottom of the Piano Roll.
  - **`Alt + R`** **randomises velocity**, which makes drums or keyboards sound more **human**.
- **Slide notes** (FL Studio's **signature feature**)
  - Right-click a note → choose **Slide**, or use the **Slide tool**.
  - Slide notes create **pitch glides**, which are **essential for 808 basslines**.
- **Note properties:** right-click a **single note** → **Note properties** to fine-tune **pitch and other parameters**.

> ⚠ **SOURCE CONFLICT 3 (octave shortcut).** § 10 says octave transpose is **`Ctrl + Shift + ↑/↓`**. § 27 (Octave) says **`Ctrl + ↑/↓`**. Both agree that **`Shift + ↑/↓` = one semitone**. **Confirm the octave shortcut before the exam.**
>
> ⚠ See also **SOURCE CONFLICT 2** in § 7 (right-click deletes vs. right-click opens Slide / Note properties).

**Common confusions**
- **Semitone** = `Shift` + arrow. Octave = see conflict above.
- **Velocity** is edited in the **velocity pane** at the *bottom* of the Piano Roll, not by moving the note.
- **Slide** = a pitch glide between notes. **Strumize** (§ 8) = a timing offset inside a chord.

### Quick notes
- `Shift + ↑/↓` = transpose one semitone
- Octave: `Ctrl + Shift + ↑/↓` (§ 10) vs `Ctrl + ↑/↓` (§ 27) ⚠
- Velocity: drag bars in the velocity pane; `Alt + R` randomises (humanises)
- Slide notes = pitch glides, essential for 808 basslines
- Right-click a single note → Note properties: fine-tune pitch etc.

---

## 11. Piano Roll Tools (Advanced / Generative) ◐
*§ 11. Piano Roll Tools (Advanced / Generative)*

### Full notes
This topic complements § 9 and focuses on **automated generation and batch processing**.

- **Fill each 2 / 4 / 8 step**
  - Found **in the Stamp menu or related tools**.
  - **Automatically fills notes at fixed intervals**, e.g. a **kick every 4 steps** or a **snare every 8 steps**.
  - Builds **steady rhythmic patterns** quickly.
- **Riff Machine (advanced use)**
  - Goes beyond basic melody generation: **adjust its parameters** to produce **different variations of a motif**.
  - A fast way to generate **editable MIDI material** when you need ideas.

◐ **Thin in source:**
- The exact menu for "Fill each" is vague ("Stamp menu or related tools").
- No Riff Machine parameter names are given.

**Common confusions**
- **Fill each N steps** places notes at *fixed rhythmic intervals*. **Paint** (§ 7) draws a stream by hand.
- Riff Machine appears in both § 9 (basic: generate motifs, `Alt + E`) and § 11 (advanced: adjust parameters for variations).

### Quick notes
- Fill each 2/4/8 step: auto-fill notes at fixed intervals (Stamp menu or related tools)
- Example: kick every 4 steps, snare every 8
- Riff Machine advanced: adjust parameters → motif variations
- Output = editable MIDI material

---

## 12. Tempo Tapper
*§ 12. Tempo Tapper*

### Full notes
Use the **Tempo Tapper** when you have a sample or melody but **don't know its BPM**. You "tap" the tempo yourself.

**How to use**
1. **Right-click the BPM value** in the top toolbar and choose **Tap**, or open Tempo Tapper from the **View menu**.
2. Play the audio and **click the TAP button repeatedly in time with the beat**.
3. After several taps, FL Studio calculates an **estimated BPM**.

**The "Apply tempo" setting**
- **Enabled:** the project tempo is **set** to the tapped value.
- **Disabled:** it **only measures** and doesn't change the project.

**Common confusions**
- The result is an **estimate** and needs several taps.
- If you only want to *check* a tempo, turn **Apply tempo off**.

### Quick notes
- Use when you don't know a sample's BPM
- Open: right-click the BPM value → Tap, or View menu
- Click TAP repeatedly in time with the beat → estimated BPM
- Apply tempo ON = sets project tempo; OFF = only measures

---

## 13. Templates
*§ 13. Templates*

### Full notes
**Templates** are **pre-configured project starting points**, so you don't repeat the same setup every time.

- **Open a template:** **`File > New from template`**, then choose one from the list.
- **Loop Starter (2025 feature)**
  - **Genre-based loop templates**.
  - You can start a loop straight from a template and **access FL Cloud samples directly**.
- **Custom templates**
  - Set up your favourite **tracks, routing and effects**.
  - Save the project as a template file in **FL Studio's Templates folder**.
  - It then appears in **New from template**.

**Common confusions**
- **Loop Starter** is the **2025** genre-based feature. Ordinary templates are found under `File > New from template`.
- A custom template only shows up if it's saved in the **Templates folder**.

### Quick notes
- Templates = pre-configured project starting points
- `File > New from template`
- 2025 Loop Starter: genre-based loop templates + direct FL Cloud samples
- Custom: set up tracks/routing/effects → save in the Templates folder

---

## 14. Make Some Noise
*§ 14. Make Some Noise*

### Full notes
Your **first practical goal**: build a **complete 4-bar loop** using the minimal workflow.

**Standard beginner exercise**
1. **Drums:** load **Kick**, **Clap/Snare** and **Hi-hat** in the Channel Rack. Click in a basic rhythm with the **Step Sequencer**.
2. **Bass:** add a bass instrument channel, open its **Piano Roll**, and draw a bassline **following the root notes**.
3. **Chords / Melody:** add a synth or keyboard sound. Place a chord progression with the **Stamp tool**, or draw a simple melody in the Piano Roll.
4. **Listen to the loop:**
   - Press **`Space`** to play.
   - In the **Playlist**, drag the pattern onto a track.
   - Press **`L`** to switch to **Song mode** and let the loop repeat.

**The goal** isn't perfection. It's to **connect the full chain: Channel Rack → Piano Roll → Playlist**.

### Quick notes
- Goal: a complete 4-bar loop
- Drums (Kick, Clap/Snare, Hi-hat) in the Step Sequencer
- Bass in the Piano Roll, following the root notes
- Chords via the Stamp tool, or a simple melody
- `Space` play · drag pattern to Playlist · `L` = Song mode
- Chain: Channel Rack → Piano Roll → Playlist

---

## 15. Packs and Sounds ◐
*§ 15. Packs and Sounds (overlaps § 6)*

### Full notes
FL Studio ships with a large amount of **stock material**, found mainly in the Browser's **Packs** folder.

- **Packs:** drum samples, loops, one-shot effects and presets, **organised by style and type**.
- **Sounds:**
  - Available if your edition includes **FL Cloud** access.
  - The **Sounds tab** lets you **browse and audition** cloud samples and **drag them straight into your project**.
- **Browsing tip:**
  - Use the **search box at the top of the Browser** to filter quickly, e.g. "kick", "808", "riser".
  - **Click a sample to preview it** (depending on your preview settings).

**Common confusions**
- **Packs** = stock material, always included. **Sounds** = FL Cloud, depends on your edition.

### Quick notes
- Packs = stock drums, loops, one-shots, presets (by style & type)
- Sounds tab = FL Cloud samples (if your edition includes it); drag into project
- Search box at the top of the Browser filters ("kick", "808", "riser")
- Click a sample to preview

---

## 16. Mixer Track Routing
*§ 16. Mixer Track Routing*

### Full notes
**By default, every instrument in the Channel Rack outputs directly to the Master track.** To control each sound on its own, route each instrument to its own **Insert track** in the Mixer.

**Three common routing methods**

| Method | Steps |
|---|---|
| **Channel settings panel** | Left-click the channel → find the **FX / TRK field** → type or drag to the target Insert number |
| **Shortcut `Ctrl + L`** | **Select** one or more channels in the Channel Rack → **click the target Insert** in the Mixer → press **`Ctrl + L`** |
| **Right-click routing** | **Select the target Insert** in the Mixer → right-click the channel in the Channel Rack → **Route to this track** |

**2025 notes**
- **Right-click an empty plugin slot** in the Mixer to add a plugin.
- **Playback tracking now defaults to the Mixer.**

**Best practice:** for a clean mix, route at least **Kick, Snare, Hi-hat, Bass, melody and vocals** to separate Inserts.

**Common confusions**
- The default output is the **Master**, not an Insert.
- **`Ctrl + L`** order: channels first, then the target Insert, then the shortcut.
- **Route to this track** order: the target Insert is selected first, then you right-click the channel.
- The **FX / TRK field** is in the **channel settings panel**, not in the Mixer.

### Quick notes
- Default: every instrument → Master track
- Route each sound to its own Insert to control it independently
- Channel settings → FX / TRK field → Insert number
- Select channels → click Insert → `Ctrl + L`
- Select Insert → right-click channel → Route to this track
- Route at least Kick, Snare, Hi-hat, Bass, melody, vocals separately

---

## 17. Mixer Track Options
*§ 17. Mixer Track Options*

### Full notes
Each **Mixer Insert** is an **independent audio channel** with its own **volume, pan, effect chain and routing**.

**Common track options**
- **Rename:** select the track and press **`F2`**, or right-click the track label → **Rename**.
- **Colour-code:**
  - Right-click the track label → **Change color**.
  - Use consistent colours for instrument groups (e.g. **red = drums, green = bass, yellow = vocals**) so you can navigate quickly.
- **Mute / Solo:**
  - The **green circular button** mutes the track.
  - **Right-click** it to **solo** the track; all others are muted.
  - Very useful for **troubleshooting**.
- **Pan and stereo separation:** the **knobs at the top** of the strip control **panning** and **stereo width**.

**Common confusions**
- **`F2`** renames a Mixer track. Don't confuse it with the window shortcuts F5–F9.
- Mute vs solo works the same as in the Channel Rack (§ 2): click = mute, right-click = solo.

### Quick notes
- Each Insert has its own volume, pan, effect chain, routing
- Rename: `F2` or right-click label → Rename
- Colour: right-click label → Change color (e.g. red drums, green bass, yellow vocals)
- Green button = mute; right-click = solo (others muted)
- Top knobs = pan & stereo width

---

## 18. Effects Rack
*§ 18. Effects Rack*

### Full notes
Each Mixer Track has **10 effect slots** on its right side. Audio flows **from Slot 1 to Slot 10, top to bottom**.

**How to use**
- **Add an effect:** click an **empty slot** → choose an effect plugin from the **Plugin Picker**. (2025: you can also **right-click** an empty slot, see § 16.)
- **Open an effect:** click the **slot label** to open the plugin's GUI and adjust its parameters.
- **Reorder:** **drag slot labels** to reorder effects. The **signal flow changes** to match.
- **Bypass:** click the **green indicator** on the left of a slot to **bypass** that effect, for **A/B comparison**.

**Typical order**
1. **EQ**: fix problem frequencies
2. **Compression**: control dynamics
3. **Creative effects**: saturation, chorus
4. **Time-based effects**: delay / reverb

**Common confusions**
- There are **10** slots, and the order **matters** because signal flows top to bottom.
- **Bypass** (green slot indicator) turns off *one effect*. **Mute** (§ 17) silences the *whole track*.
- Reverb and delay are **time-based** effects and come **last** in the typical order.

### Quick notes
- 10 effect slots per track; audio flows Slot 1 → 10, top to bottom
- Click empty slot → pick effect; click label → open GUI
- Drag labels to reorder; signal flow follows
- Green slot indicator = bypass (A/B compare)
- Typical order: EQ → compression → creative → delay/reverb

---

## 19. Mixer Panel Tools
*§ 19. Mixer Panel Tools*

### Full notes
Each Mixer Track **strip** (channel strip) contains these core tools, **from top to bottom**:

1. **Track name**: identifies the track's purpose.
2. **Peak meter**: shows the **real-time level**. Avoid **clipping (red)**.
3. **Pan / Stereo Separation**: controls panning and stereo width.
4. **Volume fader**: adjusts the track's **output level**.
5. **Mute / Solo**: mutes or solos the track.
6. **Record Arm**: the **circular button (often a disk icon) at the bottom**. It **arms the Mixer Track as a recording destination**.

**Common confusions**
- **Record Arm** is on the individual track (at the bottom of the strip). The **main Record button** (§ 23, § 24) is a separate control.
- **Peak meter** shows the level. The **volume fader** sets it.

### Quick notes
- Strip, top to bottom: name → peak meter → pan/stereo → fader → mute/solo → record arm
- Peak meter: watch for red (clipping)
- Volume fader sets the track's output level
- Record Arm (circular/disk icon, bottom) = makes the track a recording destination

---

## 20. Playlist
*§ 20. Playlist*

### Full notes
The **Playlist** (`F5`) is your **song timeline**. Its tracks are **"multi-purpose Clip Tracks"** that can hold **three types of clips**:

| Clip type | What it does |
|---|---|
| **Pattern Clip** | Plays a **Pattern** from the Channel Rack (notes, drums) |
| **Audio Clip** | Plays **recorded or imported audio** |
| **Automation Clip** | **Automates a parameter** over time |

**Placing clips:** switch to **Draw mode (`P`)** and **left-click** on a Playlist track to place the **currently selected Pattern Clip**. Audio and automation clips are placed the same way.

> ⚠ See **SOURCE CONFLICT 1** in § 7: here `P` = Draw (Playlist); in § 7, `P` = Paint (Piano Roll).

**Common confusions**
- Playlist tracks are **multi-purpose**: any track can hold any of the three clip types.
- A **Pattern Clip** plays a Pattern. The Pattern itself lives in the Channel Rack / Piano Roll.

### Quick notes
- `F5` = song timeline
- Tracks are multi-purpose Clip Tracks
- 3 clip types: Pattern, Audio, Automation
- Draw mode (`P`) + left-click places the selected Pattern Clip

---

## 21. Patterns To Songs
*§ 21. Patterns To Songs*

### Full notes
**Patterns are the "ingredients"; the Playlist is the "finished dish".**

**Building a full song**
1. Create **several Patterns** in the Channel Rack / Piano Roll, e.g. `Intro`, `Verse`, `Chorus`, `Bridge`.
2. In the Playlist, **arrange copies of these Pattern Clips from left to right** to form the song structure.
3. Press **`L`** to switch to **Song mode**. FL Studio plays all clips **in the order they appear** in the Playlist.

**Reuse and linking**
- One Pattern can be **reused as many times as you like**.
- If you **edit the Pattern's content**, **every clip that references it updates automatically**.

**Common confusions**
- Editing a Pattern changes **every** copy of it in the Playlist, not only the one you clicked.
- **`L`** = Song mode (play the whole Playlist arrangement).

### Quick notes
- Patterns = ingredients; Playlist = finished dish
- Make Patterns (Intro/Verse/Chorus/Bridge) → arrange left to right
- `L` = Song mode; clips play in Playlist order
- Edit a Pattern → every clip using it updates

---

## 22. Playlist Tools
*§ 22. Playlist Tools*

### Full notes
The Playlist toolbar and right-click menus offer these editing tools:

- **Chop:** in the **Clip menu** or the **right-click menu**, choose **Chop** to **slice Pattern or Automation Clips** into smaller pieces for rearranging.
- **Draw / Paint modes:** quickly **place or paint clips**.
- **Select tool (`E`):** **box-select or move** clips.
- **Snap:** controls the **grid resolution** for moving and slicing clips.
- **Mini overview (2025 improvement):** added to the **horizontal scrollbar**, making long songs easy to navigate.

**Common confusions**
- **Chop** (Playlist) slices *clips*. **Slice `C`** (§ 7) cuts a *note*. **Chop chords `Alt + U`** (§ 9) arpeggiates a chord.
- **Snap** sets grid resolution. It doesn't cut anything itself.
- `E` = Select in both the Playlist and the Piano Roll.

### Quick notes
- Chop (Clip menu / right-click): slice Pattern or Automation Clips
- Draw / Paint: place or paint clips
- Select `E`: box-select or move clips
- Snap = grid resolution for moving/slicing
- 2025: mini overview on the horizontal scrollbar

---

## 23. Audio Recording
*§ 23. Audio Recording*

### Full notes
To record **vocals or external instruments**:

1. **Open the Mixer (`F9`)** and select a **free Insert Track**.
2. **Set the input source** at the **top of the track**:
   - Choose the input channel for your **audio interface**, e.g. `In 1`.
   - **Mono microphones usually use a mono input.**
3. **Arm the track:** click the **record-arm button** (circular/disk icon) at the **bottom** of the track so it lights up.
4. **Set the recording filter:** **right-click the main Record button** and make sure **Audio** is ticked.
5. Press the **main Record** button and **Play** to start.

**Result**
- The recording appears as an **Audio Clip** in the Playlist.
- An **Audio Track** is **automatically created and linked** to it.

**Common confusions**
- **Input** is set at the **top** of the track. **Record arm** is at the **bottom**.
- The **Audio** tick lives in the **main Record button's right-click menu**. The same menu has **Automation** (§ 24).
- Use a **free** Insert so the recording doesn't share a track with another sound.

### Quick notes
- `F9` → pick a free Insert
- Top of track: set input (e.g. `In 1`; mono mic → mono input)
- Bottom: record-arm button (disk icon) lit
- Right-click main Record → tick Audio
- Record + Play → Audio Clip in Playlist + auto-linked Audio Track

---

## 24. Recording & Editing Automation
*§ 24. Recording & Editing Automation*

### Full notes
**Automation** makes parameters **change over time**. There are two main approaches.

**A. Record automation**
1. **Right-click the main Record button** → tick **Automation**.
2. Press **Record** and **Play**, then **turn the knob** you want to automate (e.g. filter cutoff, volume fader) on the plugin or Mixer.
3. FL Studio creates **Event Data** (event automation).
   - Edit it in the **Event Editor**, or
   - Convert it to an Automation Clip with **`Edit > Turn into automation clip`**.

**B. Create an Automation Clip manually**
1. **Right-click any automatable knob or parameter** → **Create automation clip**.
2. An **Automation Clip** appears in the **Playlist**.
3. Use the **Draw tool** to **draw control points** on the clip and shape the curve.

**Type value (2025 improvement):** the **node pop-up menu** in Automation Clips now has a **Type value** field, so you can enter **precise values** instead of dragging.

**Common confusions**
- **Recording** automation produces **Event Data**, not an Automation Clip. You convert it with `Edit > Turn into automation clip`.
- **Create automation clip** (right-click a knob) produces an **Automation Clip** directly in the Playlist.
- Record filter: **Audio** (§ 23) and **Automation** are both ticked from the **main Record button's right-click menu**.

### Quick notes
- Right-click main Record → tick Automation → Record + Play → turn knob
- Recorded result = Event Data (edit in Event Editor)
- Convert: Edit > Turn into automation clip
- Manual: right-click knob → Create automation clip → draw points in Playlist
- 2025: node pop-up "Type value" for precise values

---

## 25. Mixing & Effects
*§ 25. Mixing & Effects*

### Full notes
**Goal of mixing:** make all sounds **coexist in volume, frequency and space** without **masking** each other.

**Core workflow**
1. **Routing:** send each main sound to its **own Insert** (§ 16).
2. **Volume balance:**
   - Start with the **most important element** (kick or vocal) and build the other tracks **around it**.
   - The **Master meter should not be constantly red**.
3. **Effects processing:**
   - **EQ**: **cut unwanted low or harsh high frequencies**. Plugin: **Fruity Parametric EQ 2**.
   - **Compression**: **control dynamics** and make sounds more **consistent**. Plugins: **Fruity Compressor / Fruity Limiter**.
   - **Spatial effects**: use **Sends** to **share reverb/delay**, so multiple sounds sit in the **same space**.
4. **Sidechain:** the **kick triggers a compressor on the bass**, so the bass **"ducks"** when the kick hits.
   - In the Mixer's **routing panel** at the bottom, **right-click the routing triangle** under the kick track → **Sidechain to this track only**.
   - Then select that sidechain source in the **bass compressor**.

**Common confusions**
- **Sends** share *one* reverb/delay between several sounds. They are not a separate reverb per track.
- In a sidechain, the **kick is the trigger** and the **bass gets compressed** (it ducks).
- **Fruity Limiter** is listed under **compression**, alongside Fruity Compressor.
- The source doesn't say which track must be *selected* before you right-click the routing triangle.

### Quick notes
- Mixing goal: no masking in volume, frequency, space
- Balance from the most important element (kick/vocal); Master not constantly red
- EQ = Fruity Parametric EQ 2 (cut lows/harsh highs)
- Compression = Fruity Compressor / Fruity Limiter (dynamics)
- Sends = shared reverb/delay
- Sidechain: kick ducks bass; routing triangle → "Sidechain to this track only"

---

## 26. Plugins
*§ 26. Plugins*

### Full notes
FL Studio plugins fall into **two main categories**, managed through the **Plugin Picker (`F8`)**.

| Category | Purpose | Examples |
|---|---|---|
| **Generator** (instrument) | **Produces** sound | Sampler, Sytrus, FLEX, third-party VSTi |
| **Effect** | **Processes** sound | Fruity Parametric EQ 2, Fruity Limiter, Fruity Reeverb 2 |

**Management tips**
- **Favourites:**
  - Right-click a plugin in the Plugin Picker → add to **Favorites**.
  - Favourites appear **at the top of the list**, and FL Studio **learns your usage habits**.
- **Plugin database:** this folder in the Browser is **linked to the Plugin Picker**, so you can organise and search plugins **by category**.

**2025 improvements**
- The **Plugin Manager** can now **change a plugin's type** (e.g. Effect → Generator) **after verification**.
- **Waves plugins** automatically **merge VST3 and VST2 entries** during verification.

**Common confusions**
- **`F8`** = Plugin Picker. **`Alt/Opt + F8`** = Browser (§ 1).
- **Generator** = makes sound (Sampler, Sytrus, FLEX). **Effect** = changes sound (EQ, Limiter, Reeverb 2).
- **Plugin Picker** = choose and add plugins. **Plugin Manager** = change a plugin's type after verification.

### Quick notes
- Plugin Picker = `F8`
- Generator produces sound (Sampler, Sytrus, FLEX, VSTi)
- Effect processes sound (Parametric EQ 2, Limiter, Reeverb 2)
- Favourites: right-click → Favorites; shown at top
- Plugin database (Browser) is linked to the Plugin Picker
- 2025: Plugin Manager can change plugin type; Waves VST2/VST3 auto-merge

---

## 27. Music Theory & Terminology for FL Studio
*§ 27. Music Theory & Terminology for FL Studio*

### Full notes
Essential musical terms, defined the way they appear inside FL Studio.

**Pitch & notes**
- **Pitch**: how **high or low** a sound is.
  - Shown on the **vertical axis of the Piano Roll**; higher notes sit further up.
  - The **Pitch knob** on a Sampler or synth changes the pitch of the sound.
  - **Middle C = `C5`** in FL Studio's default naming. It is the reference point.
- **Note**: a **single musical sound** with a defined pitch and duration. Each rectangle in the Piano Roll is a note. A note has:
  - **Pitch**: its vertical position
  - **Start time**: its horizontal position
  - **Length**: how wide the rectangle is
  - **Velocity**: how hard it is "played" (set in the velocity pane)
- **Octave**: the interval to a pitch with **double or half the frequency**.
  - Octaves are stacked vertically and **share the same letter name** (C4, C5, C6).
  - The Piano Roll can show multiple octaves.
  - Transpose selected notes by an octave with **`Ctrl + ↑/↓`**. ⚠ See SOURCE CONFLICT 3 in § 10.
- **Semitone (half step)**: the **smallest interval** in Western music.
  - One key on a piano, **one step on the Piano Roll grid**.
  - **`Shift + ↑/↓`** transposes by one semitone.

**Scales, keys, chords**
- **Scale**: a **set of notes** in ascending or descending order that forms the **tonal basis** of a piece.
  - Common scales: **major, minor, pentatonic, chromatic**.
  - FL's **Scale Highlighting** (`Helpers > Scale highlighting`) dims out-of-key notes.
- **Key**: the **central note** a piece is built around.
  - Example: "**C major**" = the scale starts on C and uses the major pattern.
  - Set it in the **Scale Highlighting menu**, or by choosing the **root note in the Stamp tool**.
- **Chord**: **three or more notes played together**.
  - Draw them manually, or use the **Stamp tool** (major, minor, seventh, etc.).
  - The **Chord Progression Tool** can generate progressions for you.
- **Melody**: a **sequence of single notes** forming the main tune.
  - Written in the Piano Roll of a melodic instrument channel.
  - Use **Ghost Channels** to see the chords while you write.
- **Harmony**: the **combination of simultaneous notes**, usually chords, that **supports a melody**.
  - Made by layering notes in the Piano Roll, or by stamping chords under a melody.

**Time**
- **Rhythm**: the **pattern of sounds in time**, i.e. where notes sit relative to the beat.
  - Programmed in the **Step Sequencer** (drums).
  - Seen in the Piano Roll as the **horizontal spacing** of notes.
- **Beat & Bar**
  - A **beat** = the basic pulse.
  - A **bar** (measure) = a group of beats, usually **4 in 4/4 time**.
  - Bars are divided by **vertical grid lines** in the Playlist and Piano Roll.
  - The **Step Sequencer shows 16 steps per bar** by default = **sixteenth notes**.
- **BPM (Beats Per Minute)**: the **tempo**.
  - Shown at the top of the toolbar.
  - Change it by **clicking and dragging the number**, or detect it with the **Tempo Tapper** (§ 12).

**Sound**
- **Velocity**: **how hard a note is played**. It affects **volume and sometimes timbre**.
  - **Higher velocity = louder/harder.**
  - Adjust the bars in the velocity pane; **`Alt + R`** randomises.
- **Timbre (tone colour)**: the **character or "colour" of a sound** that makes a piano sound different from a guitar **at the same pitch**.
  - Set by the **instrument (plugin)** you choose and its **settings** (oscillators, filters, effects).

**FL Studio structures**
- **Pattern**: a **container for musical data** (notes, automation).
  - One Pattern can hold **multiple channels'** data.
  - Patterns are the building blocks you arrange in the Playlist (§ 2, § 21).
- **Clip**: a **block placed in the Playlist** that plays back a Pattern, an audio file or an automation curve. Types: **Pattern, Audio, Automation** (§ 20).
- **Automation**: **recorded or drawn changes to a parameter over time**, e.g. a filter slowly opening. Stored as **Event Data** or an **Automation Clip** (§ 24).
- **Mixer Insert / Track**: a Mixer channel that **receives audio from one or more instruments**, with **independent volume, panning and effects** (§ 16–19).
- **Send**: **routes audio from one Mixer track to another**, typically to **share** reverb or delay.
  - In the routing panel, **click the send triangle** under a track to enable a send.
- **Sidechain**: **one sound triggers a compressor on another**, causing it to **"duck"**.
  - Classic use: the **kick ducks the bass**.
  - Set the sidechain source in the routing panel, then select it in a compressor (§ 25).
- **Plugin (Generator vs. Effect)**: software that **generates** sound (synths, samplers) or **processes** sound (EQ, reverb). Managed via the **Plugin Picker (`F8`)** (§ 26).
- **Master Track**: the **final Mixer track** that all other tracks eventually feed into. It is the **overall output** of the song. Keep it **below clipping (red)**.

**Common confusions**
- **Octave** = same letter name, double/half frequency. **Semitone** = one grid step.
- **Key** = the central note. **Scale** = the set of notes. "C major" names both.
- **Melody** = single notes in sequence. **Harmony** = simultaneous notes that support it. **Chord** = 3+ notes together.
- **Pitch** = how high/low. **Timbre** = what kind of sound, at the same pitch.
- **Pattern** = the content. **Clip** = a block in the Playlist that plays that content.
- **Send** = audio to another track to share an effect. **Sidechain** = one sound controls compression on another.

### Quick notes
- Middle C = `C5` in FL Studio
- Semitone = one grid step (`Shift + ↑/↓`); octave = same letter, double/half frequency
- Chord = 3+ notes together; melody = single notes in sequence; harmony supports melody
- 4/4: 4 beats per bar; Step Sequencer = 16 steps/bar = sixteenth notes
- Velocity: higher = louder/harder; timbre = a sound's "colour"
- Pattern = data container; Clip = block in the Playlist
- Send shares effects; sidechain makes one sound duck another; Master = final output

---

## Final practical advice (from source)
*§ Final Practical Advice*

You don't need to master all 27 topics before making music. Suggested learning path:
1. **Build a 4-bar loop** with topics 1, 6, 14, 2, 7 and 8.
2. **Expand it into a short song** with topics 20 and 21.
3. **Mix it** with topics 16–19 and 25.
4. **Refer back to topic 27** whenever a musical term is unclear.

Topics 12, 13, 15 and 26 are tools that become useful once you're comfortable with the basic workflow.

---

## Glossary

| Term | Meaning | § |
|---|---|---|
| **Apply tempo** | Tempo Tapper option: on = sets project BPM, off = only measures | 12 |
| **Audio Clip** | Playlist clip that plays recorded or imported audio | 20, 23 |
| **Audio Track** | Created automatically and linked to a new recording | 23 |
| **Automation** | Recorded or drawn change to a parameter over time | 24, 27 |
| **Automation Clip** | Playlist clip that automates a parameter; made via right-click knob → Create automation clip | 20, 24 |
| **Bar (measure)** | Group of beats, usually 4 in 4/4; 16 steps in the Step Sequencer | 27 |
| **Bassline Mode** | 2025 Chord Progression Tool mode that generates a matching bassline | 8 |
| **Beat** | The basic pulse of a piece | 27 |
| **BPM** | Beats per minute, the tempo; shown in the top toolbar | 27 |
| **Browser** | `Alt/Opt + F8`; single entry point for all media | 1, 6 |
| **Bypass** | Green slot indicator; turns one effect off for A/B comparison | 18 |
| **Channel** | One row in the Channel Rack: an instrument or sample | 2 |
| **Channel Rack** | `F6`; central hub for all sound sources | 1, 2 |
| **Chop (Playlist)** | Slices Pattern or Automation Clips into smaller pieces | 22 |
| **Chop chords** | `Alt + U`; turns a held chord into an arpeggiated stream | 9 |
| **Chord** | Three or more notes played together | 27 |
| **Chord Progression Tool** | Generates chord progressions; has Bassline Mode (2025) | 8, 27 |
| **Clip** | Block in the Playlist that plays a Pattern, audio or automation | 20, 27 |
| **Clip Track** | Multi-purpose Playlist track that can hold any clip type | 20 |
| **Create automation clip** | Right-click menu item on any automatable knob | 24 |
| **Current project** | Browser section listing files already used in the project | 6 |
| **Effect (plugin)** | Plugin that processes sound | 26 |
| **Effect slots** | 10 per Mixer track; signal flows Slot 1 → 10 | 18 |
| **Event Data / Event Editor** | What recorded automation becomes / where you edit it | 24 |
| **Fill each 2/4/8 step** | Auto-fills notes at fixed intervals | 11 |
| **FL Cloud** | Online sample source behind the Sounds tab and Loop Starter | 6, 13, 15 |
| **FX / TRK field** | Field in channel settings that sets the target Mixer Insert | 16 |
| **Generator** | Plugin that produces sound (Sampler, Sytrus, FLEX, VSTi) | 26 |
| **Ghost Channels** | `Alt + V`; faintly shows other channels' notes | 9 |
| **Harmony** | Simultaneous notes (usually chords) supporting a melody | 27 |
| **Insert (Channel Rack)** | Adds a new instrument channel above the selected one | 4 |
| **Key** | The central note a piece is built around | 27 |
| **Load Sample** | Right-click a Sampler → swap its audio file | 3 |
| **Loop Starter** | 2025 genre-based loop templates with FL Cloud access | 13 |
| **Master Track** | Final Mixer track; overall output; keep below red | 16, 27 |
| **Melody** | Sequence of single notes forming the main tune | 27 |
| **Middle C** | `C5` in FL Studio's default naming | 27 |
| **Mixer** | `F9`; routing, volume balancing, effects | 1 |
| **Mixer Insert / Track** | Mixer channel with its own volume, pan, effects, routing | 16, 17, 27 |
| **Note** | Single sound with pitch, start time, length, velocity | 27 |
| **Note properties** | Right-click a single note → fine-tune pitch etc. | 10 |
| **Octave** | Interval to double/half frequency; same letter name | 27 |
| **Packs** | Stock samples, loops, presets shipped with FL Studio | 6, 15 |
| **Paint tool** | Draws continuous streams of notes (hi-hat rolls) | 7 |
| **Pattern** | Container for notes/automation; can hold multiple channels | 21, 27 |
| **Pattern Clip** | Playlist clip that plays a Pattern | 20 |
| **Peak meter** | Real-time level on a mixer strip; avoid red | 19 |
| **Piano Roll** | `F7`; melody/chord editor; one per channel | 1, 7 |
| **Pitch** | How high or low a sound is; Piano Roll vertical axis | 27 |
| **Playlist** | `F5`; song timeline | 1, 20 |
| **Plugin database** | Browser folder linked to the Plugin Picker | 6, 26 |
| **Plugin Manager** | 2025: can change a plugin's type after verification | 26 |
| **Plugin Picker** | `F8`; where you choose and add plugins | 26 |
| **Record Arm** | Circular/disk button at the bottom of a strip; arms the track for recording | 19, 23 |
| **Replace** | Swaps a channel's instrument and keeps notes and pattern data | 5 |
| **Rhythm** | Pattern of sounds in time | 27 |
| **Riff Machine** | `Alt + E`; generates motifs and variations | 9, 11 |
| **Route to this track** | Right-click channel option after selecting a Mixer Insert | 16 |
| **Sampler Channel** | Auto-created when you drag WAV/MP3 into the Channel Rack | 3 |
| **Scale** | Set of notes forming the tonal basis | 27 |
| **Scale Highlighting** | `Helpers > Scale highlighting`; dims out-of-scale notes | 9, 27 |
| **Semitone** | Smallest interval; one grid step; `Shift + ↑/↓` | 10, 27 |
| **Send** | Routes one Mixer track to another to share an effect | 25, 27 |
| **Sidechain** | One sound triggers a compressor on another so it ducks | 25, 27 |
| **Slice tool** | `C`; cuts a note in two | 7 |
| **Slide note** | Note that creates a pitch glide; key for 808 basslines | 10 |
| **Snap** | Grid resolution for moving/slicing Playlist clips | 22 |
| **Song mode** | `L`; plays the whole Playlist arrangement | 14, 21 |
| **Sounds** | Browser tab of FL Cloud samples (edition-dependent) | 6, 15 |
| **Stamp tool** | Hand icon / `Alt + C`; places a full chord on a root note | 8 |
| **Step Sequencer** | Right side of the Channel Rack; 16 steps per bar | 2, 27 |
| **Strumize** | `Alt + S`; offsets chord notes into a strum | 8 |
| **Tempo Tapper** | Tap a TAP button in time to estimate BPM | 12 |
| **Templates** | Pre-configured project starting points; File > New from template | 13 |
| **Timbre** | The character/"colour" of a sound | 27 |
| **Turn into automation clip** | `Edit` menu command that converts Event Data to a clip | 24 |
| **Type value** | 2025 field in the Automation Clip node pop-up for precise values | 24 |
| **Velocity** | How hard a note is played; higher = louder | 10, 27 |
| **Velocity pane** | Bottom of the Piano Roll; vertical bars per note | 10 |

---

## Coverage table

| # | Topic | Status | Notes | Est. flashcards | Est. MCQs |
|---|---|---|---|---|---|
| 1 | FL Studio Interface | covered | 5 windows + shortcuts + reset | 6 | 6 |
| 2 | Channel Rack | covered | | 5 | 4 |
| 3 | Sampler Channels | covered | | 4 | 4 |
| 4 | Insert | **thin** | 2 facts; 4 is the ceiling | 4 | 4 |
| 5 | Replace | **thin** | 2 facts + 2 use cases; 4 is the ceiling | 4 | 4 |
| 6 | Browser Panel | covered | | 5 | 4 |
| 7 | Piano Roll | covered ⚠ | Conflicts 1 & 2 (Draw/Paint key, right-click) | 6 | 5 |
| 8 | Chords & Melodies | covered | | 5 | 5 |
| 9 | Piano Roll Tools (Basic) | covered | | 5 | 5 |
| 10 | Notes | covered ⚠ | Conflict 3 (octave shortcut) | 6 | 5 |
| 11 | Piano Roll Tools (Advanced) | **thin** | Vague menu location; overlaps § 9 | 4 | 4 |
| 12 | Tempo Tapper | covered | Small but complete | 4 | 4 |
| 13 | Templates | covered | | 4 | 4 |
| 14 | Make Some Noise | covered | | 5 | 4 |
| 15 | Packs and Sounds | **thin** | Mostly overlaps § 6 | 4 | 4 |
| 16 | Mixer Track Routing | covered | | 5 | 5 |
| 17 | Mixer Track Options | covered | | 5 | 4 |
| 18 | Effects Rack | covered | | 6 | 5 |
| 19 | Mixer Panel Tools | covered | | 5 | 4 |
| 20 | Playlist | covered ⚠ | Conflict 1 (P = Draw here) | 5 | 4 |
| 21 | Patterns To Songs | covered | | 4 | 4 |
| 22 | Playlist Tools | covered | | 5 | 4 |
| 23 | Audio Recording | covered | | 6 | 5 |
| 24 | Recording & Editing Automation | covered | | 6 | 5 |
| 25 | Mixing & Effects | covered | | 6 | 5 |
| 26 | Plugins | covered | | 5 | 5 |
| 27 | Music Theory & Terminology | covered | 25 terms; several repeat other topics | 20 | 15 |
| | **Total (ceiling)** | | | **149** | **131** |

**NOT COVERED IN SOURCE:** none of the 27 listed topics.

## Volume estimate
- **The minimum rule is higher than the targets.** "Every topic ≥ 4 flashcards and ≥ 4 MCQs" × 27 topics = **at least 108 of each**. The 100 / 90 targets are below that floor.
- **The source can support** up to about **149 flashcards / 131 MCQs**. Beyond that you get near-duplicates, especially in thin topics 4, 5, 11 and 15, and in § 27 terms that repeat earlier topics.
- **Proposed counts: 120 flashcards, 110 MCQs.**
  - Thin topics get exactly 4 each.
  - § 27 gets about 16 flashcards and 10 MCQs.
  - The rest are spread over the covered topics.
- **Priority mapping:** 100% (every topic is on the focus list).
