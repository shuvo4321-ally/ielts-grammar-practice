"""Units 23-24 (Speaking and word order), the marking guide, the error hunt and the cheat sheet."""
from content_task1 import Q

SPEAKING = [
dict(
    id="u23", where="Speaking · Parts 1–3", title="Speaking tenses that sound natural",
    rule="""<p>In Speaking, grammar is judged on the same range-and-accuracy scale, but the structures that score are the natural ones.</p>
<ul>
<li>Up to now: <b>present perfect continuous</b>. <i>I<b>'ve been learning</b> English for six years.</i></li>
<li>Past habits: <b>used to</b> / <b>would</b>. <i>I <b>used to</b> walk to school. We <b>would</b> play cricket every evening.</i> (<i>Would</i> only for actions, not states.)</li>
<li>Plans: <b>be going to / be planning to / be hoping to</b>. Arrangements: <b>present continuous</b>. <i>I'm meeting my tutor tomorrow.</i></li>
<li>Wishes and regrets: <b>I wish I had / I wish I could / I wish I'd known</b>.</li>
<li>Softeners for opinions: <b>I'd say, I suppose, I'd probably, it depends on</b>.</li>
</ul>""",
    fits=[("Part 1: how long", "have been + -ing", "I<b>'ve been living</b> in Dhaka since 2018."),
          ("Part 2: childhood memory", "used to / would", "My grandfather <b>would</b> tell us stories."),
          ("Part 1: future", "I'm hoping to / I'm planning to", "I<b>'m hoping to</b> do a master's."),
          ("Part 3: hypothetical", "would / might", "People <b>would</b> probably travel less.")],
    pairs=[("I am living here since five years.", "I<b>'ve been living</b> here <b>for</b> five years.", "Duration up to now: present perfect (continuous) + <i>for</i>."),
           ("When I was child, I was used to play football.", "When I was <b>a</b> child, I <b>used to play</b> football.",
            "<i>Used to</i> + base verb for past habits. <i>Be used to + -ing</i> means <i>be accustomed to</i>."),
           ("I wish I can speak French.", "I wish I <b>could</b> speak French.", "<i>Wish</i> moves the verb back one tense.")],
    band=("I like reading. I read many books. When I was small I also read.",
          "I've always been a keen reader. As a child I used to get through a book a week, and these days I'd say I read mostly non-fiction.",
          "Four tenses used naturally (present perfect, <i>used to</i>, <i>I'd say</i>, present simple), with no slips."),
    qs=[Q("pick", "Examiner: How long have you studied English? — I ___ it since primary school.", opts=["study", "have been studying", "am studying"], ans=1,
          why="Duration up to now with <i>since</i>: present perfect continuous."),
        Q("pick", "When I was young, my family ___ in a small village.", opts=["would live", "used to live", "was used to live"], ans=1,
          why="<i>Live</i> is a state: <i>used to</i>, not <i>would</i>."),
        Q("gap", "I wish I ___ (have) more free time these days.", acc=["had"], why="<i>Wish</i> + past simple for a present wish."),
        Q("spot", "Next year I [[go]] to study engineering in Canada, if my visa is approved.", fix="Next year I'm going to study engineering in Canada, if my visa is approved.",
          why="A plan: <i>be going to</i> (or <i>I'm planning to / I'm hoping to</i>).")],
    remember="How long → <i>I've been -ing</i>. Childhood → <i>used to</i>. Plans → <i>I'm going / hoping to</i>. Wishes → <i>I wish I could / had</i>."),

dict(
    id="u24", where="Speaking + Writing", title="Word order: adverbs, enough, and indirect questions",
    rule="""<ul>
<li>Frequency adverbs go <b>before the main verb</b> and <b>after be</b>: <i>I <b>always</b> walk. I am <b>always</b> late.</i></li>
<li><b>also</b> follows the same rule: <i>It <b>also</b> saves time. It is <b>also</b> cheap.</i></li>
<li><b>enough</b> goes <b>after</b> an adjective but <b>before</b> a noun: <i>old <b>enough</b> · <b>enough</b> money</i>.</li>
<li>Indirect questions use <b>statement order</b>: <i>I don't know what <b>the answer is</b>.</i> Not <i>what is the answer</i>.</li>
<li>Do not put an adverb between a verb and its object: <i>I like <b>very much</b> football</i> ✗ → <i>I like football <b>very much</b></i>.</li>
</ul>""",
    fits=[("Speaking: habits", "adverb before the verb", "I <b>usually</b> cook at home."),
          ("Speaking: unsure answer", "statement order after <i>I'm not sure what…</i>", "I'm not sure why <b>people do</b> that."),
          ("Essay: adding a point", "also before the verb", "It <b>also</b> creates jobs."),
          ("Essay: amount", "enough + noun", "There is not <b>enough housing</b>.")],
    pairs=[("I go always to the gym on Fridays.", "I <b>always go</b> to the gym on Fridays.", "Frequency adverb before the main verb."),
           ("I don't know what is the reason.", "I don't know what <b>the reason is</b>.", "Indirect question: subject before verb."),
           ("Salaries are not enough high.", "Salaries are not <b>high enough</b>.", "<i>Enough</i> after an adjective.")],
    band=("I like very much travelling and I go often abroad.",
          "I really enjoy travelling, and I try to go abroad at least once a year.",
          "Adverbs placed correctly and a precise frequency phrase instead of <i>often</i>."),
    qs=[Q("pick", "Choose the correct order.", opts=["She speaks fluently English.", "She speaks English fluently.", "She fluently English speaks."], ans=1,
          why="No adverb between the verb and its object."),
        Q("pick", "Can you tell me where ___ ?", opts=["is the library", "the library is", "does the library is"], ans=1, why="Indirect question: statement order."),
        Q("gap", "Many rural areas do not have ___ (enough + doctors, in the right order).", acc=["enough doctors"], why="<i>Enough</i> goes before a noun: <i>enough doctors</i>."),
        Q("spot", "Public transport is cheap and it [[reduces also]] pollution.", fix="Public transport is cheap and it also reduces pollution.", why="<i>Also</i> goes before the main verb.")],
    remember="Adverb before the main verb, after <i>be</i>. Adjective + <i>enough</i>, <i>enough</i> + noun. Indirect questions: statement order."),
]

