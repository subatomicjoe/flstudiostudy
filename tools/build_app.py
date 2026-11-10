"""Build index.html: notes.md + content/*.json inlined into tools/app_template.html.
Run: python tools/build_app.py   (also writes _test.html, a doctype-wrapped copy for local testing)
"""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SHORT = {1: "Interface", 2: "Channel Rack", 3: "Sampler", 4: "Insert", 5: "Replace", 6: "Browser", 7: "Piano Roll",
         8: "Chords", 9: "PR Tools", 10: "Notes", 11: "PR Generate", 12: "Tempo Tapper", 13: "Templates",
         14: "First Loop", 15: "Packs/Sounds", 16: "Routing", 17: "Track Options", 18: "Effects Rack",
         19: "Mixer Strip", 20: "Playlist", 21: "Pattern→Song", 22: "Playlist Tools", 23: "Recording",
         24: "Automation", 25: "Mixing", 26: "Plugins", 27: "Terms"}
KEY = r"(Shift|Ctrl|Alt/Opt|Alt|Space|F\d{1,2}|[A-Z]|↑/↓|↑|↓)"

def code(s):
    keys = s.split(" + ")
    if all(re.fullmatch(KEY, k) for k in keys):
        return " + ".join(f"<kbd>{k}</kbd>" for k in keys)
    return f"<code>{s}</code>"

def inline(s):
    s = html.escape(s, quote=False)
    parts = re.split(r"`([^`]+)`", s)  # odd indexes are code spans
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(code(p))
        else:
            p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
            p = re.sub(r"(?<![\w*])\*(?!\s)([^*]+?)\*(?!\w)", r"<em>\1</em>", p)
            out.append(p)
    return "".join(out)

LIST = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")

def render_list(items, i):
    ind, ordered = items[i][0], items[i][1]
    out = ["<ol>" if ordered else "<ul>"]
    while i < len(items) and items[i][0] >= ind:
        if items[i][0] == ind:
            out.append("<li>" + inline(items[i][2]))
            i += 1
            if i < len(items) and items[i][0] > ind:
                sub, i = render_list(items, i)
                out.append(sub)
            out.append("</li>")
        else:
            sub, i = render_list(items, i)
            out.append(sub)
    out.append("</ol>" if ordered else "</ul>")
    return "".join(out), i

def md(lines):
    blocks, para, i = [], [], 0
    def flush():
        if para:
            text = " ".join(para)
            m = re.fullmatch(r"\*\*([^*]+)\*\*", text)
            blocks.append(f"<h3>{inline(m.group(1))}</h3>" if m else f"<p>{inline(text)}</p>")
            para.clear()
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            flush(); i += 1
        elif ln.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            blocks.append(f'<div class="tbl"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
        elif ln.startswith(">"):
            flush()
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(re.sub(r"^> ?", "", lines[i])); i += 1
            blocks.append(f'<div class="callout">{md(q)}</div>')
        elif LIST.match(ln):
            flush()
            items = []
            while i < len(lines) and LIST.match(lines[i]):
                m = LIST.match(lines[i])
                items.append((len(m.group(1)), m.group(2)[0].isdigit(), m.group(3))); i += 1
            blocks.append(render_list(items, 0)[0])
        else:
            para.append(ln.strip()); i += 1
    flush()
    # wrap "Common confusions" heading + its list in a panel
    outb, k = [], 0
    while k < len(blocks):
        if blocks[k] == "<h3>Common confusions</h3>" and k + 1 < len(blocks):
            outb.append(f'<div class="confuse">{blocks[k]}{blocks[k + 1]}</div>'); k += 2
        else:
            outb.append(blocks[k]); k += 1
    return "".join(outb)

def parse_notes(text):
    lines = text.splitlines()
    topics, glossary, i = [], [], 0
    while i < len(lines):
        m = re.match(r"^## (\d+)\. (.+)$", lines[i])
        if m:
            n, title = int(m.group(1)), m.group(2).replace("◐", "").strip()
            src = lines[i + 1].strip().strip("*")
            j = lines.index("### Full notes", i) + 1
            k = lines.index("### Quick notes", j)
            full = md(lines[j:k])
            quick, q = [], k + 1
            while q < len(lines) and not lines[q].startswith("---") and not lines[q].startswith("## "):
                if lines[q].startswith("- "):
                    quick.append(inline(lines[q][2:]))
                q += 1
            topics.append({"n": n, "title": title, "short": SHORT[n], "src": src, "full": full, "quick": quick})
            i = q
        elif lines[i] == "## Glossary":
            i += 1
            while i < len(lines) and not lines[i].startswith("## "):
                if lines[i].startswith("|") and not lines[i].startswith("|---") and not lines[i].startswith("| Term"):
                    glossary.append([inline(c.strip()) for c in lines[i].strip().strip("|").split("|")])
                i += 1
        else:
            i += 1
    return topics, glossary

def main():
    topics, glossary = parse_notes(open(os.path.join(ROOT, "notes.md"), encoding="utf-8").read())
    assert [t["n"] for t in topics] == list(range(1, 28)), "expected 27 topics"
    assert all(t["quick"] for t in topics) and glossary
    data = {
        "topics": topics, "glossary": glossary,
        "fc": json.load(open(os.path.join(ROOT, "content", "flashcards.json"), encoding="utf-8")),
        "mcq": json.load(open(os.path.join(ROOT, "content", "mcq.json"), encoding="utf-8")),
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = open(os.path.join(HERE, "app_template.html"), encoding="utf-8").read()
    assert "/*__DATA__*/null" in tpl
    out = tpl.replace("/*__DATA__*/null", blob)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(out)
    test = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"></head><body>' + out + "</body></html>")
    open(os.path.join(ROOT, "_test.html"), "w", encoding="utf-8").write(test)
    print(f"index.html: {len(out.encode()) / 1024:.0f} KB · {len(topics)} topics · {len(glossary)} glossary terms · {len(data['fc'])} cards · {len(data['mcq'])} MCQs")

if __name__ == "__main__":
    main()
