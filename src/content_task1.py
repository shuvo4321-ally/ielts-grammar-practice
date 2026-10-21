"""Units 1-8: grammar for Writing Task 1 (charts, tables, maps, processes).

Question kinds
  pick  - choose one option            Q("pick", stem, opts=[...], ans=index, why=...)
  gap   - type the missing form        Q("gap", stem with ___, acc=[accepted answers], why=...)
  spot  - tap the wrong word           Q("spot", sentence with the error in [[ ]], fix=corrected sentence, why=...)
"""


def Q(kind, stem, why, **kw):
    return dict(kind=kind, stem=stem, why=why, **kw)


TASK1 = [
dict(
    id="u1", where="Task 1 · charts and tables", title="Tense follows the dates on the chart",
    rule="""<p>Look at the time axis before you write a single verb. <b>The dates choose the tense, not you.</b></p>
<ul>
<li>Dates in the past (1990–2010): <b>past simple</b>. <i>Sales rose, peaked, fell.</i></li>
<li>No dates, or a table of current facts: <b>present simple</b>. <i>Men spend more time on sport.</i></li>
<li>Dates in the future (2030, 2050): <b>projection language</b>. <i>is expected to, is projected to, is predicted to, will.</i></li>
<li>Past dates that run into future dates: switch tense <b>at the point where the data becomes a forecast</b>.</li>
</ul>""",
    fits=[("Line graph 1990–2020", "past simple", "The number of visitors <b>doubled</b> between 1990 and 2005."),
          ("Table with no year", "present simple", "Japan <b>has</b> the highest proportion of elderly people."),
          ("Forecast to 2050", "is expected to / is projected to", "The figure <b>is projected to reach</b> 40% by 2050."),
          ("Overview sentence", "past simple or present, matching the data", "Overall, car ownership <b>increased</b> in every country.")],
    pairs=[("In 2005, the number of tourists has reached 2 million.", "In 2005, the number of tourists <b>reached</b> 2 million.",
            "A finished past date (in 2005) never takes the present perfect."),
           ("By 2040, the price rises to $8.", "By 2040, the price <b>is expected to rise</b> to $8.",
            "A forecast is not a fact. Present simple states it as certain, which misreports the chart."),
           ("The table shows that in 2015 Germany produces the most.", "The table shows that in 2015 Germany <b>produced</b> the most.",
            "\"The table shows\" stays present (the table exists now), but the data verb follows the date.")],
    band=("The number of cars will be increasing to 50 million in 2030.",
          "The number of cars is projected to climb to around 50 million by 2030.",
          "Band 9 uses a projection verb (<i>is projected to</i>), the right preposition for a deadline (<i>by</i>) and an approximation word."),
    qs=[Q("pick", "Between 1995 and 2005, coal consumption ___ by a third.", opts=["has fallen", "fell", "falls"], ans=1,
          why="A closed period in the past with both dates given: past simple."),
        Q("pick", "According to the forecast, the population of the city ___ 12 million by 2050.", opts=["reaches", "reached", "is predicted to reach"], ans=2,
          why="2050 is a forecast, so it needs projection language. <i>Reaches</i> states it as a fact."),
        Q("gap", "The pie chart shows how an average household ___ (spend) its money today.", acc=["spends"],
          why="No past date and the word <i>today</i>: present simple, third person <i>-s</i>."),
        Q("spot", "The graph shows that sales [[have peaked]] at 800 units in 2012 before declining.", fix="The graph shows that sales peaked at 800 units in 2012 before declining.",
          why="<i>In 2012</i> is a finished past time. Present perfect cannot sit with it.")],
    remember="Read the dates first. Past dates: past simple. No dates: present simple. Future dates: <i>is expected / projected to</i>."),

dict(
    id="u2", where="Task 1 + Task 2 + Speaking", title="Past simple or present perfect?",
    rule="""<p>Both talk about the past. The difference is <b>whether the time is finished</b>.</p>
<ul>
<li><b>Past simple:</b> a finished time that is named or understood: <i>in 2010, last year, when I was a child, during the 1990s</i>.</li>
<li><b>Present perfect:</b> a period that runs up to now: <i>since 2010, over the last decade, in recent years, so far, recently</i>.</li>
<li>Duration up to now: <b>for / since</b> with the present perfect. <i>Prices have risen for five years / since 2019.</i></li>
</ul>""",
    fits=[("Task 1, closed period", "past simple", "Unemployment <b>fell</b> in 2018."),
          ("Task 2, change up to now", "present perfect", "Online learning <b>has become</b> far more common in recent years."),
          ("Speaking, life experience", "present perfect", "I<b>'ve been</b> to Chittagong twice."),
          ("Speaking, a story", "past simple", "I <b>went</b> there last summer and <b>stayed</b> a week.")],
    pairs=[("In recent years, many people moved to cities.", "In recent years, many people <b>have moved</b> to cities.",
            "<i>In recent years</i> reaches up to now, so it takes the present perfect."),
           ("I have visited London in 2019.", "I <b>visited</b> London in 2019.",
            "A finished date (in 2019) needs past simple."),
           ("I live here since 2015.", "I<b>'ve lived</b> (or <b>'ve been living</b>) here since 2015.",
            "<i>Since</i> + a starting point means a period up to now: present perfect, never present simple.")],
    band=("Nowadays technology changed our life a lot.",
          "Over the past two decades, technology has transformed the way people work and communicate.",
          "A time frame that reaches now (<i>over the past two decades</i>) with the present perfect, and a precise verb instead of <i>changed a lot</i>."),
    qs=[Q("pick", "Since the 1980s, the gap between rich and poor ___ steadily.", opts=["widened", "has widened", "widens"], ans=1,
          why="<i>Since the 1980s</i> runs up to now: present perfect."),
        Q("pick", "The bridge ___ in 1998 and cut journey times by half.", opts=["was opened", "has been opened", "has opened"], ans=0,
          why="A finished date (1998): past simple. Passive, because the bridge did not open itself."),
        Q("gap", "I ___ (know) my best friend for about ten years now.", acc=["have known", "'ve known", "’ve known"],
          why="<i>Know</i> is a state verb, so no <i>-ing</i>; duration up to now with <i>for</i>: present perfect."),
        Q("spot", "Many governments [[have introduced]] sugar taxes in 2016.", fix="Many governments introduced sugar taxes in 2016.",
          why="<i>In 2016</i> is a finished time. Either drop the date or use past simple.")],
    remember="A named finished time takes past simple. <i>Since, for, recently, in recent years, so far</i> take the present perfect."),

dict(
    id="u3", where="Task 1 · process diagrams", title="The passive in process descriptions",
    rule="""<p>In a process, what matters is <b>what happens to the material</b>, not who does it. So the passive is the normal choice.</p>
<ul>
<li>Form: <b>is / are + past participle</b>. <i>The leaves are dried. The mixture is then heated.</i></li>
<li>Leave out <i>by</i> + doer unless the doer is important: <i>The bottles are collected <b>by lorries</b></i> is fine; <i>by workers</i> usually adds nothing.</li>
<li>Natural processes (life cycles) use the <b>active</b>: <i>The eggs hatch. The larva grows.</i></li>
<li>Some verbs are never passive: <i>consist of, happen, occur, become, take place</i>.</li>
</ul>""",
    fits=[("Manufacturing, recycling, production", "present simple passive", "The glass <b>is crushed</b> and then <b>melted</b>."),
          ("Natural cycle", "present simple active", "The frog <b>lays</b> its eggs in water."),
          ("Overview of a process", "active, with a count", "The process <b>consists of</b> six stages."),
          ("Sequencing", "passive + sequencers", "<b>Once</b> it has been cleaned, the wool <b>is spun</b> into yarn.")],
    pairs=[("The process is consisted of five stages.", "The process <b>consists of</b> five stages.",
            "<i>Consist of</i> is never passive."),
           ("Then workers heat the sand to 1,500°C.", "The sand <b>is then heated</b> to 1,500°C.",
            "The workers are obvious. The passive keeps the focus on the material."),
           ("The caterpillar is turned into a butterfly.", "The caterpillar <b>turns into</b> a butterfly.",
            "Nobody turns it. Natural changes are active.")],
    band=("First they pick the tea and then they dry it and after that they put it in bags.",
          "Once the leaves have been picked, they are dried for several hours before being packed into bags.",
          "Passive throughout, a time clause (<i>once…</i>) and a passive <i>-ing</i> form (<i>before being packed</i>) instead of a chain of <i>and then</i>."),
    qs=[Q("pick", "At the next stage, the clay ___ into bricks.", opts=["shapes", "is shaped", "has shaped"], ans=1,
          why="The clay does not shape itself: present simple passive."),
        Q("pick", "The whole cycle ___ about three weeks.", opts=["is taken", "takes", "is taking"], ans=1,
          why="<i>Take</i> meaning <i>last</i> is active; a general fact about the cycle: present simple."),
        Q("gap", "After the cans ___ (collect), they are taken to a recycling plant.", acc=["are collected", "have been collected"],
          why="Passive, because the cans are collected by someone. Present simple or present perfect passive both work after <i>after</i>."),
        Q("spot", "The water is boiled and then it [[is evaporated]] into steam.", fix="The water is boiled and then it evaporates into steam.",
          why="Evaporating happens by itself. It is an intransitive verb, so it has no passive.")],
    remember="Things done to the material: passive. Things that happen by themselves: active. <i>Consist of</i> and <i>happen</i>: never passive."),

dict(
    id="u4", where="Task 1 · charts", title="Verbs and nouns of change, and their prepositions",
    rule="""<p>One small word changes the meaning of the whole sentence:</p>
<ul>
<li><b>rose to 20%</b>: the end point. <b>rose by 5%</b>: the size of the change. <b>rose from 15% to 20%</b>: start and end.</li>
<li>As a noun: <b>a rise in</b> + the thing, <b>a rise of</b> + the amount. <i>a rise of 5% in sales</i>.</li>
<li><b>stood at / peaked at / bottomed out at</b> + a figure. <b>levelled off at</b> + a figure.</li>
<li>Verb pairs: <i>rise / raise</i>: prices <b>rise</b> (no object); the government <b>raises</b> taxes (object).</li>
</ul>""",
    fits=[("Size of change", "by", "Exports grew <b>by</b> 12%."),
          ("End point", "to", "Exports grew <b>to</b> $40bn."),
          ("Starting figure", "stood at / began at", "In 2000 the rate <b>stood at</b> 7%."),
          ("Noun phrase", "a + adjective + noun + in", "There was <b>a sharp fall in</b> imports.")],
    pairs=[("Sales increased with 10%.", "Sales increased <b>by</b> 10%.", "The amount of change takes <b>by</b>."),
           ("There was a significant increase of the number of students.", "There was a significant increase <b>in</b> the number of students.",
            "<b>in</b> before the thing that changed; <b>of</b> only before an amount."),
           ("The price was raised to $5 in 2010.", "The price <b>rose</b> to $5 in 2010.",
            "<i>Raised</i> needs someone doing it. For a chart, use <i>rose</i>.")],
    band=("The number went up and then it went down and then it was the same.",
          "The figure climbed to a peak of 60 in 2008, dropped sharply over the following two years and then levelled off at around 35.",
          "Exact prepositions (<i>to a peak of, at around</i>), varied verbs and one clear time line."),
    qs=[Q("pick", "Rice exports fell ___ 4 million tonnes, reaching a low of 2 million.", opts=["to", "by", "at"], ans=1,
          why="4 million is the size of the fall (6 → 2), so <i>by</i>."),
        Q("pick", "There was a dramatic rise ___ the cost of housing.", opts=["of", "in", "at"], ans=1,
          why="<i>A rise in</i> + the thing that rose."),
        Q("gap", "The unemployment rate peaked ___ 11% in 2012.", acc=["at"],
          why="<i>Peak at</i>, <i>stand at</i>, <i>level off at</i> + the figure."),
        Q("spot", "The government [[rose]] the minimum wage twice in five years.", fix="The government raised the minimum wage twice in five years.",
          why="With an object (<i>the minimum wage</i>), the verb is <i>raise</i>. <i>Rise</i> never takes an object.")],
    remember="<b>to</b> = where it ended. <b>by</b> = how much it moved. <b>a rise in</b> the thing, <b>a rise of</b> the amount."),

dict(
    id="u5", where="Task 1 · comparisons", title="Comparing figures accurately",
    rule="""<ul>
<li>One syllable: <b>-er / -est</b> (<i>higher, the lowest</i>). Two or more: <b>more / most</b> (<i>more popular</i>). Never both: <i>more higher</i>.</li>
<li>Multiples: <b>twice as many as / three times as high as</b>, or <b>twice the number of</b>.</li>
<li>Size of a difference: <b>slightly / marginally / considerably / significantly / far</b> + comparative. Not <i>very higher</i>.</li>
<li>Uncountable: <b>much / far more money</b>. Countable: <b>many / far more people</b>. Fewer for countables, less for uncountables.</li>
<li>Equality: <b>the same as, as … as</b>, and for a near match <b>almost as … as</b>.</li>
</ul>""",
    fits=[("Two figures, big gap", "far / considerably + comparative", "Women's wages were <b>considerably lower than</b> men's."),
          ("A multiple", "twice / three times as … as", "Spain received <b>twice as many</b> visitors <b>as</b> Greece."),
          ("Top or bottom", "the + superlative", "Oil was <b>the most widely used</b> fuel."),
          ("Similar figures", "(almost) as … as", "Rail was <b>almost as popular as</b> bus.")],
    pairs=[("The figure for Canada was more higher than Mexico.", "The figure for Canada was <b>higher than that of</b> Mexico.",
            "No double comparative, and compare figure with figure (<i>that of</i>), not figure with country."),
           ("Japan had two times more cars than Korea.", "Japan had <b>twice as many cars as</b> Korea.",
            "<i>Twice as many … as</i> is the accurate pattern for multiples."),
           ("Less people travelled by train.", "<b>Fewer</b> people travelled by train.", "People are countable: <i>fewer</i>.")],
    band=("The USA was very higher than China and China was less than India.",
          "The figure for the USA was considerably higher than that for China, which in turn was slightly below India's.",
          "Grading words (<i>considerably, slightly</i>), <i>that for</i> to compare like with like, and a non-defining clause to chain three items."),
    qs=[Q("pick", "Coal accounted for ___ electricity as gas did.", opts=["twice more", "twice as much", "two times much"], ans=1,
          why="Electricity is uncountable: <i>twice as much … as</i>."),
        Q("pick", "Consumption in 2020 was ___ than in 2010.", opts=["very higher", "much higher", "more higher"], ans=1,
          why="Comparatives are graded with <i>much, far, slightly, considerably</i>, never <i>very</i>."),
        Q("gap", "There were ___ (few) accidents in 2019 than in any other year.", acc=["fewer"],
          why="Accidents are countable: <i>fewer</i>, not <i>less</i>."),
        Q("spot", "The average salary in London was higher than [[Manchester]].", fix="The average salary in London was higher than that in Manchester.",
          why="Compare salary with salary: <i>than that in Manchester</i> (or <i>than in Manchester</i>), not salary with a city.")],
    remember="Never <i>more + -er</i> or <i>very + comparative</i>. Compare like with like: <i>that of / those of</i>."),

dict(
    id="u6", where="Task 1 · data nouns", title="The number of, a number of, and percentages",
    rule="""<p>Agreement with data words is the most common Task 1 grammar error. The verb agrees with the <b>head noun</b>:</p>
<ul>
<li><b>The number of</b> students <b>is</b> rising (head = <i>number</i>, singular).</li>
<li><b>A number of</b> students <b>are</b> unhappy (means <i>several</i>, plural).</li>
<li><b>The percentage / proportion / amount of</b> … <b>is / was</b>.</li>
<li><b>20% of</b> + plural noun → plural verb (<i>20% of adults <b>were</b></i>); + uncountable → singular (<i>20% of the land <b>was</b></i>).</li>
<li><b>Per cent</b> after a number; <b>percentage</b> as a noun without a number. Not <i>30 percentage</i>.</li>
</ul>""",
    fits=[("Count of people / things", "the number of + singular verb", "The number of cyclists <b>has</b> doubled."),
          ("Uncountable quantity", "the amount of", "The amount of waste <b>fell</b>."),
          ("A share", "the proportion / percentage of", "The proportion of graduates <b>was</b> highest in Korea."),
          ("A figure", "number + per cent", "Just over 40 <b>per cent</b> of homes had internet access.")],
    pairs=[("The number of tourists were higher in summer.", "The number of tourists <b>was</b> higher in summer.",
            "The head noun is <i>number</i>, which is singular."),
           ("The amount of cars increased.", "The <b>number</b> of cars increased.", "Cars are countable: <i>number</i>, not <i>amount</i>."),
           ("Around 30 percentage of people walked to work.", "Around 30 <b>per cent</b> of people walked to work.",
            "After a number, write <i>per cent</i> (or %). <i>Percentage</i> is the general noun.")],
    band=("The percent of people who use internet are increasing.",
          "The percentage of households with internet access rose steadily, reaching almost 90% by 2020.",
          "Correct noun (<i>percentage</i>), correct agreement (<i>rose</i>, head = percentage) and a precise figure."),
    qs=[Q("pick", "The number of international students ___ grown every year since 2010.", opts=["have", "has"], ans=1,
          why="Head noun <i>number</i> is singular."),
        Q("pick", "A large number of respondents ___ unhappy with the service.", opts=["was", "were"], ans=1,
          why="<i>A number of</i> means <i>several</i>, so the verb is plural."),
        Q("gap", "The ___ (amount / number) of electricity generated from wind tripled.", acc=["amount"],
          why="Electricity is uncountable: <i>amount</i>."),
        Q("spot", "Around 20% of the land [[were]] used for farming in 1950.", fix="Around 20% of the land was used for farming in 1950.",
          why="<i>20% of</i> + an uncountable noun (<i>land</i>) takes a singular verb. With a plural noun it would be plural: <i>20% of farms were</i>.")],
    remember="<i>The number of … is</i>. <i>A number of … are</i>. Countable → number; uncountable → amount. Number + <i>per cent</i>."),

dict(
    id="u7", where="Task 1 · numbers in phrases", title="Numbers inside phrases, and approximation",
    rule="""<ul>
<li>A number + noun used <b>before another noun</b> is an adjective, so <b>no plural -s</b>: <i>a <b>five-year</b> period, a <b>20-percent</b> rise, a <b>two-hour</b> journey</i>.</li>
<li>Hyphenate it: <i>a ten-year plan</i>. Without a following noun, use the plural: <i>over five years</i>.</li>
<li>Approximation goes before the number: <b>just over, just under, approximately, roughly, nearly, around, well over</b>.</li>
<li>Fractions and shares: <b>a third of, nearly half of, the majority of, a small minority of</b>.</li>
<li>Large numbers: <i>2 million</i> (no <i>s</i>), but <i>millions of people</i>.</li>
</ul>""",
    fits=[("Duration as an adjective", "number-noun (singular)", "over a <b>ten-year</b> period"),
          ("Rounding a figure", "approximation word + number", "<b>just under</b> 60%"),
          ("Describing a share", "fraction / majority", "<b>Roughly two-thirds</b> of students"),
          ("Big figures", "number + million (no s)", "<b>3.5 million</b> visitors")],
    pairs=[("over a five years period", "over a <b>five-year</b> period", "Number + noun before another noun: singular, hyphenated."),
           ("The population reached 8 millions.", "The population reached <b>8 million</b>.", "After a number, <i>million</i> has no <i>-s</i>."),
           ("Almost the half of the workers were women.", "<b>Almost half of</b> the workers were women.", "<i>Half</i> takes no article in this pattern.")],
    band=("It was about 49.7% in the first year and it was 70.2% at the end.",
          "The figure began at just under half and had risen to well over two-thirds by the end of the period.",
          "Band 9 rounds sensibly and turns figures into fractions, so the trend is easier to read. Exact figures are still fine for the key points."),
    qs=[Q("pick", "The survey covered a ___ period.", opts=["three-months", "three-month", "three month's"], ans=1,
          why="Number + noun before a noun: singular and hyphenated."),
        Q("pick", "In 2010, ___ people used public transport daily.", opts=["2 millions", "2 million", "2 million of"], ans=1,
          why="Number + <i>million</i>, no <i>-s</i> and no <i>of</i>."),
        Q("gap", "At 51%, ___ (most / the majority) of the votes went to the Green Party.", acc=["the majority", "most"],
          why="Both work. <i>The majority of</i> sounds more formal; <i>most of</i> is also correct."),
        Q("spot", "The government launched a [[twenty-years]] plan to reduce emissions.", fix="The government launched a twenty-year plan to reduce emissions.",
          why="Inside a noun phrase, the number + noun is singular: <i>a twenty-year plan</i>.")],
    remember="<i>a five-year period</i>, <i>8 million</i>, <i>almost half of</i>. Put the approximation word before the number."),

dict(
    id="u8", where="Task 1 · articles with data", title="Articles in chart descriptions",
    rule="""<ul>
<li><b>the</b> before a specific measure: <i><b>the</b> number of, <b>the</b> proportion of, <b>the</b> figure for, <b>the</b> highest</i>.</li>
<li>Countries: no article (<i>Japan, France</i>) except plural or political names: <i><b>the</b> UK, <b>the</b> USA, <b>the</b> Netherlands</i>.</li>
<li>Decades take <b>the</b>: <i>in <b>the</b> 1990s</i>. Single years do not: <i>in 1995</i>.</li>
<li>General plural or uncountable nouns: no article: <i>Cars were the main form of transport.</i></li>
<li><b>a / an</b> for one of something: <i><b>a</b> sharp rise, <b>an</b> 8% fall</i> (<i>an</i> because <i>eight</i> starts with a vowel sound).</li>
</ul>""",
    fits=[("A measure", "the + noun + of", "<b>The</b> proportion of women rose."),
          ("A country", "zero article (or <i>the</i> for UK/USA)", "<b>The</b> UK spent more than Italy."),
          ("A time", "in + year / in the + decade", "in 2001 · in <b>the</b> 2000s"),
          ("A single change", "a / an", "<b>an</b> 11% drop")],
    pairs=[("Number of students rose.", "<b>The</b> number of students rose.", "A specific measure takes <i>the</i>."),
           ("in 1980s", "in <b>the</b> 1980s", "Decades take <i>the</i>."),
           ("There was a 8% decline.", "There was <b>an</b> 8% decline.", "<i>an</i> before a vowel sound: <i>an eight…</i>")],
    band=("In UK, number of elderly people was higher than in USA in 2000s.",
          "In the UK, the number of elderly people was higher than in the USA throughout the 2000s.",
          "Four missing articles restored. No new vocabulary needed: accuracy alone moves this sentence up a band."),
    qs=[Q("pick", "___ highest figure was recorded in Brazil.", opts=["A", "The", "—"], ans=1, why="Superlatives take <i>the</i>."),
        Q("pick", "Spending rose sharply in ___ .", opts=["1990s", "the 1990s", "the 1995"], ans=1,
          why="Decades take <i>the</i>; single years do not."),
        Q("gap", "There was ___ 11% increase in exports.", acc=["an"], why="<i>Eleven</i> begins with a vowel sound: <i>an</i>."),
        Q("spot", "Overall, [[proportion]] of people working from home increased in all five countries.", fix="Overall, the proportion of people working from home increased in all five countries.",
          why="A specific measure: <i>the proportion of</i>.")],
    remember="<i>the number / proportion / figure</i>, <i>the UK / USA</i>, <i>in the 1990s</i>, <i>an 8% rise</i>."),
]
