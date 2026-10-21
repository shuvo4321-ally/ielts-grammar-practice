"""Units 9-22: grammar for Writing Task 2 (and much of it for Speaking)."""
from content_task1 import Q

TASK2 = [
dict(
    id="u9", where="Task 2 · general ideas", title="Articles when you talk about things in general",
    rule="""<p>Essays talk about things <b>in general</b>, and that is where most article errors happen.</p>
<ul>
<li>General plural: <b>no article</b>. <i>Children need routine. Cars pollute cities.</i></li>
<li>General uncountable: <b>no article</b>. <i>Education, technology, society, nature, crime, happiness.</i> Not <i>the society</i>.</li>
<li><b>the</b> for one specific or unique thing: <i>the internet, the environment, the government (of a country), the economy</i>.</li>
<li><b>the</b> when the noun is limited by a phrase after it: <i><b>the</b> education <b>of girls in rural areas</b></i>.</li>
<li>A singular countable noun can never stand alone: <i><b>a</b> car, <b>the</b> car, cars</i>. Not <i>car is useful</i>.</li>
</ul>""",
    fits=[("General idea, plural", "no article", "<b>Teenagers</b> are influenced by <b>advertising</b>."),
          ("Unique / shared thing", "the", "<b>The internet</b> has changed <b>the economy</b>."),
          ("Limited by an <i>of</i> phrase", "the", "<b>the</b> cost <b>of living in cities</b>"),
          ("One example", "a / an", "<b>A</b> child who reads daily…")],
    pairs=[("The society should respect the elderly people.", "<b>Society</b> should respect <b>elderly people</b>.",
            "General ideas: no article. (<i>The elderly</i> as a group noun is also correct.)"),
           ("Internet has made life easier.", "<b>The</b> internet has made life easier.", "<i>The internet</i> is unique: always <i>the</i>."),
           ("Government should invest in public transport.", "<b>The</b> government (or <b>Governments</b>) should invest in public transport.",
            "<i>Government</i> as a body is countable: <i>the government</i> or <i>governments</i>.")],
    band=("The technology is very important in the modern life of the people.",
          "Technology now shapes almost every aspect of modern life.",
          "Three unnecessary articles removed and the idea made concrete. Correct articles make a script feel native-like."),
    qs=[Q("pick", "___ is one of the main causes of stress among young people.", opts=["The unemployment", "Unemployment", "An unemployment"], ans=1,
          why="A general uncountable idea: no article."),
        Q("pick", "Many people now buy everything on ___ .", opts=["internet", "the internet", "an internet"], ans=1, why="<i>The internet</i> always takes <i>the</i>."),
        Q("gap", "___ (the / —) quality of the air in big cities is getting worse.", acc=["the"],
          why="<i>Quality</i> is limited by <i>of the air in big cities</i>, so it takes <i>the</i>."),
        Q("spot", "In my opinion, [[the nature]] should be protected at all costs.", fix="In my opinion, nature should be protected at all costs.",
          why="<i>Nature</i> in general takes no article.")],
    remember="General plural or uncountable: no article. Unique or limited by <i>of…</i>: <i>the</i>. Never a bare singular countable."),

dict(
    id="u10", where="Task 2 + Task 1", title="Countable or uncountable?",
    rule="""<p>Some nouns that are countable in other languages are <b>uncountable in English</b>. They take no <i>a</i>, no plural <i>-s</i> and a singular verb:</p>
<p><i>information, advice, research, evidence, knowledge, equipment, furniture, traffic, homework, progress, feedback, pollution, transport, accommodation, software, luggage</i></p>
<ul>
<li>Count them with a unit: <i>a piece of advice, a piece of research, a study, two items of equipment</i>.</li>
<li><b>much / little / less / an amount of</b> + uncountable. <b>many / few / fewer / a number of</b> + countable.</li>
<li><b>a lot of / plenty of / more / most / some</b> work with both.</li>
</ul>""",
    fits=[("Supporting an argument", "research / evidence (uncountable)", "<b>Research shows</b> that…"),
          ("Counting studies", "a study / studies", "<b>Several studies have</b> found…"),
          ("Quantities", "much / little + uncountable", "<b>Little progress</b> has been made."),
          ("Numbers of things", "many / fewer + countable", "<b>Fewer jobs</b> are available.")],
    pairs=[("Many researches show that…", "<b>Much research shows</b> (or <b>Many studies show</b>) that…", "<i>Research</i> is uncountable."),
           ("She gave me an advice.", "She gave me <b>some advice</b> / <b>a piece of advice</b>.", "<i>Advice</i> is uncountable."),
           ("These informations are useful.", "<b>This information is</b> useful.", "Uncountable: singular verb and <i>this</i>.")],
    band=("There are many evidences that the traffics is causing a lot of pollutions.",
          "There is considerable evidence that traffic is a major source of pollution.",
          "Every uncountable noun is now used correctly. One sentence free of three errors moves accuracy up a band."),
    qs=[Q("pick", "Students need more ___ about career choices.", opts=["informations", "information", "an information"], ans=1, why="<i>Information</i> is uncountable."),
        Q("pick", "There is ___ evidence to support this claim.", opts=["few", "little", "many"], ans=1, why="<i>Evidence</i> is uncountable: <i>little</i>."),
        Q("gap", "The equipment in many schools ___ (be) out of date.", acc=["is"], why="<i>Equipment</i> is uncountable: singular verb."),
        Q("spot", "Recent [[researches]] suggest that sleep affects memory.", fix="Recent research suggests that sleep affects memory. (Or: Recent studies suggest…)",
          why="<i>Research</i> has no plural. Use <i>research suggests</i> or <i>studies suggest</i>.")],
    remember="information, advice, research, evidence, equipment, knowledge, traffic, progress: no <i>a</i>, no <i>-s</i>, singular verb."),

dict(
    id="u11", where="Task 2 + Speaking", title="Subject–verb agreement in long sentences",
    rule="""<p>The verb agrees with the <b>head of the subject</b>, not with the noun nearest to it. Find the head by removing the phrases after it.</p>
<ul>
<li><i>The <b>use</b> of mobile phones in schools <b>is</b> …</i> (head: <i>use</i>)</li>
<li><i><b>One</b> of the main reasons <b>is</b> …</i> (head: <i>one</i>)</li>
<li><b>Everyone, each, every, nobody, somebody</b> → singular: <i>Everyone <b>has</b></i>.</li>
<li><b>There is</b> + singular / uncountable; <b>there are</b> + plural. <i>There <b>are</b> many reasons why…</i></li>
<li>Two subjects joined by <b>and</b> → plural: <i>Diet and exercise <b>are</b> both important.</i></li>
</ul>""",
    fits=[("Long noun phrase subject", "verb agrees with the first noun", "The <b>number</b> of hours children spend online <b>is</b> worrying."),
          ("<i>One of</i>", "singular verb", "<b>One</b> of the biggest problems <b>is</b> cost."),
          ("<i>There</i> + plural", "there are", "<b>There are</b> several solutions."),
          ("Gerund subject", "singular verb", "<b>Learning</b> languages <b>is</b> rewarding.")],
    pairs=[("One of the reason are cost.", "One of the <b>reasons is</b> cost.", "<i>One of the</i> + plural noun + singular verb."),
           ("The quality of public hospitals are declining.", "The quality of public hospitals <b>is</b> declining.", "Head noun: <i>quality</i>."),
           ("Everybody have a right to education.", "Everybody <b>has</b> a right to education.", "<i>Everybody</i> is singular.")],
    band=("The problems which the young generation face in big cities is many.",
          "The problems facing young people in big cities are numerous.",
          "A participle clause (<i>facing</i>) shortens the subject, which makes it easier to see that the head noun (<i>problems</i>) is plural."),
    qs=[Q("pick", "The impact of these policies on small businesses ___ been severe.", opts=["have", "has"], ans=1, why="Head: <i>impact</i>."),
        Q("pick", "There ___ a great deal of evidence that diet affects mood.", opts=["is", "are"], ans=0,
          why="After <i>there</i>, the verb agrees with what follows: <i>a great deal of evidence</i> is uncountable, so <i>there is</i>."),
        Q("gap", "Watching too much television ___ (affect) children's concentration.", acc=["affects"], why="A gerund subject is singular."),
        Q("spot", "Each of these solutions [[have]] advantages and disadvantages.", fix="Each of these solutions has advantages and disadvantages.", why="<i>Each</i> is singular.")],
    remember="Cover the <i>of…</i> phrase and find the head noun. <i>One of / each of / everyone</i>: singular."),

dict(
    id="u12", where="Task 2 · complex sentences", title="Relative clauses: who, which, that, whose, where, and commas",
    rule="""<ul>
<li><b>Defining</b> (tells you which one, no commas): <i>Students <b>who</b> work part-time often get lower grades.</i> <b>that</b> is allowed here.</li>
<li><b>Non-defining</b> (extra information, commas, never <b>that</b>): <i>My brother, <b>who</b> lives in Dhaka, is a doctor.</i></li>
<li><b>whose</b> for possession, <b>where</b> for places (or <b>in which</b>), <b>when</b> for times.</li>
<li><b>, which</b> can refer to the whole previous clause: <i>Prices rose, <b>which</b> led to protests.</i></li>
<li>Never repeat the subject or object: <i>the people who <s>they</s> live here</i>.</li>
</ul>""",
    fits=[("Define a group", "who / that, no commas", "Countries <b>that</b> invest in education grow faster."),
          ("Add a comment", ", which / , who", "Tokyo, <b>which</b> hosted the Olympics, …"),
          ("Comment on a whole idea", ", which + verb", "Fewer people cook, <b>which</b> affects health."),
          ("Formal place / situation", "in which / under which", "a system <b>in which</b> everyone pays")],
    pairs=[("The people who they live in cities have more stress.", "People who live in cities <b>have</b> more stress.",
            "No repeated subject after <i>who</i>, and no article for a general group."),
           ("Paris that is the capital of France is expensive.", "Paris<b>, which</b> is the capital of France<b>,</b> is expensive.",
            "Non-defining: commas and <i>which</i>, never <i>that</i>."),
           ("This is the town which I grew up.", "This is the town <b>where</b> I grew up (or <b>in which</b> I grew up).",
            "A place needs <i>where</i> or a preposition.")],
    band=("Some people work from home. This is good. It saves time.",
          "Many people now work from home, which saves them hours of commuting each week.",
          "Three simple sentences joined with a <i>, which</i> clause: more range, and no error risk."),
    qs=[Q("pick", "Children ___ parents read to them tend to read earlier.", opts=["who", "whose", "which"], ans=1, why="Possession (their parents): <i>whose</i>."),
        Q("pick", "The new law, ___ came into force in 2022, bans single-use plastic.", opts=["that", "which", "what"], ans=1,
          why="Commas mean non-defining: <i>which</i>, never <i>that</i>."),
        Q("gap", "Many young people move to cities, ___ leaves rural areas short of workers.", acc=["which"],
          why="<i>, which</i> refers back to the whole previous clause."),
        Q("spot", "Teachers [[which]] have more experience are often paid more.", fix="Teachers who have more experience are often paid more.",
          why="People: <i>who</i> (or <i>that</i> in a defining clause), never <i>which</i>.")],
    remember="Commas → <i>who / which</i>, never <i>that</i>. No commas → <i>who / which / that</i>. Never repeat the subject."),

dict(
    id="u13", where="Task 2 · arguments and solutions", title="Conditionals that match what you mean",
    rule="""<ul>
<li><b>First</b> (real, likely): <i>If + present, will / can / may</i>. <i>If taxes <b>rise</b>, people <b>will</b> spend less.</i></li>
<li><b>Second</b> (imagined, unlikely or a proposal): <i>If + past, would / could / might</i>. <i>If cars <b>were</b> banned, cities <b>would</b> be quieter.</i></li>
<li><b>Third</b> (past that did not happen): <i>If + had + past participle, would have + past participle</i>.</li>
<li><b>Zero</b> (always true): <i>If + present, present</i>. <i>If water <b>boils</b>, it <b>turns</b> to steam.</i></li>
<li>No <b>will</b> in the <i>if</i> clause. Formal alternatives: <i>unless, provided that, as long as, were … to</i>.</li>
</ul>""",
    fits=[("Likely result of a policy", "first", "If the government <b>invests</b> in rail, traffic <b>will</b> fall."),
          ("A suggestion / hypothetical", "second", "If schools <b>taught</b> cooking, diets <b>might</b> improve."),
          ("Speaking: regret", "third", "If I <b>had studied</b> harder, I <b>would have passed</b>."),
          ("Formal, band 9", "inversion", "<b>Were</b> governments to act now, …")],
    pairs=[("If the government will raise taxes, people will complain.", "If the government <b>raises</b> taxes, people will complain.",
            "No <i>will</i> in the <i>if</i> clause."),
           ("If I would be the president, I would ban guns.", "If I <b>were</b> the president, I would ban guns.",
            "Second conditional: past in the <i>if</i> clause (<i>were</i> for all persons in formal English)."),
           ("If they had prepared, they would pass.", "If they had prepared, they <b>would have passed</b>.",
            "Third conditional needs <i>would have</i> + past participle.")],
    band=("If people will use public transport, it will be good for environment.",
          "If more commuters switched to public transport, urban air quality would improve considerably.",
          "A second conditional frames the idea as a proposal, and the result is specific (<i>urban air quality</i>) instead of vague (<i>good for environment</i>)."),
    qs=[Q("pick", "If fast food ___ more heavily, people might choose healthier options.", opts=["is taxed", "were taxed", "will be taxed"], ans=1,
          why="<i>Might</i> in the result shows an imagined proposal: second conditional, past in the <i>if</i> clause."),
        Q("pick", "Unless action ___ soon, many species will disappear.", opts=["is taken", "will be taken", "was taken"], ans=0,
          why="<i>Unless</i> = <i>if not</i>, first conditional: present in that clause."),
        Q("gap", "If I had known about the scholarship, I ___ (apply).", acc=["would have applied", "could have applied", "might have applied"],
          why="Past that did not happen: third conditional."),
        Q("spot", "If people [[will recycle]] more, landfill sites will shrink.", fix="If people recycle more, landfill sites will shrink.",
          why="First conditional: present simple after <i>if</i>.")],
    remember="Likely: <i>if + present, will</i>. Imagined or proposed: <i>if + past, would</i>. Never <i>will</i> after <i>if</i>."),

dict(
    id="u14", where="Task 2 + Speaking", title="Hedging: being careful instead of absolute",
    rule="""<p>Strong claims with no evidence weaken an essay. Band 8–9 writers soften claims that cannot be proved.</p>
<ul>
<li>Modals: <b>may, might, could, can</b>. <i>This <b>may</b> lead to…</i></li>
<li>Tendency: <b>tend to, are likely to, are more likely to, often, in many cases</b>.</li>
<li>Limiters: <b>to some extent, arguably, in most cases, many (not all)</b>.</li>
<li>Recommendation: <b>should, ought to, it would be wise to</b>. Necessity: <b>must, need to</b> (use these sparingly).</li>
<li>Do not stack them: <i>it may possibly perhaps</i> is weaker, not more careful.</li>
</ul>""",
    fits=[("Predicting an effect", "may / could / is likely to", "Remote work <b>is likely to</b> reduce traffic."),
          ("Generalising about people", "tend to / many", "Teenagers <b>tend to</b> copy their peers."),
          ("Recommending", "should", "Schools <b>should</b> teach financial skills."),
          ("Conceding", "admittedly, to some extent", "<b>Admittedly</b>, this <b>could</b> raise costs.")],
    pairs=[("All young people are addicted to phones.", "<b>Many</b> young people <b>appear</b> to be addicted to their phones.",
            "<i>All</i> is easy to disprove. Soften the quantity and the verb."),
           ("This will definitely solve the problem.", "This <b>could</b> go a long way towards solving the problem.", "No policy definitely solves anything."),
           ("It might possibly perhaps help.", "It <b>may</b> help.", "One hedge is enough.")],
    band=("Video games make children violent.",
          "There is some evidence that violent video games may increase aggressive behaviour in certain children.",
          "Hedged on quantity (<i>some</i>), certainty (<i>may</i>) and scope (<i>certain children</i>). A balanced claim is harder to attack."),
    qs=[Q("pick", "Raising the price of cigarettes ___ reduce smoking among teenagers.", opts=["will surely", "is likely to", "must definitely"], ans=1,
          why="A prediction without proof: hedge it."),
        Q("pick", "Children who read for pleasure ___ do better at school.", opts=["always", "tend to", "are always going to"], ans=1, why="A tendency, not a law."),
        Q("gap", "Governments ___ (should / will) provide free childcare to working parents.", acc=["should"], why="A recommendation: <i>should</i>."),
        Q("spot", "Online courses [[will completely replace]] universities within ten years.", fix="Online courses may partly replace traditional universities in the coming decades.",
          why="An absolute prediction that nobody can prove. Soften the modal, the extent and the time.")],
    remember="Predictions and generalisations: <i>may, tend to, is likely to, many</i>. One hedge per claim."),

dict(
    id="u15", where="Task 2 + Task 1", title="Contrast: although, despite, however, but, whereas",
    rule="""<p>The linker decides the grammar that follows it.</p>
<ul>
<li><b>although / though / even though / whereas / while</b> + a full clause (subject + verb).</li>
<li><b>despite / in spite of</b> + a noun or <i>-ing</i>. <i>Despite <b>the cost</b> · despite <b>being</b> expensive · despite <b>the fact that</b> + clause.</i></li>
<li><b>However</b> starts a new sentence (or follows a semicolon) and takes a comma: <i>… cheap. <b>However,</b> it is slow.</i></li>
<li><b>but</b> joins two clauses inside one sentence.</li>
<li>Never pair <b>although … but</b>. Use one or the other.</li>
</ul>""",
    fits=[("Contrast inside a sentence", "although / while / whereas + clause", "<b>While</b> cars are convenient, they pollute."),
          ("Contrast with a noun", "despite + noun", "<b>Despite</b> its high cost, the plan…"),
          ("Contrast between sentences", ". However,", "<b>However,</b> this is not the whole story."),
          ("Task 1 comparison", "whereas", "Sales rose in May, <b>whereas</b> they fell in June.")],
    pairs=[("Although it is expensive, but many people buy it.", "<b>Although</b> it is expensive, many people buy it.", "One contrast word per contrast."),
           ("Despite it is expensive, many people buy it.", "<b>Despite being</b> expensive (or <b>Although it is</b> expensive), many people buy it.",
            "<i>Despite</i> cannot take a clause."),
           ("It is cheap, however it is slow.", "It is cheap<b>; however,</b> it is slow. / It is cheap, <b>but</b> it is slow.",
            "<i>However</i> after a comma creates a comma splice.")],
    band=("Some people think it is good. But others think it is bad.",
          "While some argue that the policy protects consumers, others maintain that it places an unfair burden on small businesses.",
          "A <i>while</i> clause holds both views in one balanced sentence, with precise reporting verbs."),
    qs=[Q("pick", "___ the heavy rain, the match went ahead.", opts=["Although", "Despite", "However"], ans=1, why="Followed by a noun phrase: <i>despite</i>."),
        Q("pick", "Rents in the capital doubled, ___ those in smaller towns stayed flat.", opts=["despite", "whereas", "however"], ans=1,
          why="Two full clauses compared: <i>whereas</i>."),
        Q("gap", "The plan is popular. ___, it may be too expensive to carry out.", acc=["however", "nevertheless", "nonetheless"],
          why="A new sentence with a contrast: <i>However,</i> (or <i>Nevertheless,</i>)."),
        Q("spot", "[[In spite of]] the government has spent billions, the roads are still poor.", fix="Although the government has spent billions, the roads are still poor. (Or: In spite of the billions spent…)",
          why="A full clause follows, so use <i>although</i>. <i>In spite of</i> needs a noun or <i>-ing</i>.")],
    remember="although + clause · despite + noun / -ing · <i>. However,</i> · never <i>although … but</i>."),

dict(
    id="u16", where="Task 2", title="Cause, effect and purpose",
    rule="""<ul>
<li><b>because / as / since</b> + clause. <b>because of / due to / owing to / as a result of</b> + noun.</li>
<li><b>so</b> joins two clauses with a comma: <i>…, so…</i> <b>Therefore / As a result / Consequently</b> start a new sentence (or follow a semicolon).</li>
<li>Purpose: <b>to / in order to / so as to</b> + verb; <b>so that</b> + clause (often with <i>can / could / will</i>).</li>
<li><b>lead to / result in / cause</b> + noun: <i>Poverty <b>leads to</b> crime.</i> Not <i>leads to increase</i>.</li>
<li><b>so … that / such a … that</b> for a result of degree.</li>
</ul>""",
    fits=[("Reason as a clause", "because + clause", "<b>because</b> housing is expensive"),
          ("Reason as a noun", "due to + noun", "<b>due to</b> the high cost of housing"),
          ("Consequence", "This leads to + noun", "<b>This leads to</b> overcrowding."),
          ("Purpose", "so that + can", "<b>so that</b> students <b>can</b> study at home")],
    pairs=[("Due to people are busy, they eat fast food.", "<b>Because</b> people are busy (or <b>Due to</b> busy lifestyles), they eat fast food.",
            "<i>Due to</i> + noun, never a clause."),
           ("This leads to increase crime.", "This leads to <b>an increase in</b> crime.", "<i>Lead to</i> + noun phrase (the <i>to</i> is a preposition)."),
           ("Many people study abroad for getting a good job.", "Many people study abroad <b>to get</b> (or <b>in order to get</b>) a good job.",
            "Purpose of an action: <i>to</i> + base verb.")],
    band=("People are busy so they don't cook so they eat junk food so they get fat.",
          "Longer working hours leave many families little time to cook, which in turn leads to greater reliance on processed food and, ultimately, higher rates of obesity.",
          "A cause–effect chain with <i>leave…, which leads to…</i>: one controlled sentence instead of three <i>so</i>s."),
    qs=[Q("pick", "Many flights were cancelled ___ the storm.", opts=["because", "because of", "so that"], ans=1, why="A noun follows: <i>because of</i>."),
        Q("pick", "Cities should build more cycle lanes ___ people can travel safely.", opts=["so that", "in order to", "due to"], ans=0,
          why="A clause with a new subject and <i>can</i>: <i>so that</i>."),
        Q("gap", "Deforestation can result ___ soil erosion.", acc=["in"], why="<i>Result in</i> + the effect (<i>result from</i> + the cause)."),
        Q("spot", "Unemployment is rising, [[therefore]] many graduates are moving abroad.", fix="Unemployment is rising; therefore, many graduates are moving abroad. (Or: …rising, so many graduates…)",
          why="<i>Therefore</i> cannot join two clauses with a comma. Use a semicolon or full stop, or use <i>so</i>.")],
    remember="because + clause · because of / due to + noun · <i>, so</i> · <i>. Therefore,</i> · to / so that for purpose."),

dict(
    id="u17", where="Task 2 · accuracy", title="Sentence boundaries: comma splices, run-ons and fragments",
    rule="""<p>Examiners count error-free sentences. These three errors break a sentence even when every word is right.</p>
<ul>
<li><b>Comma splice:</b> two full sentences joined only by a comma. <i>Prices rose, people complained.</i> ✗</li>
<li><b>Run-on:</b> two sentences with nothing between them, or a long chain of <i>and</i>.</li>
<li><b>Fragment:</b> half a sentence standing alone. <i>Because it is cheaper.</i> ✗ <i>For example, the USA.</i> ✗</li>
<li>Fixes: a full stop · a semicolon · a conjunction (<i>and, but, so, because, although</i>) · a relative or participle clause.</li>
</ul>""",
    fits=[("Two linked sentences", "; or . ", "Prices rose<b>;</b> people complained."),
          ("Cause and effect", "conjunction", "Prices rose, <b>so</b> people complained."),
          ("Adding an example", "full sentence", "<b>For example, the USA has</b> high obesity rates."),
          ("Adding a reason", "attach it to the main clause", "Many choose buses <b>because they are cheaper</b>.")],
    pairs=[("Technology is useful, it saves time.", "Technology is useful<b>;</b> it saves time. / Technology is useful <b>because</b> it saves time.",
            "Comma splice: a comma cannot join two sentences."),
           ("Many people prefer cars. Because they are faster.", "Many people prefer cars <b>because</b> they are faster.",
            "A <i>because</i> clause cannot stand alone."),
           ("For example the UK.", "For example, <b>the UK has introduced</b> a sugar tax.", "An example needs a full sentence (subject + verb).")],
    band=("Some people say exams are stressful, they are not fair, students can have a bad day.",
          "Some argue that exams are unfair because a single bad day can undo months of work.",
          "Three spliced clauses become one sentence with a clear reason. Shorter and error-free."),
    qs=[Q("pick", "Which is a correct sentence?", opts=["Cities are crowded, many people still move there.", "Cities are crowded, yet many people still move there.", "Cities are crowded. Yet many people still moving there."], ans=1,
          why="<i>Yet</i> is a conjunction, so the comma is fine. Option A is a comma splice; option C has no finite verb in the second part."),
        Q("pick", "Which is a fragment?", opts=["Although the plan failed.", "The plan failed.", "Although the plan failed, it taught us a lot."], ans=0,
          why="An <i>although</i> clause needs a main clause."),
        Q("gap", "Fill in the punctuation: Online learning is flexible___ however, it can be isolating.", acc=[";"],
          why="A semicolon before <i>however</i> joins the two sentences correctly."),
        Q("spot", "Smoking is banned in restaurants[[,]] this has improved public health.", fix="Smoking is banned in restaurants, which has improved public health. (Or: …restaurants; this has…)",
          why="A comma splice. Use a semicolon, a full stop, or <i>, which</i>.")],
    remember="Comma + new subject + verb = splice. Join with <i>;</i>, <i>.</i>, a conjunction or <i>, which</i>. Every sentence needs a main verb."),

dict(
    id="u18", where="Task 2 · academic style", title="Noun phrases (nominalisation)",
    rule="""<p>Academic writing packs ideas into <b>nouns</b>. This lets one sentence carry more information and sounds more objective.</p>
<ul>
<li>verb → noun: <i>decide → <b>decision</b>, increase → <b>an increase in</b>, fail → <b>failure</b>, reduce → <b>reduction</b></i></li>
<li>adjective → noun: <i>important → <b>importance</b>, available → <b>availability</b>, difficult → <b>difficulty</b></i></li>
<li>Build the phrase: <b>the + noun + of / in + …</b>: <i><b>the rapid growth of</b> online shopping</i>.</li>
<li>Do not overdo it. Two or three per paragraph is enough; a sentence of nothing but nouns is hard to read.</li>
</ul>""",
    fits=[("Topic sentence", "the + noun + of", "<b>The rise of</b> remote work has reshaped cities."),
          ("Cause", "noun phrase as subject", "<b>A lack of</b> affordable housing drives people away."),
          ("Conclusion", "nominalised summary", "<b>The introduction of</b> a sugar tax is justified."),
          ("Task 1 overview", "noun of change", "<b>The most striking feature</b> is the fall in coal use.")],
    pairs=[("When people use cars a lot it makes the air dirty.", "<b>Heavy car use</b> pollutes the air.", "The clause becomes a noun phrase subject."),
           ("Because the government decided to cut funding, schools suffered.", "<b>The government's decision to cut funding</b> hurt schools.", "<i>decided → decision</i>."),
           ("It is important that children are safe.", "<b>Children's safety</b> is paramount.", "Adjective clause → noun phrase.")],
    band=("Because more and more people are buying things on the internet, shops in town centres are closing.",
          "The rapid growth of online shopping has led to the closure of many town-centre shops.",
          "Two noun phrases (<i>the rapid growth of…, the closure of…</i>) joined by one verb: denser and more academic."),
    qs=[Q("pick", "Choose the best noun phrase: \"Prices increased sharply, which worried consumers.\" → ___ worried consumers.", opts=["Prices increasing sharply", "The sharp increase in prices", "The sharp increasing of prices"], ans=1,
          why="<i>A sharp increase in</i> + noun is the standard nominal form."),
        Q("pick", "___ of clean water remains a problem in many rural areas.", opts=["The available", "The availability", "Availably"], ans=1, why="A noun is needed after <i>the</i>."),
        Q("gap", "The government's ___ (fail) to act has angered voters.", acc=["failure"], why="<i>fail → failure</i>."),
        Q("spot", "The [[reduce]] of plastic waste is a priority for many cities.", fix="The reduction of plastic waste is a priority for many cities.", why="A noun is needed: <i>reduction</i>.")],
    remember="Turn a clause into <i>the + noun + of</i> when it is the subject of a bigger idea. Two or three per paragraph."),

dict(
    id="u19", where="Task 2 · advanced range", title="Participle clauses (and the dangling modifier)",
    rule="""<p>A participle clause replaces a full clause with an <i>-ing</i> or <i>-ed</i> form. It is one of the quickest ways to show range.</p>
<ul>
<li><b>-ing</b> (active): <i><b>Living</b> in a city, I rarely drive.</i> = <i>Because I live…</i></li>
<li><b>-ed</b> (passive): <i><b>Built</b> in 1890, the bridge is still in use.</i> = <i>which was built…</i></li>
<li><b>Having + past participle</b> (earlier action): <i><b>Having finished</b> school, many teenagers…</i></li>
<li>Reduced relative clauses: <i>students <b>living</b> abroad, products <b>made</b> in China</i>.</li>
<li>The rule that matters: the participle's subject <b>must be the subject of the main clause</b>. Otherwise it "dangles".</li>
</ul>""",
    fits=[("Shorter relative clause", "noun + -ing / -ed", "People <b>working</b> long hours…"),
          ("Background information", "-ed clause at the start", "<b>Introduced</b> in 2015, the tax…"),
          ("Sequence", "Having + past participle", "<b>Having analysed</b> both views, I believe…"),
          ("Result", ", -ing", "Prices fell, <b>making</b> homes more affordable.")],
    pairs=[("Walking along the beach, the sun was very hot.", "<b>Walking</b> along the beach, <b>I</b> found the sun very hot.",
            "Dangling: the sun was not walking. The main subject must be the walker."),
           ("Students who are living in dormitories save money.", "Students <b>living</b> in dormitories save money.", "Reduced relative clause."),
           ("After they finished school, many of them travel.", "<b>Having finished</b> school, many young people travel.", "Earlier action: <i>having + past participle</i>.")],
    band=("The museum was opened in 1990. It attracts many visitors. It is the most popular attraction.",
          "Opened in 1990, the museum now attracts more visitors than any other attraction in the city.",
          "Two sentences folded into an <i>-ed</i> participle clause."),
    qs=[Q("pick", "___ by the results, the researchers repeated the experiment.", opts=["Surprising", "Surprised", "Having surprised"], ans=1,
          why="The researchers were surprised (passive meaning): <i>-ed</i>."),
        Q("pick", "Which sentence is correct?", opts=["Having read the report, the problem was clear.", "Having read the report, I understood the problem.", "Reading the report, the problem became clear."], ans=1,
          why="Only in B is the subject of the main clause (<i>I</i>) the person who read."),
        Q("gap", "Products ___ (make) from recycled materials are becoming more popular.", acc=["made"], why="Passive meaning (<i>which are made</i>): <i>-ed</i> participle."),
        Q("spot", "Fewer people bought cars, [[reduced]] traffic in the city centre.", fix="Fewer people bought cars, reducing traffic in the city centre.",
          why="A result clause with active meaning needs <i>-ing</i>: <i>, reducing…</i>")],
    remember="-ing = active, -ed = passive, having + done = earlier. Check that the participle's subject is the main subject."),

dict(
    id="u20", where="Task 2 + Speaking", title="Verb patterns: -ing or to + verb?",
    rule="""<ul>
<li>+ <b>-ing</b>: <i>avoid, enjoy, consider, suggest, admit, deny, risk, keep, mind, involve, can't help</i>.</li>
<li>+ <b>to</b> + verb: <i>decide, plan, hope, aim, refuse, afford, manage, tend, fail, agree</i>.</li>
<li>+ object + <b>to</b>: <i>allow, encourage, enable, force, persuade, require, want, ask</i> sb <b>to do</b>.</li>
<li>After a <b>preposition</b> → <b>-ing</b>: <i>interested in learning, instead of driving, by investing</i>. Watch for <b>to</b> as a preposition: <i>look forward to <b>meeting</b>, be used to <b>living</b>, contribute to <b>reducing</b></i>.</li>
<li><b>suggest / recommend</b>: <i>suggest <b>doing</b></i> or <i>suggest <b>that</b> sb <b>(should) do</b></i>. Never <i>suggest sb to do</i>.</li>
</ul>""",
    fits=[("Essay solutions", "encourage / enable sb to", "Tax breaks <b>encourage</b> firms <b>to hire</b>."),
          ("Method", "by + -ing", "<b>By investing</b> in rail…"),
          ("Recommending", "suggest that / recommend + -ing", "I <b>recommend introducing</b> a fee."),
          ("Speaking, future plans", "plan / hope to", "I'm <b>hoping to study</b> abroad.")],
    pairs=[("I look forward to hear from you.", "I look forward to <b>hearing</b> from you.", "<i>To</i> here is a preposition: <i>-ing</i>."),
           ("Experts suggest people to exercise daily.", "Experts <b>suggest that people exercise</b> daily.", "<i>Suggest</i> never takes object + <i>to</i>."),
           ("The internet allows to work from home.", "The internet allows <b>people to work</b> from home.", "<i>Allow</i> needs an object before <i>to</i>.")],
    band=("Government should make people to use less water.",
          "Governments should encourage households to use less water by introducing tiered pricing.",
          "Correct object + <i>to</i> pattern, plus <i>by + -ing</i> to name the method."),
    qs=[Q("pick", "Many young people cannot afford ___ a house.", opts=["buying", "to buy", "buy"], ans=1, why="<i>Afford to do</i>."),
        Q("pick", "Doctors recommend ___ sugary drinks.", opts=["to avoid", "avoiding", "avoid of"], ans=1,
          why="<i>Recommend + -ing</i> (or <i>recommend that people avoid</i>)."),
        Q("gap", "Cycling to work can contribute to ___ (reduce) emissions.", acc=["reducing"], why="<i>Contribute to</i> + <i>-ing</i>: <i>to</i> is a preposition."),
        Q("spot", "Online platforms enable [[to learn]] at their own pace.", fix="Online platforms enable learners to learn at their own pace.",
          why="<i>Enable</i> needs an object: <i>enable someone to do</i>.")],
    remember="avoid / enjoy / suggest + -ing · decide / afford / aim + to · allow / enable / encourage + sb + to · preposition + -ing."),

dict(
    id="u21", where="Task 2 · accuracy", title="Parallel structure",
    rule="""<p>Items joined by <b>and, or, but, both … and, either … or, not only … but also, rather than</b> must have the <b>same grammatical form</b>.</p>
<ul>
<li>Lists: <i>reading, writing and <b>speaking</b></i>, not <i>reading, writing and to speak</i>.</li>
<li><i>not only <b>reduces</b> costs but also <b>improves</b> safety</i>: verb with verb.</li>
<li>Comparisons: <i>It is better <b>to prevent</b> crime than <b>to punish</b> it.</i></li>
</ul>""",
    fits=[("A list of benefits", "same form for each item", "It <b>saves</b> time, <b>cuts</b> costs and <b>reduces</b> stress."),
          ("Two-part emphasis", "not only X but also Y", "not only <b>cheaper</b> but also <b>safer</b>"),
          ("Preference", "rather than + same form", "<b>investing</b> in buses rather than <b>building</b> roads"),
          ("Paired choice", "either X or Y", "either <b>taxing</b> fuel or <b>banning</b> cars")],
    pairs=[("Exercise improves health, mood and helps you sleep.", "Exercise improves health <b>and</b> mood and helps you sleep. / Exercise <b>improves</b> health, <b>lifts</b> mood and <b>aids</b> sleep.",
            "The third item broke the pattern (noun, noun, verb phrase)."),
           ("The plan is not only expensive but also it is slow.", "The plan is not only <b>expensive</b> but also <b>slow</b>.", "Adjective with adjective."),
           ("I prefer walking to drive.", "I prefer <b>walking</b> to <b>driving</b>.", "Same form on both sides.")],
    band=("Uniforms are good because they are cheap, students look equal and for discipline.",
          "School uniforms are inexpensive, reduce visible differences in wealth and encourage discipline.",
          "Three parallel verb phrases, so the list reads cleanly."),
    qs=[Q("pick", "The scheme aims to cut waste, save energy and ___ .", opts=["reducing costs", "reduce costs", "cost reduction"], ans=1,
          why="Matches <i>cut</i> and <i>save</i>: base verb."),
        Q("pick", "Remote work is not only convenient but also ___ .", opts=["it saves money", "economical", "saving money"], ans=1, why="Adjective after <i>but also</i>, to match <i>convenient</i>."),
        Q("gap", "It is often easier to prevent illness than ___ (cure) it.", acc=["to cure"], why="<i>to prevent … than to cure</i>."),
        Q("spot", "The course teaches students how to plan, research and [[writing]] essays.", fix="The course teaches students how to plan, research and write essays.",
          why="The list after <i>how to</i> is base verbs: <i>plan, research, write</i>.")],
    remember="Every item after <i>and, or, not only … but also, rather than</i> takes the same form."),

dict(
    id="u22", where="Task 2 · band 8–9 range", title="Emphasis: cleft sentences and inversion (use once, correctly)",
    rule="""<p>These structures show range, but only when they are correct and used rarely: one or two per essay.</p>
<ul>
<li><b>It-cleft:</b> <i><b>It is</b> the cost of housing <b>that</b> drives young people away.</i></li>
<li><b>What-cleft:</b> <i><b>What</b> concerns me most <b>is</b> the effect on children.</i></li>
<li><b>Negative inversion</b> (auxiliary before the subject): <i><b>Not only does</b> it save money, but it also…</i> · <i><b>Only by</b> investing in education <b>can</b> we…</i> · <i><b>Rarely is</b> this discussed.</i></li>
<li>Conditional inversion: <i><b>Were</b> governments to act…, <b>Had</b> they acted…, <b>Should</b> you need…</i></li>
</ul>""",
    fits=[("Thesis emphasis", "What-cleft", "<b>What</b> matters most <b>is</b> access."),
          ("Contrasting a cause", "It-cleft", "<b>It is</b> poverty, not laziness, <b>that</b>…"),
          ("Adding a second benefit", "Not only + inversion", "<b>Not only does</b> it…, but it also…"),
          ("Conclusion", "Only by + inversion", "<b>Only by</b> acting together <b>can</b> we…")],
    pairs=[("Not only it saves money but also time.", "Not only <b>does it save</b> money, <b>but it also saves</b> time.",
            "After a fronted <i>not only</i>, invert the auxiliary and subject."),
           ("Only by education we can solve this.", "Only by <b>improving</b> education <b>can we</b> solve this.", "<i>Only by</i> at the start → inversion."),
           ("What I think is important it is education.", "What I think is important <b>is</b> education.", "No extra <i>it</i> after a what-clause.")],
    band=("Education is the most important thing to fix this problem.",
          "It is only through better education that this problem can be addressed in the long term.",
          "An it-cleft puts the focus on <i>education</i>, and the passive keeps the sentence formal. Once is enough."),
    qs=[Q("pick", "Not only ___ pollution, but it also wastes time.", opts=["traffic causes", "does traffic cause", "traffic does cause"], ans=1,
          why="Fronted <i>not only</i> → auxiliary + subject."),
        Q("pick", "___ worries parents most is online safety.", opts=["That", "What", "It"], ans=1, why="A what-cleft: <i>What … is …</i>."),
        Q("gap", "Rarely ___ (be) such a simple solution so effective.", acc=["is"], why="<i>Rarely</i> at the front → inversion: <i>Rarely is …</i>"),
        Q("spot", "Only by working together [[we can]] tackle climate change.", fix="Only by working together can we tackle climate change.", why="<i>Only by…</i> at the start: invert to <i>can we</i>.")],
    remember="Inversion after a fronted negative: <i>Not only does…, Only by … can…, Rarely is…</i>. One or two per essay, never forced."),
]
