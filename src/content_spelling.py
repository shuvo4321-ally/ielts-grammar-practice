"""Part 3: spelling technique. Seven units in the same format as the grammar units, plus an intro, a hunt and cheat-sheet rows."""
from content_task1 import Q

INTRO = dict(
    why="""<p>Spelling is marked differently in each paper, and in two of them one slip costs a whole mark.</p>""",
    table=[("Listening", "A misspelled answer is <b>wrong</b>, even when you heard the right word. One slip = one lost mark."),
           ("Reading", "The same. Copy words from the passage <b>exactly</b>, including hyphens and plurals."),
           ("Writing", "Spelling is part of <b>vocabulary (lexical resource)</b>. A few slips are fine at band 7. Frequent errors hold you below it."),
           ("Speaking", "Not assessed. Pronunciation is marked, spelling is not.")],
    both="""<p>British and American spellings are <b>both accepted</b>. But be <b>consistent</b>: <i>colour</i> with <i>centre</i>, or <i>color</i> with <i>center</i>, never one of each (Spelling Unit 7).</p>""",
    how=[("Keep a list of your own errors.", "Ten words at a time. Your mistakes repeat, so a short personal list beats any long word list."),
         ("Look, say, cover, write, check.", "Look at the word, say it in syllables, cover it, write it from memory, then check. Do this three times."),
         ("Break words into chunks.", "ac-com-mo-da-tion, ne-ces-sa-ry, en-vi-ron-ment. A long word is four easy ones."),
         ("Use a memory trick.", "A rat in sepaRATe. One collar and two sleeves in necessary. Silly tricks stick."),
         ("Proofread backwards.", "In the last three minutes of Writing, read your essay one sentence at a time, from the last sentence to the first. Your eye then sees the spelling, not the meaning."),
         ("Do not trade a good word for a safe one.", "A correct, precise word you can spell is best, but never avoid a good word forever. Learn to spell it.")],
)