MARKING = dict(
    intro="""<p>One quarter of your Writing and Speaking score is grammar. The examiner looks at two things, and they pull in opposite directions:</p>
<ul>
<li><b>Range:</b> do you use a variety of sentence types (complex sentences, passives, conditionals, relative and participle clauses)?</li>
<li><b>Accuracy:</b> how many of your sentences are completely free of errors?</li>
</ul>
<p>Most band-7 candidates lose marks on <b>accuracy</b>, not range. The fastest way to band 8 is not new structures. It is <b>the same structures with fewer mistakes</b>.</p>""",
    bands=[("6", "A mix of simple and complex sentences, but complex ones often contain errors. Errors rarely stop the reader understanding."),
           ("7", "A variety of complex structures. Many sentences are error-free. A few errors keep coming back (articles, agreement, punctuation)."),
           ("8", "A wide range of structures. Most sentences are completely error-free. Only occasional slips."),
           ("9", "A full range used naturally and flexibly. Errors are rare and look like slips, not gaps in knowledge.")],
    rules=[("Accuracy first.", "A short sentence that is correct beats a long one with an error. Every error-free sentence counts in your favour."),
           ("Range from a handful of structures.", "Relative clauses, conditionals, the passive, participle clauses and noun phrases (Units 3, 12, 13, 18, 19) give you all the range you need for band 8."),
           ("Know your own top five errors.", "Do the Error Hunt (Part 3). Whatever you miss there is what you check for in the last three minutes of the test.")],
    how="""<ul>
<li>Each unit: <b>the rule</b> → <b>where it fits</b> in the test → <b>right and wrong</b> pairs → <b>band 7 vs band 9</b> → four quick questions.</li>
<li>Answer each question, then open <b>Show answer</b> underneath. It tells you if you were right and why.</li>
<li>In <b>Spot the error</b> questions, tap the word that is wrong.</li>
<li>Your answers are saved in this browser only.</li>
</ul>""",
)

