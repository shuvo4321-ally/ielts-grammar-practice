# IELTS Grammar: What Goes Where

An interactive grammar book for IELTS **Writing and Speaking**. It covers only the grammar that moves your band, and for each point it shows **exactly where in the test it belongs**. It has the same look as the IELTS Reading and Listening practice pages.

**Open it:** https://shuvo4321-ally.github.io/ielts-grammar-practice/

## What's inside

It is one continuous page. The Contents on the cover jumps to any unit.

| Part | What it is |
|---|---|
| **1 How grammar is marked** | Range vs accuracy, what band 6, 7, 8 and 9 grammar looks like in plain words, and three rules for band 8+. |
| **2 The 24 units** | Units 1–8 for Task 1 (tenses for dates, the passive in processes, prepositions of change, comparisons, data nouns, numbers, articles). Units 9–22 for Task 2 (articles, countable nouns, agreement, relative clauses, conditionals, hedging, linkers, sentence boundaries, noun phrases, participle clauses, verb patterns, parallel structure, emphasis). Units 23–24 for Speaking. |
| **3 Error hunt** | 24 sentences with one error each. Find yours, and the page builds your personal checklist with links back to the units. |
| **4 Cheat sheet** | Which structure goes where, on one page, plus a last-three-minutes checklist for Writing. |

Each unit has five parts: **the rule**, **where it fits** in the test, **right and wrong** pairs, a **band 7 sentence beside a band 9 sentence**, and **four questions**.

## Using it

- **Pick:** tap the correct option.
- **Type:** fill the gap in the sentence.
- **Spot the error:** tap the word that is wrong.
- **Show answer** under each question tells you whether you were right, shows the answer, and explains why.
- Your answers and progress (per unit and in the error hunt) are saved in this browser only.

## Rebuilding the page

```bash
cd src
python build.py
```

The build checks every question before it writes `index.html`:
- every pick answer is one of its options,
- every gap has exactly one blank and at least one accepted answer,
- every error-hunt sentence marks exactly one error.

| File | Contents |
|---|---|
| `src/content_task1.py` | Units 1–8 (Task 1) |
| `src/content_task2.py` | Units 9–22 (Task 2) |
| `src/content_extra.py` | Units 23–24 (Speaking), the marking guide, the error hunt and the cheat sheet |
| `src/build.py` | Builds and checks the page |
| `src/style.css`, `src/app.js` | Page styles and the answering, marking and saving logic |

## Note

All explanations, examples and questions are original material written for this project. The band summaries paraphrase the public IELTS band descriptors in plain words and are not the official wording. IELTS is a registered trademark of the British Council, IDP: IELTS Australia and Cambridge University Press & Assessment, which are not connected with this project.
