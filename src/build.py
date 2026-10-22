"""Build index.html for the IELTS grammar and spelling book from the content files.

Checks before writing: every pick answer is a valid option, every gap has an accepted answer and exactly one ___,
every spot sentence marks exactly one error, every unit has a rule, examples and questions, and every error-hunt
sentence points at a real unit.
"""
import html, json, os, re, sys
from content_task1 import TASK1
from content_task2 import TASK2
from content_extra import SPEAKING, MARKING, HUNT, CHEAT
from additions import ADD, MORE_HUNT
from content_spelling import INTRO, SPELLING, SHUNT, SPELL_CHEAT

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "index.html")
GRAMMAR = TASK1 + TASK2 + SPEAKING
problems = []

# ---------------------------------------------------------------- merge the extra examples into the grammar units
for u in GRAMMAR:
    extra = ADD.get(u["id"])
    if not extra:
        problems.append(f"{u['id']}: no extra examples in additions.py")
        continue
    u["pairs"] = u["pairs"] + extra["pairs"]
    u["bands"] = [u["band"]] + extra["bands"]
    u["qs"] = u["qs"] + extra["qs"]
for u in SPELLING:
    u["bands"] = []
HUNT = HUNT + MORE_HUNT

UNITS = GRAMMAR + SPELLING
LABEL = {}
for n, u in enumerate(GRAMMAR, 1):
    LABEL[u["id"]] = ("Unit", n)
for n, u in enumerate(SPELLING, 1):
    LABEL[u["id"]] = ("Spelling", n)
BY_ID = {u["id"]: u for u in UNITS}

TOKEN = re.compile(r"\[\[.+?\]\]|[\w’'%°$£€-]+|[^\s\w]")
NO_SPACE_BEFORE = set(",.;:!?)%")


def tokens(sentence):
    """Split a spot sentence into tappable word tokens. A multi-word error is split like any other words,
    so the layout gives nothing away; tapping any word of it counts. Returns (html, error token indices, error text)."""
    out, err, err_text, i = [], [], "", 0
    for t in TOKEN.findall(sentence):
        is_err = t.startswith("[[")
        words = re.findall(r"[\w’'%°$£€-]+|[^\s\w]", t[2:-2]) if is_err else [t]
        if is_err:
            err_text = t[2:-2]
        for w in words:
            if is_err:
                err.append(i)
            sp = "" if (i == 0 or w[0] in NO_SPACE_BEFORE) else " "
            out.append(f'{sp}<button type="button" class="tok" data-t="{i}">{html.escape(w)}</button>')
            i += 1
    return "".join(out), err, err_text


def qa_html(qid, num, q):
    kind, stem = q["kind"], q["stem"]
    acc, ans_html, ctl, qq = None, "", "", ""
    if kind == "pick":
        if not (0 <= q["ans"] < len(q["opts"])):
            problems.append(f"{qid}: answer index out of range")
        acc = q["ans"]
        qq = stem.replace("___", '<span class="blank">______</span>')
        ctl = "".join(f'<button type="button" class="ch opt" data-v="{i}">{html.escape(o)}</button>' for i, o in enumerate(q["opts"]))
        ans_html = f'<span class="ansv">{html.escape(q["opts"][q["ans"]])}</span>'
    elif kind == "gap":
        if stem.count("___") != 1 or not q.get("acc"):
            problems.append(f"{qid}: a gap question needs exactly one ___ and an accepted answer")
        acc = q["acc"]
        a, b = stem.split("___", 1)
        qq = a + '<input class="ain gapin" type="text" autocomplete="off" spellcheck="false" aria-label="Your answer">' + b
        ans_html = f'<span class="ansv">{html.escape(q["acc"][0])}</span>' + (
            f'<span class="alsos">also accepted: {html.escape(", ".join(q["acc"][1:]))}</span>' if len(q["acc"]) > 1 else "")
    elif kind == "spot":
        toks, err, err_text = tokens(stem)
        if not err or stem.count("[[") != 1:
            problems.append(f"{qid}: spot sentence must mark exactly one error")
        acc = err
        qq = '<span class="spothint">Tap the part that is wrong.</span>'
        ctl = f'<div class="toks">{toks}</div>'
        ans_html = (f'<p class="wrongpart">Wrong: <b>{html.escape(err_text)}</b></p>'
                    f'<p class="fixline"><span class="ok">✓</span> {html.escape(q["fix"])}</p>')
    else:
        problems.append(f"{qid}: unknown kind {kind}")
    why = q["why"]
    if q.get("unit"):
        if q["unit"] not in LABEL:
            problems.append(f"{qid}: unknown unit {q['unit']}")
        else:
            kind_l, n = LABEL[q["unit"]]
            why += f' <a class="unitref" href="#{q["unit"]}">→ {kind_l} {n}: {html.escape(BY_ID[q["unit"]]["title"])}</a>'
    return (f'<div class="qa" id="q-{qid}" data-q="{qid}" data-kind="{kind}" data-acc=\'{html.escape(json.dumps(acc), quote=True)}\'>'
            f'<div class="qq"><span class="qn">{num}</span>{qq}</div>'
            + (f'<div class="qctl">{ctl}</div>' if ctl else "") +
            '<details class="afold"><summary><span class="peek">Show answer</span><span class="res"></span></summary>'
            '<p class="yours" hidden></p>'
            f'<div class="ab">{ans_html}</div><div class="ww"><p><span class="wt">Why</span><br>{why}</p></div></details></div>')