# Part 3: mixed error hunt. Each sentence has exactly one error in [[ ]]; "unit" points back to the lesson.
HUNT = [
    Q("spot", "The number of people living alone [[have]] doubled since 1980.", fix="The number of people living alone has doubled since 1980.", why="Head noun <i>number</i>: singular.", unit="u6"),
    Q("spot", "In 2010, the price of oil [[has fallen]] to $70 a barrel.", fix="In 2010, the price of oil fell to $70 a barrel.", why="Finished date: past simple.", unit="u1"),
    Q("spot", "Many [[researches]] have shown the benefits of bilingual education.", fix="Much research has shown (or Many studies have shown) the benefits of bilingual education.", why="<i>Research</i> is uncountable.", unit="u10"),
    Q("spot", "[[Despite]] the rent is high, many students live in the city centre.", fix="Although the rent is high, many students live in the city centre.", why="A clause follows: <i>although</i>.", unit="u15"),
    Q("spot", "The government should encourage people [[using]] public transport.", fix="The government should encourage people to use public transport.", why="<i>Encourage</i> sb <i>to do</i>.", unit="u20"),
    Q("spot", "Exports rose [[with]] 15% between 2005 and 2010.", fix="Exports rose by 15% between 2005 and 2010.", why="Size of change: <i>by</i>.", unit="u4"),
    Q("spot", "[[The]] happiness depends more on relationships than on money.", fix="Happiness depends more on relationships than on money.", why="General uncountable idea: no article.", unit="u9"),
    Q("spot", "If governments [[will invest]] in renewable energy, emissions will fall.", fix="If governments invest in renewable energy, emissions will fall.", why="No <i>will</i> in the <i>if</i> clause.", unit="u13"),
    Q("spot", "Children [[which]] grow up bilingual often find it easier to learn a third language.", fix="Children who grow up bilingual often find it easier to learn a third language.", why="People: <i>who</i>.", unit="u12"),
    Q("spot", "The process [[is consisted]] of four main stages.", fix="The process consists of four main stages.", why="<i>Consist of</i> is never passive.", unit="u3"),
    Q("spot", "One of the main [[reason]] is the lack of affordable housing.", fix="One of the main reasons is the lack of affordable housing.", why="<i>One of the</i> + plural noun.", unit="u11"),
    Q("spot", "France received [[two times more]] visitors than Portugal.", fix="France received twice as many visitors as Portugal.", why="Multiples: <i>twice as many … as</i>.", unit="u5"),
    Q("spot", "Online shopping is convenient[[,]] it saves people a lot of time.", fix="Online shopping is convenient because it saves people a lot of time. (Or: …convenient; it saves…)", why="Comma splice.", unit="u17"),
    Q("spot", "The figure reached a peak of 8 [[millions]] in 2015.", fix="The figure reached a peak of 8 million in 2015.", why="Number + <i>million</i>: no <i>-s</i>.", unit="u7"),
    Q("spot", "Not only [[it reduces]] traffic, but it also improves air quality.", fix="Not only does it reduce traffic, but it also improves air quality.", why="Fronted <i>not only</i> → inversion.", unit="u22"),
    Q("spot", "Having finished the experiment, [[the results]] were sent to the journal.", fix="Having finished the experiment, the researchers sent the results to the journal.", why="Dangling participle: the results did not finish the experiment.", unit="u19"),
    Q("spot", "I look forward to [[hear]] from you soon.", fix="I look forward to hearing from you soon.", why="<i>Look forward to</i> + <i>-ing</i>.", unit="u20"),
    Q("spot", "There is a lack of [[informations]] about the risks of vaping.", fix="There is a lack of information about the risks of vaping.", why="Uncountable: no <i>-s</i>.", unit="u10"),
    Q("spot", "In recent years, more women [[entered]] politics than ever before.", fix="In recent years, more women have entered politics than ever before.", why="<i>In recent years</i>: present perfect.", unit="u2"),
    Q("spot", "Reading improves vocabulary, concentration and [[it helps]] you relax.", fix="Reading improves vocabulary and concentration and helps you relax.", why="Parallel structure in a list.", unit="u21"),
    Q("spot", "There was a significant increase [[of]] the number of electric cars.", fix="There was a significant increase in the number of electric cars.", why="<i>An increase in</i> + the thing.", unit="u4"),
    Q("spot", "I [[am living]] in this city since 2019.", fix="I have been living in this city since 2019.", why="<i>Since</i> → present perfect (continuous).", unit="u23"),
    Q("spot", "Nobody knows exactly what [[is the solution]] to this problem.", fix="Nobody knows exactly what the solution to this problem is.", why="Indirect question: statement order.", unit="u24"),
    Q("spot", "Fast food is cheap, [[however]] it is often unhealthy.", fix="Fast food is cheap; however, it is often unhealthy. (Or: …cheap, but it is…)", why="<i>However</i> cannot follow a comma to join two clauses.", unit="u15"),
]