SPELLING = [
dict(
    id="s1", where="Listening · Reading · Writing", title="Doubling the last letter",
    rule="""<p>When you add <b>-ed, -ing, -er, -est</b> to a word, do you double the last letter?</p>
<ul>
<li><b>One syllable, one vowel, one consonant → double it.</b> <i>stop → stopped, run → running, big → bigger, plan → planned</i>.</li>
<li><b>Two syllables → double only if the stress is on the last syllable.</b> <i>be<b>GIN</b> → beginning, oc<b>CUR</b> → occurred, re<b>FER</b> → referred</i> (but <i><b>VIS</b>it → visited, <b>LIS</b>ten → listening, <b>OP</b>en → opened</i>).</li>
<li><b>Do not double</b> after two consonants (<i>help → helped</i>), after two vowels (<i>rain → rained</i>), or after <i>w, x, y</i> (<i>play → played, fix → fixed</i>).</li>
<li><b>British -l:</b> a final <i>l</i> doubles even when it is not stressed: <i>travel → travelled, cancel → cancelled</i>. (American: <i>traveled</i>.)</li>
</ul>""",
    fits=[("Past simple in Writing", "stopped, planned, dropped", "Prices <b>dropped</b> in 2010."),
          ("Gerund in Listening", "beginning, running", "the <b>beginning</b> of term"),
          ("Comparative in Task 1", "bigger, hotter, thinner", "a <b>bigger</b> increase"),
          ("Two-syllable verbs", "occurred, referred, preferred", "It <b>occurred</b> in 2019.")],
    pairs=[("The price stoped falling in 2010.", "The price <b>stopped</b> falling in 2010.", "One syllable, one vowel, one consonant: double the p."),
           ("We are begining the test now.", "We are <b>beginning</b> the test now.", "The stress is on the last syllable (be-GIN): double the n."),
           ("She visitted three countries.", "She <b>visited</b> three countries.", "The stress is on the first syllable (VIS-it): no doubling."),
           ("The report refered to earlier work.", "The report <b>referred</b> to earlier work.", "re-FER: the stress is last, so double the r."),
           ("He planed his trip carefully.", "He <b>planned</b> his trip carefully.", "<i>Plan</i> doubles. (<i>Planed</i> means smoothed with a plane.)"),
           ("He was listenning to the radio.", "He was <b>listening</b> to the radio.", "LIS-ten: stress on the first syllable, no doubling.")],
    tricks=["<b>1-1-1 test:</b> one syllable, one vowel, one consonant → double.",
            "<b>Stress test:</b> say the word aloud. If the stress falls on the last syllable (beGIN, ocCUR, preFER), double. Otherwise, do not.",
            "<b>Exception to learn:</b> British <i>travelled, cancelled, labelled, modelled</i>."],
    qs=[Q("pick", "Prices ___ sharply in 2010.", opts=["droped", "dropped", "dropd"], ans=1, why="<i>Drop</i>: one syllable, one vowel, one consonant."),
        Q("pick", "She is ___ a new language.", opts=["learning", "learnning", "lerning"], ans=0, why="<i>Learn</i> ends in two consonants: no doubling."),
        Q("pick", "The accident ___ at 8 a.m.", opts=["occured", "occurred", "ocurred"], ans=1, why="oc-CUR: stress last, so double the r. <i>Occur</i> also has two c's."),
        Q("gap", "The museum ___ (open) in 1990.", acc=["opened"], why="OP-en: stress first, no doubling."),
        Q("gap", "He is ___ (run) in the marathon.", acc=["running"], why="One syllable, one vowel, one consonant: double the n."),
        Q("gap", "As a child, she ___ (prefer) tea to coffee.", acc=["preferred"], why="pre-FER: stress last, so double the r."),
        Q("spot", "The company is [[begining]] a new project.", fix="The company is beginning a new project.", why="be-GIN: double the n."),
        Q("spot", "He [[admited]] his mistake.", fix="He admitted his mistake.", why="ad-MIT: stress last, so double the t.")],
    remember="One syllable, one vowel, one consonant: double. Two syllables: double only if the stress is last (beGIN, ocCUR). British: travelled."),

dict(
    id="s2", where="Writing · Reading", title="The silent e",
    rule="""<ul>
<li><b>Drop the e before a suffix that begins with a vowel:</b> <i>make → making, hope → hoping, create → creation, manage → managing</i>.</li>
<li><b>Keep the e before a suffix that begins with a consonant:</b> <i>manage → manage<b>ment</b>, safe → safe<b>ly</b>, achieve → achieve<b>ment</b>, care → care<b>ful</b></i>.</li>
<li><b>Keep the e after c or g before -able / -ous</b> so the soft sound stays: <i>notice → notice<b>able</b>, courage → courage<b>ous</b></i>.</li>
<li><b>Exceptions to learn:</b> <i>argue → argu<b>ment</b>, true → tru<b>ly</b>, whole → whol<b>ly</b>, judge → judg<b>ment</b> (UK also judgement), nine → ninth</i>.</li>
<li>Words ending in <b>-ee, -oe, -ye</b> keep the e before <i>-ing</i>: <i>see → seeing, agree → agreeing, dye → dyeing</i>.</li>
</ul>""",
    fits=[("Gerund in Task 2", "making, creating, hoping", "Technology is <b>making</b> life easier."),
          ("Noun form for a topic sentence", "management, achievement, movement", "<b>Management</b> training…"),
          ("Adverbs of degree", "truly, safely, definitely", "<b>Truly</b> effective policies…"),
          ("Listening gap, a person", "manager, writer", "the <b>manager</b>")],
    pairs=[("She is makeing progress.", "She is <b>making</b> progress.", "Drop the e before <i>-ing</i>."),
           ("The new managment started in May.", "The new <b>management</b> started in May.", "Keep the e before <i>-ment</i> (a consonant)."),
           ("The change is noticable.", "The change is <b>noticeable</b>.", "Keep the e after c before <i>-able</i>."),
           ("This is truely important.", "This is <b>truly</b> important.", "Exception: <i>true → truly</i>."),
           ("Her arguement was convincing.", "Her <b>argument</b> was convincing.", "Exception: <i>argue → argument</i>."),
           ("He is hopeing to travel.", "He is <b>hoping</b> to travel.", "Drop the e before <i>-ing</i>. (<i>Hopping</i> would be a different word.)")],
    tricks=["<b>Vowel suffix → drop e</b> (make-ing). <b>Consonant suffix → keep e</b> (manage-ment).",
            "<b>The five rebels:</b> argument, truly, wholly, ninth, judgment. Learn them as a group.",
            "<b>c or g + able / ous:</b> keep the e, because without it the c or g would turn hard: <i>noticeable, courageous</i>."],
    qs=[Q("pick", "The ___ of the project took two years.", opts=["achievment", "achievement", "acheivement"], ans=1, why="Keep the e before <i>-ment</i>; <i>ie</i> follows the 'i before e' rule."),
        Q("pick", "It is a ___ difference.", opts=["noticable", "noticeable", "noticible"], ans=1, why="Keep the e after c."),
        Q("pick", "She is ___ to improve.", opts=["hopeing", "hoping", "hopping"], ans=1, why="Drop the e. <i>Hopping</i> means jumping."),
        Q("gap", "His ___ (argue) was weak.", acc=["argument"], why="The exception: the e is dropped before <i>-ment</i>."),
        Q("gap", "The ___ (manage) approved the plan.", acc=["management", "manager"], why="<i>Management</i> keeps the e; <i>manager</i> drops it before the vowel suffix <i>-er</i>."),
        Q("gap", "It was ___ (true) a surprise.", acc=["truly"], why="The exception: <i>truly</i>, with no e."),
        Q("spot", "She is [[writeing]] her essay.", fix="She is writing her essay.", why="Drop the e before <i>-ing</i>."),
        Q("spot", "He lost the [[arguement]].", fix="He lost the argument.", why="The e is dropped: <i>argument</i>.")],
    remember="Vowel suffix: drop the e (making). Consonant suffix: keep it (management). The rebels: argument, truly, wholly, ninth."),

dict(
    id="s3", where="Writing · Task 1 data", title="Plurals and the y → ies rule",
    rule="""<ul>
<li><b>Consonant + y → ies / ied:</b> <i>study → studies, studied · country → countries · family → families</i>. Before <i>-ing</i> the y stays: <i>studying, carrying</i>.</li>
<li><b>Vowel + y: just add the ending:</b> <i>play → played, enjoy → enjoyed, key → keys</i>.</li>
<li><b>-es after s, x, z, ch, sh:</b> <i>boxes, buses, churches, wishes</i>.</li>
<li><b>f / fe → ves:</b> <i>life → lives, half → halves, leaf → leaves</i> (but <i>roofs, beliefs</i>).</li>
<li><b>Irregular:</b> <i>child → children, man → men, woman → women, person → people</i>. And the academic ones: <i>crisis → crises, analysis → analyses, phenomenon → phenomena, criterion → criteria, datum → data</i>.</li>
</ul>""",
    fits=[("Task 1 nouns", "countries, families, industries", "<b>Industries</b> grew."),
          ("Task 2 academic nouns", "analyses, criteria, phenomena", "several <b>criteria</b>"),
          ("Past tense", "studied, carried, tried", "She <b>studied</b> abroad."),
          ("People", "women, children, people", "<b>Women</b> earn less.")],
    pairs=[("She studyed abroad.", "She <b>studied</b> abroad.", "Consonant + y: change y to ied."),
           ("Governments need new policys.", "Governments need new <b>policies</b>.", "Consonant + y: ies."),
           ("Many familys live here.", "Many <b>families</b> live here.", "Consonant + y: ies."),
           ("Both countries face serious crisises.", "Both countries face serious <b>crises</b>.", "Irregular plural of <i>crisis</i>."),
           ("The children enjoied the trip.", "The children <b>enjoyed</b> the trip.", "Vowel + y: just add <i>-ed</i>."),
           ("Three womans applied.", "Three <b>women</b> applied.", "Irregular plural.")],
    tricks=["<b>Look at the letter before the y.</b> A consonant → change it. A vowel → leave it.",
            "<b>Say the plural aloud.</b> If you hear an extra syllable (bus-es, box-es, church-es), you need <i>-es</i>.",
            "<b>Learn the academic irregulars as pairs:</b> crisis/crises, analysis/analyses, criterion/criteria, phenomenon/phenomena."],
    qs=[Q("pick", "There are two ___ in the survey.", opts=["criterions", "criteria", "criterias"], ans=1, why="Irregular plural."),
        Q("pick", "Many ___ migrate to cities.", opts=["familys", "families", "familes"], ans=1, why="Consonant + y: ies."),
        Q("pick", "Several ___ have been proposed.", opts=["analysis", "analyses", "analysises"], ans=1, why="Irregular plural of <i>analysis</i>."),
        Q("gap", "She ___ (study) law in London last year.", acc=["studied"], why="Consonant + y: ied."),
        Q("gap", "They packed ten ___ (box).", acc=["boxes"], why="After x: <i>-es</i>."),
        Q("gap", "Fast food damages people's ___ (life).", acc=["lives"], why="f/fe → ves."),
        Q("spot", "The two [[countrys]] signed a trade deal.", fix="The two countries signed a trade deal.", why="Consonant + y: ies."),
        Q("spot", "The company [[carryed]] out a survey.", fix="The company carried out a survey.", why="Consonant + y: ied.")],
    remember="Consonant + y: ies / ied. Vowel + y: add the ending. -es after s, x, z, ch, sh. Learn crisis/crises, criterion/criteria, analysis/analyses."),

dict(
    id="s4", where="Listening · Writing", title="ie / ei and silent letters",
    rule="""<ul>
<li><b>i before e, except after c, when the sound is "ee":</b> <i>believe, achieve, relief, friend</i> but <i>receive, ceiling, deceive</i>.</li>
<li><b>Exceptions:</b> <i>weird, seize, either, neither, protein, foreign, height, their</i>.</li>
<li><b>Sound "ay" → ei:</b> <i>neighbour, weigh, eight</i>.</li>
<li><b>Silent letters</b> are the most common slips. Say each one in your head as you write: <i>gov<b>ern</b>ment, envi<b>ron</b>ment</i> (n), <i>Wed<b>nes</b>day</i> (d), <i>know<b>ledge</b></i> (k, d), <i>Feb<b>ru</b>ary</i> (r), <i>lib<b>rar</b>y</i> (r), <i>island</i> (s), <i>answer</i> (w), <i>psychology</i> (p), <i>doubt, debt</i> (b), <i>guarantee</i> (u).</li>
</ul>""",
    fits=[("Listening, days and months", "Wednesday, February", "on <b>Wednesday</b>"),
          ("Task 2 key nouns", "government, environment, knowledge", "the <b>environment</b>"),
          ("Reading, copy exactly", "foreign, height, neighbour", "<b>foreign</b> languages"),
          ("Everyday spelling", "friend, believe, receive", "I <b>believe</b> that…")],
    pairs=[("She will recieve the results.", "She will <b>receive</b> the results.", "After c: <i>ei</i>."),
           ("I beleive this is wrong.", "I <b>believe</b> this is wrong.", "<i>Ie</i> after b (sound ee)."),
           ("The goverment announced new rules.", "The <b>government</b> announced new rules.", "The silent n: govern-ment."),
           ("The enviroment must be protected.", "The <b>environment</b> must be protected.", "The silent n: environ-ment."),
           ("The test is on Wensday.", "The test is on <b>Wednesday</b>.", "Wed-nes-day: the d is silent but written."),
           ("He has a lot of knowlege.", "He has a lot of <b>knowledge</b>.", "Know + ledge: the d is silent but written.")],
    tricks=["<b>Say it the wrong way on purpose:</b> Wed-NES-day, GOV-ERN-ment, en-VI-RON-ment, FEB-ru-ary. Pronouncing the silent letters in your head fixes the spelling.",
            "<b>Rhyme:</b> <i>i before e, except after c, or when sounding like ay, as in neighbour and weigh</i>.",
            "<b>Learn the exceptions as a sentence:</b> <i>Neither foreign height is weird.</i>"],
    qs=[Q("pick", "She is my best ___.", opts=["freind", "friend", "frend"], ans=1, why="<i>Ie</i> (sound ee), not after c."),
        Q("pick", "The ___ of the building is 40 metres.", opts=["hieght", "height", "heigth"], ans=1, why="An exception: <i>height</i>."),
        Q("pick", "She ___ the news yesterday.", opts=["recieved", "received", "receved"], ans=1, why="After c: <i>ei</i>."),
        Q("gap", "The ___ (govern) has raised taxes.", acc=["government"], why="govern-ment."),
        Q("gap", "Protecting the ___ (environ) is a priority.", acc=["environment"], why="environ-ment."),
        Q("gap", "The days: Monday, Tuesday, ___.", acc=["wednesday"], why="Wed-nes-day."),
        Q("spot", "She has a lot of [[knowlege]] about history.", fix="She has a lot of knowledge about history.", why="Know + ledge."),
        Q("spot", "The [[libary]] opens at nine.", fix="The library opens at nine.", why="Lib-rar-y: two r's.")],
    remember="i before e except after c (receive); exceptions: weird, height, foreign, either. Say the silent letters in your head: govern-ment, Wed-nes-day."),

dict(
    id="s5", where="Writing · Reading", title="Words that sound alike",
    rule="""<p>Spell-check will not catch these, because every one is a real word.</p>
<ul>
<li><b>affect</b> (verb) / <b>effect</b> (noun): <i>Noise <b>affects</b> sleep. Noise has an <b>effect</b> on sleep.</i></li>
<li><b>advice</b> (noun) / <b>advise</b> (verb): <i>I advise you to follow his advice.</i></li>
<li><b>their</b> (belonging to them) / <b>there</b> (place, <i>there is</i>) / <b>they're</b> (they are).</li>
<li><b>its</b> (belonging to it) / <b>it's</b> (it is, it has).</li>
<li><b>than</b> (comparing) / <b>then</b> (next). <b>lose</b> (verb) / <b>loose</b> (not tight). <b>quiet</b> / <b>quite</b>. <b>accept</b> / <b>except</b>. <b>whether</b> / <b>weather</b>.</li>
<li><b>principal</b> (main; head of a school) / <b>principle</b> (a rule).</li>
<li><b>practice</b> (noun) / <b>practise</b> (verb, British; American uses practice for both).</li>
</ul>""",
    fits=[("Cause and effect, Task 2", "affect / effect", "This will <b>affect</b> health; the <b>effect</b> is clear."),
          ("Comparisons, Task 1", "than / then", "higher <b>than</b> in 2000"),
          ("Introducing a point", "there is / their", "<b>There is</b> evidence that…"),
          ("Reading, copy exactly", "its / it's", "<b>It's</b> clear that its cost…")],
    pairs=[("Smoking effects your health.", "Smoking <b>affects</b> your health.", "The verb is <i>affect</i>."),
           ("Their are many solutions.", "<b>There</b> are many solutions.", "<i>There are</i>, the place word."),
           ("Its a serious problem.", "<b>It's</b> a serious problem.", "<i>It's</i> = <i>it is</i>."),
           ("They lost there jobs.", "They lost <b>their</b> jobs.", "Belonging to them: <i>their</i>."),
           ("The price is higher then last year.", "The price is higher <b>than</b> last year.", "A comparison: <i>than</i>."),
           ("I need some advise.", "I need some <b>advice</b>.", "The noun is <i>advice</i> (with a c).")],
    tricks=["<b>affect = action</b> (both start with a). <b>effect = end result</b> (both start with e).",
            "<b>advice has ice</b> in it (a noun you can hold). <b>advise</b> sounds like <i>wise</i>.",
            "<b>there</b> has <b>here</b> inside it: both are places. <b>their</b> has <b>heir</b>: it belongs to someone.",
            "<b>It's</b> always means <i>it is</i> or <i>it has</i>. If you cannot say that, write <i>its</i>."],
    qs=[Q("pick", "Technology has a major ___ on education.", opts=["affect", "effect", "afect"], ans=1, why="The noun: <i>effect</i>."),
        Q("pick", "Please ___ my advice.", opts=["except", "accept", "expect"], ans=1, why="<i>Accept</i> = take. <i>Except</i> = apart from."),
        Q("pick", "Prices were higher ___ expected.", opts=["then", "than", "that"], ans=1, why="A comparison: <i>than</i>."),
        Q("pick", "I don't know ___ to go.", opts=["weather", "whether", "wether"], ans=1, why="<i>Whether</i> = if."),
        Q("gap", "Doctors ___ (advice / advise) patients to exercise.", acc=["advise"], why="The verb is <i>advise</i>."),
        Q("gap", "___ (Their / There / They're) are three main reasons.", acc=["there"], why="<i>There are</i>."),
        Q("spot", "The country must protect [[it's]] borders.", fix="The country must protect its borders.", why="Belonging to it: <i>its</i>."),
        Q("spot", "Don't [[loose]] hope.", fix="Don't lose hope.", why="The verb is <i>lose</i>. <i>Loose</i> means not tight.")],
    remember="affect (verb) / effect (noun). advice (noun) / advise (verb). there / their / they're. its / it's. than / then. lose / loose."),

dict(
    id="s6", where="Writing · Listening", title="The most common IELTS misspellings, with memory tricks",
    fits_head=("Word", "Common slip", "Memory trick"),
    rule="""<p>These words come up again and again in IELTS essays and Listening answers. Learn the <b>trick</b> for each one, not just the spelling.</p>""",
    fits=[("accommodation", "accomodation", "<b>Double c and double m</b>: a room for two needs two of each."),
          ("necessary", "neccessary, necesary", "<b>One collar, two sleeves</b>: one c, two s."),
          ("separate", "seperate", "There is <b>a rat</b> in sepaRATe."),
          ("definitely", "definately", "There is <b>finite</b> in deFINITEly."),
          ("recommend", "reccomend", "<b>One c, two m's</b>: re + commend."),
          ("occurred", "occured", "<b>Double c and double r</b>."),
          ("business", "busines", "<b>Bus-i-ness</b>: say the i."),
          ("embarrass", "embarass", "<b>Double r, double s</b>: two red cheeks, two s's."),
          ("successful", "sucessful", "<b>Double c, double s</b>: <i>suc-cess-ful</i>."),
          ("independent", "independant", "Ends in <b>-ent</b>. (Check: <i>dependent, different</i>.)"),
          ("immediately", "imediately", "<b>Double m</b>: im-MED-iate-ly."),
          ("temperature", "temprature", "Four syllables: tem-per-a-ture."),
          ("restaurant", "resturant", "<b>Rest-au-rant</b>: you can rest in a restaurant."),
          ("February", "Febuary", "Say <b>Feb-ru-ary</b>: the r is there."),
          ("privilege", "priviledge", "Ends in <b>-ege</b>: privi-lege."),
          ("occasion", "ocasion", "<b>Double c, single s</b>.")],
    pairs=[("Accomodation is expensive in the city.", "<b>Accommodation</b> is expensive in the city.", "Two c's and two m's."),
           ("It is necesary to study every day.", "It is <b>necessary</b> to study every day.", "One c, two s's."),
           ("The two groups are seperate.", "The two groups are <b>separate</b>.", "A rat in sepaRATe."),
           ("She definately agrees.", "She <b>definitely</b> agrees.", "deFINITEly."),
           ("I recomend this course.", "I <b>recommend</b> this course.", "One c, two m's."),
           ("The company is a big busines.", "The company is a big <b>business</b>.", "bus-i-ness.")],
    tricks=["<b>Pick your five worst</b> from the table and write each one ten times with its trick next to it.",
            "<b>Doubles:</b> accommodation (cc, mm), occurred (cc, rr), embarrass (rr, ss), successful (cc, ss), recommend (mm), immediately (mm).",
            "<b>Check the list again</b> before every practice essay, and again in your last three minutes."],
    qs=[Q("pick", "The ___ is near the campus.", opts=["accomodation", "accommodation", "acommodation"], ans=1, why="Two c's and two m's."),
        Q("pick", "It is ___ to book early.", opts=["neccessary", "necessary", "necesary"], ans=1, why="One collar (c), two sleeves (ss)."),
        Q("pick", "They ___ about the cost.", opts=["disagreed", "dissagreed", "disaggreed"], ans=0, why="<i>Dis</i> + <i>agree</i>: one s, one g."),
        Q("gap", "I would ___ this book to anyone. (re-com-mend)", acc=["recommend"], why="One c, two m's."),
        Q("gap", "Keep the two papers in ___ folders. (se-pa-rate)", acc=["separate"], why="A rat in sepaRATe."),
        Q("gap", "The family ___ (bus-i-ness) was successful.", acc=["business"], why="Say the i: bus-i-ness."),
        Q("spot", "The mistake was very [[embarassing]].", fix="The mistake was very embarrassing.", why="Double r, double s."),
        Q("spot", "She was [[sucessful]] in her career.", fix="She was successful in her career.", why="Double c, double s.")],
    remember="Learn the trick, not just the word: a rat in sepaRATe, deFINITEly, one collar and two sleeves in necessary, double letters in accommodation."),

dict(
    id="s7", where="Writing · consistency", title="British or American? Be consistent",
    rule="""<p>IELTS accepts both. The examiner only checks that you do not <b>mix</b> them inside one essay.</p>
<ul>
<li><b>-our / -or:</b> <i>colour / color, behaviour / behavior, favour / favor, neighbour / neighbor, labour / labor</i>.</li>
<li><b>-re / -er:</b> <i>centre / center, theatre / theater, metre / meter</i>.</li>
<li><b>-ise / -ize:</b> <i>organise / organize, realise / realize</i>. (Both are common in British English. <i>analyse</i> is British only; American is <i>analyze</i>.)</li>
<li><b>-ence / -ense:</b> <i>defence / defense, licence (noun) / license</i>.</li>
<li><b>Doubled l:</b> <i>travelled / traveled, cancelled / canceled</i>.</li>
<li><b>Others:</b> <i>programme / program, grey / gray, cheque / check, catalogue / catalog</i>.</li>
</ul>""",
    fits=[("Choose once, at the start", "all British or all American", "colour · centre · organise"),
          ("Listening / Reading answers", "either is accepted", "<i>centre</i> or <i>center</i>"),
          ("Words that never change", "program (computing), practice (noun)", "a computer <b>program</b>"),
          ("Typed words in a gap", "copy the passage's spelling", "<i>neighbours</i>")],
    pairs=[("The theater's colour scheme was popular.", "The <b>theatre's colour</b> scheme was popular. (Or: <b>theater's color</b>.)", "Do not mix British and American."),
           ("We analyze the data and organise the results.", "We <b>analyse</b> the data and <b>organise</b> the results. (Or: <b>analyze … organize</b>.)", "One variety throughout."),
           ("She traveled to Canada and cancelled the trip.", "She <b>travelled</b> to Canada and <b>cancelled</b> the trip. (Or: <b>traveled … canceled</b>.)", "Both l-words match."),
           ("The program was at the town centre.", "The <b>programme</b> was at the town <b>centre</b>. (Or: <b>program … center</b>.)", "Keep one variety."),
           ("The programme was funded by the defence ministry and the labor union.", "The programme was funded by the defence ministry and the <b>labour</b> union.", "All British: <i>labour</i>."),
           ("The neighbourhood is quiet and my neighbors are friendly.", "The neighbourhood is quiet and my <b>neighbours</b> are friendly.", "Match <i>neighbourhood</i>.")],
    tricks=["<b>Pick one on day one</b> and stick with it in every essay. Most candidates choose British because the course books use it.",
            "<b>If unsure</b> which spelling you used earlier, scroll up and match it.",
            "<b>Words like <i>program</i> (computing)</b> are the same in both. Do not worry about them."],
    qs=[Q("pick", "Which is consistent British spelling?", opts=["The colour of the centre", "The color of the centre", "The colour of the center"], ans=0, why="Both words are British."),
        Q("pick", "Which is consistent American spelling?", opts=["The favourite theater", "The favorite theater", "The favorite theatre"], ans=1, why="Both words are American."),
        Q("pick", "Which spelling is NOT accepted in either variety?", opts=["organise", "organize", "organnise"], ans=2, why="Both <i>organise</i> and <i>organize</i> are fine. <i>Organnise</i> is simply wrong."),
        Q("gap", "British spelling of <i>center</i>: ___", acc=["centre"], why="-re in British English."),
        Q("gap", "American spelling of <i>behaviour</i>: ___", acc=["behavior"], why="-or in American English."),
        Q("gap", "British spelling of <i>traveled</i>: ___", acc=["travelled"], why="Doubled l in British English."),
        Q("spot", "She loved the color, the flavor and the [[centre]] of the old town.", fix="She loved the color, the flavor and the center of the old town.", why="The first two words are American, so <i>center</i>."),
        Q("spot", "The report analyses the [[behavior]] of customers and the labour market.", fix="The report analyses the behaviour of customers and the labour market.", why="The rest is British, so <i>behaviour</i>.")],
    remember="Both are accepted. Choose one and keep it: colour + centre + organise, or color + center + organize."),
]

