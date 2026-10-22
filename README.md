# IELTS Grammar and Spelling: What Goes Where

An interactive grammar and spelling book for IELTS **Writing, Speaking, Listening and Reading**. It covers only the points that move your band, and for each one it shows **exactly where in the test it belongs**. It has the same look as the IELTS Reading and Listening practice pages.

**Open it:** https://shuvo4321-ally.github.io/ielts-grammar-practice/

## What's inside

It is one continuous page. The Contents on the cover jumps to any unit.

| Part | What it is |
|---|---|
| **1 How grammar is marked** | Range vs accuracy, what band 6, 7, 8 and 9 grammar looks like in plain words, and three rules for band 8+. |
| **2 The 24 grammar units** | Units 1–8 for Task 1 (tenses for dates, the passive in processes, prepositions of change, comparisons, data nouns, numbers, articles). Units 9–22 for Task 2 (articles, countable nouns, agreement, relative clauses, conditionals, hedging, linkers, sentence boundaries, noun phrases, participle clauses, verb patterns, parallel structure, emphasis). Units 23–24 for Speaking. |
| **3 Spelling technique** | Why spelling matters in each paper, how to practise, and seven units: doubling the last letter, the silent e, plurals and y → ies, ie/ei and silent letters, words that sound alike, the most common IELTS misspellings with memory tricks, and British vs American spelling. |
| **4 Error hunts** | A grammar hunt (40 sentences, one error each) and a spelling hunt (20 sentences, one misspelled word each). Each builds your personal checklist with links back to the units. |
| **5 Cheat sheet** | Which structure goes where, plus the spelling rules, on one page, and a last-three-minutes checklist for Writing. |

Each grammar unit has: **the rule**, **where it fits** in the test, **six right and wrong pairs**, **two band 7 → band 9 examples**, and **eight questions**. Each spelling unit has the rule, six pairs, memory tricks and eight questions.

In total there are **308 questions**.

## Using it

- **Pick:** tap the correct option.
- **Type:** fill the gap in the sentence.
- **Spot the error:** tap the word that is wrong.
- **Show answer** under each question tells you whether you were right, shows the answer, and explains why.
- Your answers and progress (per unit and in both error hunts) are saved in this browser only.

## Rebuilding the page

```bash
cd src
python build.py
```

The build checks every question before it writes `index.html`:
- every pick answer is one of its options,
- every gap has exactly one blank and at least one accepted answer,
- every error-hunt sentence marks exactly one error and points to a real unit.

| File | Contents |
|---|---|
| `src/content_task1.py` | Units 1–8 (Task 1) |
| `src/content_task2.py` | Units 9–22 (Task 2) |
| `src/content_extra.py` | Units 23–24 (Speaking), the marking guide, the first 24 error-hunt sentences and the cheat sheet |
| `src/additions.py` | The extra pairs, band examples and questions for every grammar unit, and the other 16 error-hunt sentences |
| `src/content_spelling.py` | The spelling intro, seven spelling units, the spelling hunt and its cheat-sheet rows |
| `src/build.py` | Merges and checks the content, then builds the page |
| `src/style.css`, `src/app.js` | Page styles and the answering, marking and saving logic |

## Note

All explanations, examples and questions are original material written for this project. The band summaries paraphrase the public IELTS band descriptors in plain words and are not the official wording. IELTS is a registered trademark of the British Council, IDP: IELTS Australia and Cambridge University Press & Assessment, which are not connected with this project.