# Part 4: which structure where
CHEAT = [
    ("Task 1 · past dates", "Past simple", "Sales <b>rose</b> by 20% between 2000 and 2010.", "u1"),
    ("Task 1 · future dates", "is expected / projected to", "The figure <b>is projected to reach</b> 40% by 2050.", "u1"),
    ("Task 1 · process", "Present passive + sequencers", "<b>Once</b> sorted, the glass <b>is crushed</b>.", "u3"),
    ("Task 1 · size of change", "by / to / a rise in", "fell <b>by</b> a third <b>to</b> 2m · <b>a rise in</b> demand", "u4"),
    ("Task 1 · comparing", "twice as … as / considerably + -er", "<b>twice as many</b> cars <b>as</b> · <b>considerably higher</b>", "u5"),
    ("Task 1 · data nouns", "the number of + singular verb", "<b>The number of</b> users <b>has</b> doubled.", "u6"),
    ("Task 1 · numbers in phrases", "number-noun (singular)", "a <b>ten-year</b> period · <b>8 million</b>", "u7"),
    ("Task 2 · change up to now", "Present perfect", "Technology <b>has transformed</b> work.", "u2"),
    ("Task 2 · general ideas", "Zero article", "<b>Education</b> reduces <b>crime</b>.", "u9"),
    ("Task 2 · evidence", "Uncountable nouns", "<b>Research shows</b> · <b>much evidence</b>", "u10"),
    ("Task 2 · adding detail", "Relative clause", "Cities, <b>which</b> are already crowded, …", "u12"),
    ("Task 2 · proposals", "Second conditional", "If schools <b>taught</b> X, pupils <b>would</b> …", "u13"),
    ("Task 2 · careful claims", "Hedging", "This <b>is likely to</b> / <b>may</b> …", "u14"),
    ("Task 2 · two sides", "While / Although + clause", "<b>While</b> some argue X, others …", "u15"),
    ("Task 2 · consequences", "lead to / result in + noun", "This <b>leads to</b> higher costs.", "u16"),
    ("Task 2 · topic sentences", "Noun phrase", "<b>The rapid growth of</b> X has …", "u18"),
    ("Task 2 · range", "Participle clause", "<b>Faced with</b> rising costs, many …", "u19"),
    ("Task 2 · solutions", "encourage / enable sb to · by + -ing", "<b>By investing</b> in X, governments <b>enable</b> people <b>to</b> …", "u20"),
    ("Task 2 · emphasis (once)", "Cleft or inversion", "<b>What</b> matters most <b>is</b> … · <b>Only by</b> … <b>can</b> we …", "u22"),
    ("Speaking · how long", "have been + -ing", "I<b>'ve been studying</b> here for two years.", "u23"),
    ("Speaking · childhood", "used to / would", "I <b>used to</b> walk to school.", "u23"),
    ("Speaking · unsure", "Indirect question order", "I'm not sure why <b>that is</b>.", "u24"),
]
