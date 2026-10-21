"""Build index.html for the IELTS grammar book from the content files.

Checks before writing: every pick answer is a valid option, every gap has an accepted answer and exactly one ___,
every spot sentence marks exactly one error, and every unit has a rule, examples and questions.
"""
import html, json, os, re, sys
from content_task1 import TASK1
from content_task2 import TASK2
from content_extra import SPEAKING, MARKING, HUNT, CHEAT

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "index.html")
UNITS = TASK1 + TASK2 + SPEAKING
UID = {u["id"]: n for n, u in enumerate(UNITS, 1)}
problems = []

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


def qa_html(qid, num, q, unit_link=""):
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
    why = q["why"] + (f' <a class="unitref" href="#{q["unit"]}">→ Unit {UID[q["unit"]]}: {html.escape(UNITS[UID[q["unit"]] - 1]["title"])}</a>' if q.get("unit") else "")
    return (f'<div class="qa" id="q-{qid}" data-q="{qid}" data-kind="{kind}" data-acc=\'{html.escape(json.dumps(acc), quote=True)}\'>'
            f'<div class="qq"><span class="qn">{num}</span>{qq}</div>'
            + (f'<div class="qctl">{ctl}</div>' if ctl else "") +
            '<details class="afold"><summary><span class="peek">Show answer</span><span class="res"></span></summary>'
            '<p class="yours" hidden></p>'
            f'<div class="ab">{ans_html}</div><div class="ww"><p><span class="wt">Why</span><br>{why}</p></div></details></div>')