SHUNT = [
    Q("spot", "The shop [[openned]] in 1995.", fix="The shop opened in 1995.", why="OP-en: no doubling.", unit="s1"),
    Q("spot", "He was [[runing]] for the bus.", fix="He was running for the bus.", why="One syllable, one vowel, one consonant: double the n.", unit="s1"),
    Q("spot", "The government [[recieved]] hundreds of complaints.", fix="The government received hundreds of complaints.", why="After c: <i>ei</i>.", unit="s4"),
    Q("spot", "Prices have [[droped]] dramatically.", fix="Prices have dropped dramatically.", why="Double the p.", unit="s1"),
    Q("spot", "She [[studyed]] economics.", fix="She studied economics.", why="Consonant + y: ied.", unit="s3"),
    Q("spot", "Many [[familys]] cannot afford housing.", fix="Many families cannot afford housing.", why="Consonant + y: ies.", unit="s3"),
    Q("spot", "It is [[definately]] the best option.", fix="It is definitely the best option.", why="deFINITEly.", unit="s6"),
    Q("spot", "The [[enviroment]] must be protected.", fix="The environment must be protected.", why="The silent n.", unit="s4"),
    Q("spot", "The cost of [[accomodation]] has risen.", fix="The cost of accommodation has risen.", why="Two c's and two m's.", unit="s6"),
    Q("spot", "Sleep loss can badly [[effect]] concentration.", fix="Sleep loss can badly affect concentration.", why="The verb is <i>affect</i>.", unit="s5"),
    Q("spot", "She gave me good [[advise]].", fix="She gave me good advice.", why="The noun is <i>advice</i>.", unit="s5"),
    Q("spot", "[[Their]] is no evidence for this claim.", fix="There is no evidence for this claim.", why="<i>There is</i>.", unit="s5"),
    Q("spot", "The [[managment]] changed the policy.", fix="The management changed the policy.", why="Keep the e before <i>-ment</i>.", unit="s2"),
    Q("spot", "The change is quite [[noticable]].", fix="The change is quite noticeable.", why="Keep the e after c.", unit="s2"),
    Q("spot", "He made a [[truely]] original point.", fix="He made a truly original point.", why="The exception: <i>truly</i>.", unit="s2"),
    Q("spot", "The two systems are [[seperate]].", fix="The two systems are separate.", why="A rat in sepaRATe.", unit="s6"),
    Q("spot", "A [[sucessful]] business needs planning.", fix="A successful business needs planning.", why="Double c, double s.", unit="s6"),
    Q("spot", "The [[libary]] was closed on Wednesday.", fix="The library was closed on Wednesday.", why="Lib-rar-y.", unit="s4"),
    Q("spot", "Wages are higher [[then]] last year.", fix="Wages are higher than last year.", why="A comparison: <i>than</i>.", unit="s5"),
    Q("spot", "The accident [[occured]] at night.", fix="The accident occurred at night.", why="Double c and double r.", unit="s1"),
]

SPELL_CHEAT = [
    ("Spelling · -ed, -ing", "Double only if the stress is last", "<b>stopped, begin → beginning</b> · visited, listening", "s1"),
    ("Spelling · suffixes", "Vowel suffix: drop e · consonant suffix: keep e", "<b>making, management</b> · argument, truly", "s2"),
    ("Spelling · plurals", "consonant + y → ies", "<b>countries, studied</b> · crises, criteria", "s3"),
    ("Spelling · ie / ei", "i before e, except after c", "<b>believe, receive</b> · foreign, height", "s4"),
    ("Spelling · sound-alikes", "affect / effect · its / it's", "<b>Noise affects sleep.</b> · advice / advise", "s5"),
    ("Spelling · top slips", "Learn the trick", "<b>a rat in sepaRATe</b> · deFINITEly", "s6"),
    ("Spelling · consistency", "One variety only", "<b>colour + centre</b> or <b>color + center</b>", "s7"),
]