def unit_html(u):
    label, n = LABEL[u["id"]]
    for k in ("rule", "fits", "pairs", "qs", "remember"):
        if not u.get(k):
            problems.append(f"{u['id']}: missing {k}")
    if not u["bands"] and not u.get("tricks"):
        problems.append(f"{u['id']}: needs band examples or memory tricks")
    head = u.get("fits_head", ("Situation", "Use", "Example"))
    fits = "".join(f'<tr><td class="k">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in u["fits"])
    pairs = "".join(f'<div class="pair"><p class="wr"><span class="mk">✗</span> {html.escape(w)}</p>'
                    f'<p class="rt"><span class="mk">✓</span> {r}</p><p class="pw">{y}</p></div>' for w, r, y in u["pairs"])
    bands = "".join(f'<div class="bandex"><p class="b7"><span class="bt">BAND 7</span> {html.escape(b7)}</p>'
                    f'<p class="b9"><span class="bt">BAND 9</span> {html.escape(b9)}</p><p class="small">{note}</p></div>' for b7, b9, note in u["bands"])
    bands_box = f'<div class="box same"><span class="lab">Band 7 → band 9</span>{bands}</div>' if bands else ""
    tricks_box = ('<div class="box same"><span class="lab">Memory tricks</span><ul>' + "".join(f"<li>{t}</li>" for t in u["tricks"]) + '</ul></div>') if u.get("tricks") else ""
    qs = "".join(qa_html(f'{u["id"]}-{i}', i, q) for i, q in enumerate(u["qs"], 1))
    return (f'<div class="sheetpage unit" id="{u["id"]}"><div class="pat-head"><span class="pnum">{label.upper()} {n}</span>'
            f'<span class="ptype">{html.escape(u["where"])}</span><div class="pat-title">{html.escape(u["title"])}</div></div>'
            f'<div class="box tech"><span class="lab">The rule</span>{u["rule"]}</div>'
            f'<h3>{"The words" if u.get("fits_head") else "Where it fits"}</h3><div class="tablewrap"><table><tr><th>{head[0]}</th><th>{head[1]}</th><th>{head[2]}</th></tr>{fits}</table></div>'
            f'<div class="box rw"><span class="lab">Right and wrong</span>{pairs}</div>'
            f'{bands_box}{tricks_box}'
            f'<h3>Check yourself</h3>{qs}'
            f'<div class="actions"><button type="button" class="ghost sm" data-showall="{u["id"]}">Show all answers</button>'
            f'<button type="button" class="ghost sm" data-clear="{u["id"]}">Clear my answers</button></div>'
            f'<div class="box get"><span class="lab">Remember</span><p>{u["remember"]}</p></div></div>')


# ---------------------------------------------------------------- pages
def toc_row(href, n, t, cc="", st=""):
    cc = f' <span class="cc">· {cc}</span>' if cc else ""
    sid = f' id="{st}"' if st else ""
    return f'<a href="#{href}"><span class="n">{n}</span><span class="t">{t}{cc}</span><span class="st"{sid}></span></a>'


n_g, n_s = len(GRAMMAR), len(SPELLING)
n_gq = sum(len(u["qs"]) for u in GRAMMAR)
n_sq = sum(len(u["qs"]) for u in SPELLING)
n_total = n_gq + n_sq + len(HUNT) + len(SHUNT)

groups = [("Task 1 · charts, tables and processes", TASK1), ("Task 2 · essays", TASK2), ("Speaking", SPEAKING)]
toc = ['<div class="grp">Part 1 · How grammar is marked</div>', toc_row("marking", "1", "Range, accuracy and the three rules for band 8+")]
toc.append(f'<div class="grp">Part 2 · The {n_g} grammar units</div>')
for label, us in groups:
    toc.append(f'<div class="sub">{label}</div>')
    for u in us:
        toc.append(toc_row(u["id"], f'UNIT {LABEL[u["id"]][1]}', html.escape(u["title"]), html.escape(u["where"]), "toc-" + u["id"]))
toc.append(f'<div class="grp">Part 3 · Spelling technique</div>')
toc.append(toc_row("spelling", "3", "Why spelling matters, and how to practise it"))
for u in SPELLING:
    toc.append(toc_row(u["id"], f'SPELLING {LABEL[u["id"]][1]}', html.escape(u["title"]), html.escape(u["where"]), "toc-" + u["id"]))
toc += ['<div class="grp">Part 4 · Error hunts</div>',
        toc_row("hunt", "4a", f"Grammar: {len(HUNT)} sentences, one error each", "find your own top errors", "toc-hunt"),
        toc_row("shunt", "4b", f"Spelling: {len(SHUNT)} sentences, one misspelled word each", "", "toc-shunt"),
        '<div class="grp">Part 5 · Cheat sheet</div>', toc_row("cheat", "5", "Which structure goes where, and the spelling rules, on one page")]

cover = ('<div class="sheetpage" id="start"><div class="cover"><div class="bar"></div>'
         '<span class="pnum" style="margin-bottom:18px">IELTS WRITING, SPEAKING &amp; SPELLING · BAND 7 TO 9</span>'
         '<h1>IELTS Grammar<br>What Goes Where</h1>'
         f'<div class="sub">{n_g} grammar units · {n_s} spelling units · {n_total} questions · two error hunts · every answer explained under its question</div>'
         '<ul><li>Not a grammar encyclopedia. Only the grammar that moves your band in <b>Task 1</b>, <b>Task 2</b> and <b>Speaking</b>, '
         'and for each point, <b>exactly where in the test it belongs</b>. Then the <b>spelling</b> technique that protects your marks in Listening, Reading and Writing.</li>'
         '<li>Every unit gives the rule, where it fits, six right and wrong pairs, band 7 sentences beside band 9 sentences, then eight questions. '
         'The answer and the reason are folded directly underneath each one.</li>'
         '<li>It is all one page: scroll through it like a book, or jump from the Contents below. Your answers are saved in this browser only.</li></ul></div>'
         '<div class="toc" id="contents"><h2>Contents</h2>' + "".join(toc) + '</div></div>')

bands = "".join(f'<tr><td class="k">Band {b}</td><td>{d}</td></tr>' for b, d in MARKING["bands"])
rules = "".join(f'<li><b>{a}</b> {b}</li>' for a, b in MARKING["rules"])
part1 = ('<div class="sheetpage" id="marking"><div class="part"><h1>Part 1 · How grammar is marked</h1>'
         '<div class="blurb">Read this once. It decides how you use everything after it.</div></div>'
         + MARKING["intro"] +
         '<div class="tablewrap"><table><tr><th>Band</th><th>What the grammar looks like (in plain words)</th></tr>' + bands + '</table></div>'
         '<p class="small">A plain-English summary of the public band descriptors for grammatical range and accuracy, not the official wording.</p>'
         '<div class="box tech"><span class="lab">Three rules for band 8+</span><ol>' + rules + '</ol></div>'
         '<h3>How to use this book</h3>' + MARKING["how"] + '</div>')

part2_open = (f'<div class="sheetpage"><div class="part"><h1>Part 2 · The {n_g} grammar units</h1><div class="blurb">Units 1–8 are for Task 1, '
              'units 9–22 for Task 2 (most of them also help in Speaking), and units 23–24 for Speaking.</div></div>'
              '<div class="tablewrap"><table><tr><th>Units</th><th>Where</th><th>What they fix</th></tr>'
              '<tr><td class="k">1–8</td><td>Task 1</td><td>Tenses for dates, the passive in processes, prepositions of change, comparisons, data nouns, numbers, articles</td></tr>'
              '<tr><td class="k">9–22</td><td>Task 2</td><td>Articles, countable nouns, agreement, relative clauses, conditionals, hedging, linkers, sentence boundaries, noun phrases, participles, verb patterns, parallelism, emphasis</td></tr>'
              '<tr><td class="k">23–24</td><td>Speaking</td><td>Natural tenses, <i>used to</i>, wishes, word order and indirect questions</td></tr></table></div></div>')
grammar_html = "".join(unit_html(u) for u in GRAMMAR)

spell_table = "".join(f'<tr><td class="k">{a}</td><td>{b}</td></tr>' for a, b in INTRO["table"])
how = "".join(f"<li><b>{a}</b> {b}</li>" for a, b in INTRO["how"])
part3_open = ('<div class="sheetpage" id="spelling"><div class="part"><h1>Part 3 · Spelling technique</h1>'
              '<div class="blurb">A misspelled word in Listening or Reading is a lost mark, however well you understood it.</div></div>'
              + INTRO["why"] + '<div class="tablewrap"><table><tr><th>Paper</th><th>How spelling counts</th></tr>' + spell_table + '</table></div>'
              + INTRO["both"] + '<div class="box tech"><span class="lab">How to practise spelling</span><ol>' + how + '</ol></div>'
              f'<p class="small">Seven short units follow, each in the same shape as the grammar units, then a {len(SHUNT)}-sentence spelling hunt.</p></div>')
spelling_html = "".join(unit_html(u) for u in SPELLING)


def hunt_html(hid, prefix, title, blurb, use, items):
    qs = "".join(qa_html(f"{prefix}-{i}", i, q) for i, q in enumerate(items, 1))
    return (f'<div class="sheetpage hunt" id="{hid}"><div class="part"><h1>{title}</h1><div class="blurb">{blurb}</div></div>'
            f'<div class="box tech"><span class="lab">How to use it</span><p>{use}</p></div>' + qs +
            f'<div class="actions"><button type="button" class="ghost sm" data-showall="{hid}">Show all answers</button>'
            f'<button type="button" class="ghost sm" data-clear="{hid}">Clear my answers</button></div><div class="huntscore"></div></div>')


part4 = (hunt_html("hunt", "h", "Part 4a · Grammar error hunt",
                   f"{len(HUNT)} sentences, one error each, all of the kind that keep band-7 scripts at band 7. Tap the wrong part, then check. Each answer links back to its unit.",
                   f"Do all {len(HUNT)} before opening any answers. Every one you miss is a habit, and that is your personal checklist for the last three minutes of the Writing test.", HUNT)
         + hunt_html("shunt", "sh", "Part 4b · Spelling error hunt",
                     f"{len(SHUNT)} sentences, one misspelled word each. Tap the misspelled word, then check. Each answer links back to its spelling unit.",
                     "Do them all before checking. The words you miss go straight onto your personal list of ten.", SHUNT))

cheat_rows = "".join(f'<tr><td class="k">{a}</td><td>{b}</td><td>{c}</td><td><a href="#{u}">{LABEL[u][0]} {LABEL[u][1]}</a></td></tr>' for a, b, c, u in CHEAT + SPELL_CHEAT)
part5 = ('<div class="sheetpage" id="cheat"><div class="part"><h1>Part 5 · Which structure goes where</h1>'
         '<div class="blurb">The whole book on one page. Read it the night before the test.</div></div>'
         '<div class="tablewrap"><table><tr><th>Where</th><th>Structure or rule</th><th>Example</th><th>Unit</th></tr>' + cheat_rows + '</table></div>'
         '<div class="box get"><span class="lab">The last three minutes of Writing</span><ol>'
         '<li>Every verb: does it agree with its subject, and does its tense match the time?</li>'
         '<li>Every noun: <i>a / the / nothing</i>? Countable or not?</li>'
         '<li>Every comma: is it joining two full sentences? (Then it is a splice.)</li>'
         '<li>Spelling: read your essay backwards, one sentence at a time, and check your own list of ten words.</li>'
         '<li>Colour and centre, or color and center: one variety only.</li></ol></div></div>')

if problems:
    print("PROBLEMS:")
    for p in problems:
        print("  -", p)
    sys.exit(1)

css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
js = open(os.path.join(HERE, "app.js"), encoding="utf-8").read()
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<meta name="description" content="IELTS grammar and spelling for Writing, Speaking, Listening and Reading: {n_g} grammar units and {n_s} spelling units on which structure goes where, with {n_total} questions and every answer explained.">\n'
        '<title>IELTS Grammar Lab</title>\n<style>\n' + css + '</style>\n</head>\n<body>\n<main id="view">\n'
        + cover + part1 + part2_open + grammar_html + part3_open + spelling_html + part4 + part5 +
        '\n</main>\n<a class="totop" id="totop" href="#contents" hidden>↑ Contents</a>\n<script>\n' + js + '\n</script>\n</body>\n</html>\n')
open(OUT, "w", encoding="utf-8").write(page)
print(f"OK  {n_g} grammar units ({n_gq} questions), {n_s} spelling units ({n_sq} questions), "
      f"hunts of {len(HUNT)} + {len(SHUNT)} = {n_total} questions in all")
print(f"OK  page written: {len(page) // 1024} KB")