def unit_html(n, u):
    for k in ("rule", "fits", "pairs", "band", "qs", "remember"):
        if not u.get(k):
            problems.append(f"{u['id']}: missing {k}")
    fits = "".join(f'<tr><td class="k">{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in u["fits"])
    pairs = "".join(f'<div class="pair"><p class="wr"><span class="mk">✗</span> {html.escape(w)}</p>'
                    f'<p class="rt"><span class="mk">✓</span> {r}</p><p class="pw">{y}</p></div>' for w, r, y in u["pairs"])
    b7, b9, note = u["band"]
    qs = "".join(qa_html(f'{u["id"]}-{i}', i, q) for i, q in enumerate(u["qs"], 1))
    return (f'<div class="sheetpage" id="{u["id"]}"><div class="pat-head"><span class="pnum">UNIT {n}</span>'
            f'<span class="ptype">{html.escape(u["where"])}</span><div class="pat-title">{html.escape(u["title"])}</div></div>'
            f'<div class="box tech"><span class="lab">The rule</span>{u["rule"]}</div>'
            f'<h3>Where it fits</h3><div class="tablewrap"><table><tr><th>Situation</th><th>Use</th><th>Example</th></tr>{fits}</table></div>'
            f'<div class="box rw"><span class="lab">Right and wrong</span>{pairs}</div>'
            f'<div class="box same"><span class="lab">Band 7 → band 9</span>'
            f'<p class="b7"><span class="bt">BAND 7</span> {html.escape(b7)}</p><p class="b9"><span class="bt">BAND 9</span> {html.escape(b9)}</p>'
            f'<p class="small">{note}</p></div>'
            f'<h3>Check yourself</h3>{qs}'
            f'<div class="actions"><button type="button" class="ghost sm" data-showall="{u["id"]}">Show all answers</button>'
            f'<button type="button" class="ghost sm" data-clear="{u["id"]}">Clear my answers</button></div>'
            f'<div class="box get"><span class="lab">Remember</span><p>{u["remember"]}</p></div></div>')


# ---------------------------------------------------------------- pages
def toc_row(href, n, t, cc="", st=""):
    cc = f' <span class="cc">· {cc}</span>' if cc else ""
    sid = f' id="{st}"' if st else ""
    return f'<a href="#{href}"><span class="n">{n}</span><span class="t">{t}{cc}</span><span class="st"{sid}></span></a>'


groups = [("Task 1 · charts, tables and processes", TASK1), ("Task 2 · essays", TASK2), ("Speaking", SPEAKING)]
toc = ['<div class="grp">Part 1 · How grammar is marked</div>', toc_row("marking", "1", "Range, accuracy and the three rules for band 8+")]
toc.append('<div class="grp">Part 2 · The 24 units</div>')
for label, us in groups:
    toc.append(f'<div class="sub">{label}</div>')
    for u in us:
        toc.append(toc_row(u["id"], f'UNIT {UID[u["id"]]}', html.escape(u["title"]), html.escape(u["where"]), "toc-" + u["id"]))
toc += ['<div class="grp">Part 3 · Error hunt</div>', toc_row("hunt", "3", "24 sentences, one error each", "find your own top five errors", "toc-hunt"),
        '<div class="grp">Part 4 · Cheat sheet</div>', toc_row("cheat", "4", "Which structure goes where, on one page")]

cover = ('<div class="sheetpage" id="start"><div class="cover"><div class="bar"></div>'
         '<span class="pnum" style="margin-bottom:18px">IELTS WRITING &amp; SPEAKING · BAND 7 TO 9</span>'
         '<h1>IELTS Grammar<br>What Goes Where</h1>'
         '<div class="sub">24 units · 96 questions · a 24-sentence error hunt · every answer explained under its question</div>'
         '<ul><li>Not a grammar encyclopedia. Only the grammar that moves your band in <b>Task 1</b>, <b>Task 2</b> and <b>Speaking</b>, '
         'and for each point, <b>exactly where in the test it belongs</b>.</li>'
         '<li>Every unit gives the rule, where it fits, right and wrong pairs, a band 7 sentence beside a band 9 sentence, then four questions. '
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

part2_open = ('<div class="sheetpage"><div class="part"><h1>Part 2 · The 24 units</h1><div class="blurb">Units 1–8 are for Task 1, '
              'units 9–22 for Task 2 (most of them also help in Speaking), and units 23–24 for Speaking.</div></div>'
              '<div class="tablewrap"><table><tr><th>Units</th><th>Where</th><th>What they fix</th></tr>'
              '<tr><td class="k">1–8</td><td>Task 1</td><td>Tenses for dates, the passive in processes, prepositions of change, comparisons, data nouns, numbers, articles</td></tr>'
              '<tr><td class="k">9–22</td><td>Task 2</td><td>Articles, countable nouns, agreement, relative clauses, conditionals, hedging, linkers, sentence boundaries, noun phrases, participles, verb patterns, parallelism, emphasis</td></tr>'
              '<tr><td class="k">23–24</td><td>Speaking</td><td>Natural tenses, <i>used to</i>, wishes, word order and indirect questions</td></tr></table></div></div>')
units_html = "".join(unit_html(UID[u["id"]], u) for u in UNITS)

hunt_qs = "".join(qa_html(f"h-{i}", i, q) for i, q in enumerate(HUNT, 1))
part3 = ('<div class="sheetpage" id="hunt"><div class="part"><h1>Part 3 · Error hunt</h1>'
         '<div class="blurb">Twenty-four sentences, one error each, all of the kind that keep band-7 scripts at band 7. '
         'Tap the wrong part, then check. Each answer links back to its unit.</div></div>'
         '<div class="box tech"><span class="lab">How to use it</span><p>Do all 24 before opening any answers. Every one you miss is a habit, '
         'and that is your personal checklist for the last three minutes of the Writing test.</p></div>'
         + hunt_qs +
         '<div class="actions"><button type="button" class="ghost sm" data-showall="hunt">Show all answers</button>'
         '<button type="button" class="ghost sm" data-clear="hunt">Clear my answers</button></div><div id="huntscore"></div></div>')

cheat_rows = "".join(f'<tr><td class="k">{a}</td><td>{b}</td><td>{c}</td><td><a href="#{u}">Unit {UID[u]}</a></td></tr>' for a, b, c, u in CHEAT)
part4 = ('<div class="sheetpage" id="cheat"><div class="part"><h1>Part 4 · Which structure goes where</h1>'
         '<div class="blurb">The whole book on one page. Read it the night before the test.</div></div>'
         '<div class="tablewrap"><table><tr><th>Where</th><th>Structure</th><th>Example</th><th>Unit</th></tr>' + cheat_rows + '</table></div>'
         '<div class="box get"><span class="lab">The last three minutes of Writing</span><ol>'
         '<li>Every verb: does it agree with its subject, and does its tense match the time?</li>'
         '<li>Every noun: <i>a / the / nothing</i>? Countable or not?</li>'
         '<li>Every comma: is it joining two full sentences? (Then it is a splice.)</li>'
         '<li>Your own top errors from the Error Hunt.</li></ol></div></div>')

if problems:
    print("PROBLEMS:")
    for p in problems:
        print("  -", p)
    sys.exit(1)

css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
js = open(os.path.join(HERE, "app.js"), encoding="utf-8").read()
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="description" content="IELTS grammar for Writing and Speaking: 24 units on which structure goes where, with 120 questions and every answer explained.">\n'
        '<title>IELTS Grammar Lab</title>\n<style>\n' + css + '</style>\n</head>\n<body>\n<main id="view">\n'
        + cover + part1 + part2_open + units_html + part3 + part4 +
        '\n</main>\n<a class="totop" id="totop" href="#contents" hidden>↑ Contents</a>\n<script>\n' + js + '\n</script>\n</body>\n</html>\n')
open(OUT, "w", encoding="utf-8").write(page)
n_q = sum(len(u["qs"]) for u in UNITS)
print(f"OK  {len(UNITS)} units, {n_q} unit questions + {len(HUNT)} error-hunt sentences = {n_q + len(HUNT)} questions")
print(f"OK  page written: {len(page) // 1024} KB")
