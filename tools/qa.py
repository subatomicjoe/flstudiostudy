"""QA for content/flashcards.json and content/mcq.json. Run: python tools/qa.py [--samples]"""
import json, os, sys, random, re
from collections import Counter
from difflib import SequenceMatcher

ROOT = os.path.join(os.path.dirname(__file__), "..", "content")
fcs = json.load(open(os.path.join(ROOT, "flashcards.json"), encoding="utf-8"))
mcqs = json.load(open(os.path.join(ROOT, "mcq.json"), encoding="utf-8"))
PRIORITY = set(range(1, 28))  # the source's 27 focus topics
MIN = 4
errors = []

def sentences(t):
    t = t.replace("e.g.", "eg").replace("i.e.", "ie").replace("...", "")
    return len(re.findall(r"[.!?](\s|$)", t))

def tnum(item):
    m = re.match(r"(\d+) ", item.get("topic", ""))
    return int(m.group(1)) if m else None

# schema
for c in fcs:
    if set(c) != {"id", "topic", "front", "back", "source"}: errors.append(f"{c.get('id')}: wrong keys")
    if not all(isinstance(c.get(k), str) and c.get(k).strip() for k in ("id", "topic", "front", "back", "source")): errors.append(f"{c.get('id')}: empty field")
    if not c.get("source", "").startswith("§ "): errors.append(f"{c['id']}: source missing §")
    if sentences(c["back"]) > 3: errors.append(f"{c['id']}: back over 3 sentences")
for q in mcqs:
    if set(q) != {"id", "topic", "question", "options", "answer", "explanation", "source"}: errors.append(f"{q.get('id')}: wrong keys")
    o = q.get("options", [])
    if not (isinstance(o, list) and len(o) == 4 and all(isinstance(x, str) and x.strip() for x in o)): errors.append(f"{q['id']}: needs 4 options")
    if len(set(x.lower() for x in o)) != 4: errors.append(f"{q['id']}: duplicate options")
    if q.get("answer") not in (0, 1, 2, 3): errors.append(f"{q['id']}: bad answer index")
    if any(re.search(r"\b(all|none) of the above\b", x, re.I) for x in o): errors.append(f"{q['id']}: all/none of the above")
    if not q.get("source", "").startswith("§ "): errors.append(f"{q['id']}: source missing §")
    if sentences(q["explanation"]) > 2: errors.append(f"{q['id']}: explanation over 2 sentences")
for bank in (fcs, mcqs):
    ids = Counter(x["id"] for x in bank)
    errors += [f"duplicate id {i}" for i, n in ids.items() if n > 1]
    errors += [f"{x['id']}: topic not recognised" for x in bank if tnum(x) not in PRIORITY]

# near-duplicates within each bank
def norm(s): return re.sub(r"[^a-z0-9 ]", "", s.lower())
dups = []
# compare question + answer, so two different facts asked the same way don't count
text = lambda x: norm(x["front"] + " " + x["back"]) if "front" in x else norm(x["question"] + " " + x["options"][x["answer"]])
for bank in (fcs, mcqs):
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            r = SequenceMatcher(None, text(bank[i]), text(bank[j])).ratio()
            if r > 0.8: dups.append((bank[i]["id"], bank[j]["id"], round(r, 2)))

fc_per = Counter(tnum(c) for c in fcs)
mq_per = Counter(tnum(q) for q in mcqs)
short = [t for t in sorted(PRIORITY) if fc_per[t] < MIN or mq_per[t] < MIN]
pct = lambda n, d: f"{100 * n / d:.1f}%"
ans = Counter(q["answer"] for q in mcqs)
longest = [q["id"] for q in mcqs if all(len(q["options"][q["answer"]]) > len(x) for k, x in enumerate(q["options"]) if k != q["answer"])]

print(f"Flashcards: {len(fcs)}   MCQs: {len(mcqs)}")
print("\nPer topic (flashcards / MCQs), minimum 4 each:")
for t in sorted(PRIORITY):
    flag = "" if fc_per[t] >= MIN and mq_per[t] >= MIN else "   <-- BELOW MINIMUM"
    print(f"  {t:>2}  {fc_per[t]:>2} / {mq_per[t]:>2}{flag}")
print(f"\nMapped to priority topics: flashcards {pct(sum(fc_per[t] for t in PRIORITY), len(fcs))}, MCQs {pct(sum(mq_per[t] for t in PRIORITY), len(mcqs))}")
print("Correct-answer index: " + ", ".join(f"{k}={ans[k]} ({pct(ans[k], len(mcqs))})" for k in range(4)))
print(f"Correct option strictly longest: {len(longest)}/{len(mcqs)} = {pct(len(longest), len(mcqs))} (limit < 35%)")
print(f"Near-duplicate pairs (similarity > 0.8): {len(dups)}" + ("".join(f"\n  {a} ~ {b} ({r})" for a, b, r in dups)))
print(f"Schema / rule errors: {len(errors)}" + "".join(f"\n  {e}" for e in errors))

ok = not errors and not short and not dups and len(longest) / len(mcqs) < 0.35
print("\nRESULT:", "PASS" if ok else "FAIL")

if "--samples" in sys.argv:
    rnd = random.Random(15112026)
    print("\n=== 10 random MCQs ===")
    for q in rnd.sample(mcqs, 10):
        print(f"\n[{q['id']}] {q['question']}")
        for k, x in enumerate(q["options"]): print(f"   {'ABCD'[k]}. {x}{'   ✓' if k == q['answer'] else ''}")
        print(f"   Why: {q['explanation']}\n   {q['source']}")
    print("\n=== 10 random flashcards ===")
    for c in rnd.sample(fcs, 10):
        print(f"\n[{c['id']}] {c['front']}\n   → {c['back']}\n   {c['source']}")
sys.exit(0 if ok else 1)
