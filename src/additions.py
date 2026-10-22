"""More examples for every grammar unit: 3 extra right/wrong pairs, 1 extra band 7 -> band 9 example, 4 extra questions.
Merged into the units by build.py (questions are appended, so earlier saved answers keep their place)."""
from content_task1 import Q

ADD = {
# ------------------------------------------------------------------ Task 1
"u1": dict(
    pairs=[("Last year, the figure is 40%.", "Last year, the figure <b>was</b> 40%.", "<i>Last year</i> is a finished time: past simple."),
           ("The graph illustrated the sales of three products.", "The graph <b>illustrates</b> the sales of three products.",
            "The graph exists now, so the introduction is present simple. Only the data verbs move into the past."),
           ("The percentage of women is rising from 20% to 35% between 1990 and 2010.", "The percentage of women <b>rose</b> from 20% to 35% between 1990 and 2010.",
            "Both dates are in the past: past simple.")],
    bands=[("In 2000 the sales was 50 and in 2005 the sales is 80.", "Sales stood at 50 units in 2000 and had climbed to 80 by 2005.",
            "The tense follows the dates, and <i>had climbed … by 2005</i> shows the change reaching a point in the past.")],
    qs=[Q("pick", "Between 2000 and 2020, the average temperature ___ by two degrees.", opts=["rises", "rose", "has risen"], ans=1, why="Both dates are finished: past simple."),
        Q("pick", "Experts say that by 2060 the global population ___ 10 billion.", opts=["reached", "is expected to reach", "has reached"], ans=1, why="2060 is a forecast: projection language."),
        Q("gap", "In 1990, only 5% of households ___ (own) a computer.", acc=["owned"], why="A past year with a state verb: past simple."),
        Q("spot", "According to the forecast, house prices [[rose]] sharply by 2030.", fix="According to the forecast, house prices will rise sharply by 2030.", why="2030 is the future: <i>will rise</i> or <i>are expected to rise</i>.")]),

"u2": dict(
    pairs=[("I have seen that film last week.", "I <b>saw</b> that film last week.", "<i>Last week</i> is finished: past simple."),
           ("She is a teacher for ten years.", "She <b>has been</b> a teacher for ten years.", "A state that began in the past and continues now: present perfect with <i>for</i>."),
           ("Have you ever went to Japan?", "Have you ever <b>been</b> to Japan?", "The present perfect needs the past participle: <i>been</i>, not <i>went</i>.")],
    bands=[("I started learning English when I was ten, and I still learn it.", "I started learning English at the age of ten and have been studying it ever since.",
            "Past simple for the start, present perfect continuous for <i>up to now</i>, and <i>ever since</i> links them.")],
    qs=[Q("pick", "Scientists ___ a new species of frog in 2021.", opts=["discovered", "have discovered", "discover"], ans=0, why="<i>In 2021</i> is a finished time: past simple."),
        Q("pick", "I ___ my phone three times this month.", opts=["lost", "have lost", "was losing"], ans=1, why="<i>This month</i> has not finished yet: present perfect."),
        Q("gap", "She ___ (work) here since 2015.", acc=["has worked", "has been working", "'s worked", "’s worked", "'s been working", "’s been working"], why="<i>Since</i> + a starting point: present perfect."),
        Q("spot", "I [[am]] interested in music since I was a child.", fix="I have been interested in music since I was a child.", why="<i>Since</i> needs the present perfect, not present simple.")]),

"u3": dict(
    pairs=[("The oranges pick by hand.", "The oranges <b>are picked</b> by hand.", "A passive needs <i>be</i> as well as the past participle."),
           ("The mixture is heating to 100°C.", "The mixture <b>is heated</b> to 100°C.", "A process passive uses the past participle, not <i>-ing</i>."),
           ("Next, the bottles are been washed.", "Next, the bottles <b>are washed</b>.", "Only one form of <i>be</i>: <i>are washed</i>.")],
    bands=[("First, farmers grow the cocoa, then they pick it, then they dry it.", "Cocoa beans are first harvested and then left to dry in the sun for about a week before being shipped to factories.",
            "Passive verbs, a time phrase and <i>before being shipped</i> (a passive <i>-ing</i> form) pack several stages into one sentence.")],
    qs=[Q("pick", "Finally, the finished cars ___ to showrooms.", opts=["deliver", "are delivered", "are delivering"], ans=1, why="The cars do not deliver themselves: passive."),
        Q("pick", "The caterpillar ___ a chrysalis after about two weeks.", opts=["forms", "is formed", "has been formed"], ans=0, why="A natural change that nobody carries out: active."),
        Q("gap", "The sugar cane ___ (crush) to extract the juice.", acc=["is crushed"], why="Done to the cane: present simple passive."),
        Q("spot", "In the pond, the eggs [[are hatched]] after two weeks.", fix="In the pond, the eggs hatch after two weeks.", why="Hatching happens by itself in nature: active.")]),

"u4": dict(
    pairs=[("The cost fell at 20% in 2010.", "The cost fell <b>by</b> 20% in 2010.", "The size of the change takes <i>by</i>."),
           ("Sales remained stable on 500 units.", "Sales remained stable <b>at</b> 500 units.", "A level figure takes <i>at</i>: <i>stood at, remained at</i>."),
           ("There was a decrease on unemployment.", "There was a decrease <b>in</b> unemployment.", "<i>A decrease in</i> + the thing that changed.")],
    bands=[("The number of visitors went up a lot in July and went down in August.", "Visitor numbers soared to a peak of 90,000 in July before dropping back to 60,000 in August.",
            "Precise verbs, the end figure with <i>to</i> and a clear order with <i>before + -ing</i>.")],
    qs=[Q("pick", "Imports remained steady ___ 3 million tonnes.", opts=["by", "at", "with"], ans=1, why="A level figure: <i>at</i>."),
        Q("pick", "There was a gradual decline ___ the birth rate.", opts=["of", "in", "on"], ans=1, why="<i>A decline in</i> + the thing."),
        Q("gap", "The temperature rose ___ 4°C, from 14°C to 18°C.", acc=["by"], why="4°C is the size of the change: <i>by</i>."),
        Q("spot", "The price [[raised]] from $2 to $5 in 2010.", fix="The price rose from $2 to $5 in 2010.", why="No object, so <i>rose</i>. <i>Raised</i> needs someone doing the raising.")]),

"u5": dict(
    pairs=[("Cars were more cheaper than trains.", "Cars were <b>cheaper</b> than trains.", "Short adjectives take <i>-er</i> alone."),
           ("The figure for men was same as women.", "The figure for men was <b>the same as</b> that for women.", "<i>The same as</i> needs <i>the</i> and <i>as</i>."),
           ("Rice was the more popular grain.", "Rice was <b>the most popular</b> grain.", "Three or more things: the superlative.")],
    bands=[("Men earned more than women. Women earned less than men.", "Men earned considerably more than women, whose pay was roughly a fifth lower.",
            "One sentence with a graded comparison, instead of the same fact said twice.")],
    qs=[Q("pick", "China produced ___ the USA.", opts=["twice as much steel as", "twice more steel than", "two times much steel as"], ans=0, why="Uncountable: <i>twice as much … as</i>."),
        Q("pick", "Of the five countries, Japan had ___ unemployment.", opts=["lower", "the lowest", "the lower"], ans=1, why="One out of five: superlative."),
        Q("gap", "Spending on food was ___ (high) in 2010 than in 2000.", acc=["higher"], why="Short adjective + <i>than</i>: <i>higher</i>."),
        Q("spot", "Bus travel was [[more cheaper]] than train travel.", fix="Bus travel was cheaper than train travel.", why="Never <i>more</i> and <i>-er</i> together.")]),

"u6": dict(
    pairs=[("The amount of students grew.", "The <b>number</b> of students grew.", "Students are countable: <i>number</i>."),
           ("A number of people was surprised.", "A number of people <b>were</b> surprised.", "<i>A number of</i> means several, so the verb is plural."),
           ("The proportions of men was higher.", "The <b>proportion</b> of men was higher.", "One share, so <i>proportion</i>, singular.")],
    bands=[("A lot of people go to the gym and the people is increasing.", "The number of people going to the gym has risen steadily, and about one in five adults now has a membership.",
            "The correct head noun, a reduced relative clause (<i>going</i>) and a concrete fraction.")],
    qs=[Q("pick", "The percentage of women in senior jobs ___ risen.", opts=["have", "has"], ans=1, why="Head noun <i>percentage</i>: singular."),
        Q("pick", "A number of students ___ complained about the fees.", opts=["has", "have"], ans=1, why="<i>A number of</i> = several: plural."),
        Q("gap", "The ___ (amount / number) of people with a degree doubled.", acc=["number"], why="People are countable."),
        Q("spot", "The number of accidents [[were]] lower in 2010.", fix="The number of accidents was lower in 2010.", why="Head noun <i>number</i>: singular.")]),

"u7": dict(
    pairs=[("a three hours journey", "a <b>three-hour</b> journey", "Number + noun before a noun: singular, hyphenated."),
           ("It cost nearly 3 thousands dollars.", "It cost nearly <b>3,000</b> dollars.", "No <i>-s</i> after a number: <i>three thousand</i>."),
           ("Around of 40% of the students passed.", "<b>Around</b> 40% of the students passed.", "No <i>of</i> after <i>around</i>.")],
    bands=[("The rate was 24.8% in 1980 and 51.2% in 2010.", "The rate roughly doubled, from about a quarter in 1980 to just over half in 2010.",
            "Rounded figures turn into fractions, so the trend is clear at a glance.")],
    qs=[Q("pick", "She completed a ___ course.", opts=["six-month", "six-months", "six months"], ans=0, why="Number + noun before another noun: singular."),
        Q("pick", "The population is now ___.", opts=["nearly 3 millions", "nearly 3 million", "nearly 3 million of people"], ans=1, why="<i>Million</i> has no <i>-s</i> after a number."),
        Q("gap", "They signed a ten-___ contract. (year)", acc=["year"], why="Inside a noun phrase: <i>ten-year</i>, singular."),
        Q("spot", "It was a [[two-hours]] flight.", fix="It was a two-hour flight.", why="Singular inside the phrase.")]),

"u8": dict(
    pairs=[("The Germany spent more.", "<b>Germany</b> spent more.", "No article with most country names."),
           ("In the 2010, sales rose.", "In 2010, sales rose.", "A single year takes no <i>the</i>."),
           ("The oil was the most used fuel.", "<b>Oil</b> was the most used fuel.", "A general uncountable noun: no article.")],
    bands=[("In graph the sales of mobile is higher than the computers.", "In the graph, sales of mobile phones were higher than sales of computers.",
            "Articles, plurals and verb agreement fixed. No new vocabulary was needed.")],
    qs=[Q("pick", "___ Netherlands had the highest cycling rate.", opts=["—", "The", "A"], ans=1, why="<i>The Netherlands</i> is a plural name."),
        Q("pick", "Coffee consumption rose in ___.", opts=["the 2000s", "2000s", "a 2000s"], ans=0, why="Decades take <i>the</i>."),
        Q("gap", "There was ___ (a / an) unusual rise in 1998.", acc=["an"], why="<i>Unusual</i> begins with a vowel sound."),
        Q("spot", "[[The]] India has the largest youth population.", fix="India has the largest youth population.", why="No article with <i>India</i>.")]),

# ------------------------------------------------------------------ Task 2
"u9": dict(
    pairs=[("The money can't buy the happiness.", "<b>Money</b> can't buy <b>happiness</b>.", "General ideas: no article."),
           ("The young people are more creative than the old people.", "<b>Young people</b> are more creative than <b>old people</b>.", "A general group: no article."),
           ("A homework is important.", "<b>Homework</b> is important.", "Uncountable: no <i>a</i>.")],
    bands=[("The pollution is very big problem in the cities.", "Pollution is a serious problem in many cities.", "<i>Pollution</i> in general takes no article. <i>A serious problem</i> needs <i>a</i>.")],
    qs=[Q("pick", "___ are more likely to use social media than older adults.", opts=["Teenagers", "The teenagers", "A teenagers"], ans=0, why="A general plural: no article."),
        Q("pick", "Many people believe that ___ will solve our energy problems.", opts=["the technology", "technology", "a technology"], ans=1, why="General uncountable idea."),
        Q("gap", "___ sun is the source of most of our energy.", acc=["the"], why="One unique sun: <i>the</i>."),
        Q("spot", "[[The]] crime has increased in recent years.", fix="Crime has increased in recent years.", why="<i>Crime</i> in general takes no article.")]),

"u10": dict(
    pairs=[("The furnitures are expensive.", "The <b>furniture is</b> expensive.", "<i>Furniture</i> is uncountable."),
           ("The traffic are heavy.", "The <b>traffic is</b> heavy.", "Uncountable: singular verb."),
           ("She has a lot of homeworks.", "She has a lot of <b>homework</b>.", "No plural <i>-s</i>.")],
    bands=[("The advices from the teachers are very useful for knowledges.", "The teachers' advice is very useful for building knowledge.", "Two uncountable nouns used correctly, with a verb that agrees.")],
    qs=[Q("pick", "I need some ___ about courses.", opts=["advices", "advice", "an advice"], ans=1, why="<i>Advice</i> is uncountable."),
        Q("pick", "How ___ progress has been made?", opts=["many", "much"], ans=1, why="Uncountable: <i>much</i>."),
        Q("gap", "The news ___ (be) shocking.", acc=["is", "was"], why="<i>News</i> is uncountable: a singular verb."),
        Q("spot", "We bought new [[furnitures]] for the office.", fix="We bought new furniture for the office.", why="<i>Furniture</i> has no plural.")]),

"u11": dict(
    pairs=[("The list of problems are long.", "The list of problems <b>is</b> long.", "Head noun: <i>list</i>."),
           ("Neither of the plans are good.", "Neither of the plans <b>is</b> good.", "<i>Neither</i> is singular."),
           ("Diet, as well as exercise, are important.", "Diet, as well as exercise, <b>is</b> important.", "<i>As well as</i> does not make the subject plural.")],
    bands=[("The things that young people are facing in cities are a lot.", "Young people in cities face numerous problems.", "A clear plural subject, one agreeing verb and a precise noun.")],
    qs=[Q("pick", "The effects of climate change ___ already visible.", opts=["is", "are"], ans=1, why="Head noun <i>effects</i>: plural."),
        Q("pick", "Everyone in the class ___ passed.", opts=["have", "has"], ans=1, why="<i>Everyone</i> is singular."),
        Q("gap", "Each of the students ___ (receive) a certificate every year.", acc=["receives"], why="<i>Each</i> is singular."),
        Q("spot", "The main cause of obesity [[are]] poor diet.", fix="The main cause of obesity is poor diet.", why="Head noun <i>cause</i>: singular.")]),

"u12": dict(
    pairs=[("The man which lives next door is a doctor.", "The man <b>who</b> lives next door is a doctor.", "People: <i>who</i>."),
           ("The book, that I read last week, was long.", "The book<b>, which</b> I read last week<b>,</b> was long. (Or: The book <b>that</b> I read last week was long.)", "Commas mean <i>which</i>; <i>that</i> needs no commas."),
           ("I met a woman whose her son is a pilot.", "I met a woman <b>whose</b> son is a pilot.", "<i>Whose</i> already means <i>her</i>.")],
    bands=[("Many students live in dormitories. The dormitories are cheap.", "Many students live in dormitories, which are cheap.", "Two short sentences become one with a <i>, which</i> clause.")],
    qs=[Q("pick", "The city ___ I was born has changed a lot.", opts=["where", "which", "who"], ans=0, why="A place: <i>where</i>."),
        Q("pick", "My teacher, ___ is from Canada, loves history.", opts=["that", "who", "which"], ans=1, why="A person with commas: <i>who</i>."),
        Q("gap", "Students ___ parents are doctors often study medicine.", acc=["whose"], why="Possession: <i>whose</i>."),
        Q("spot", "The restaurant [[who]] opened last year is closing.", fix="The restaurant which opened last year is closing.", why="A thing: <i>which</i> or <i>that</i>, never <i>who</i>.")]),

"u13": dict(
    pairs=[("If I will see him, I will tell him.", "If I <b>see</b> him, I will tell him.", "No <i>will</i> after <i>if</i>."),
           ("If I was rich, I will buy a boat.", "If I <b>were</b> rich, I <b>would</b> buy a boat.", "Second conditional: past + <i>would</i>."),
           ("Unless you don't study, you will fail.", "<b>Unless you study</b>, you will fail. (Or: <b>If you don't study</b>…)", "<i>Unless</i> already means <i>if not</i>.")],
    bands=[("If government build more roads, more cars will come and traffic will be big.", "If governments keep building roads, they will only attract more cars, and congestion will worsen.", "A clear cause and effect, with precise vocabulary.")],
    qs=[Q("pick", "If I ___ more time, I would learn Japanese.", opts=["have", "had", "would have"], ans=1, why="Second conditional."),
        Q("pick", "If she ___ harder, she would have passed.", opts=["studied", "had studied", "would study"], ans=1, why="Third conditional."),
        Q("gap", "If water ___ (freeze), it expands.", acc=["freezes"], why="Zero conditional: always true."),
        Q("spot", "If the weather [[will be]] fine tomorrow, we will go hiking.", fix="If the weather is fine tomorrow, we will go hiking.", why="Present simple after <i>if</i>.")]),

"u14": dict(
    pairs=[("Everyone knows that money brings happiness.", "Many people <b>assume</b> that money brings happiness.", "<i>Everyone knows</i> is an absolute claim."),
           ("This policy is going to fail.", "This policy <b>is likely to</b> fail.", "A prediction needs a hedge."),
           ("Students never learn anything from lectures.", "Students <b>may</b> learn <b>less</b> from lectures than from discussion.", "<i>Never … anything</i> is easy to disprove.")],
    bands=[("Smoking should be banned because it is bad. Everybody agrees.", "A ban on smoking in public places could be justified, since there is strong evidence that passive smoking harms others.", "A hedged claim, backed by a reason.")],
    qs=[Q("pick", "Which claim is most careful?", opts=["Social media destroys friendships.", "Social media can weaken friendships in some cases.", "Social media always destroys friendships."], ans=1, why="It hedges the verb and the scope."),
        Q("pick", "Cheaper public transport ___ encourage more people to leave their cars at home.", opts=["would definitely", "will definitely", "might"], ans=2, why="A prediction: hedge it."),
        Q("gap", "Young drivers ___ (tend) to take more risks.", acc=["tend"], why="<i>Tend to</i> softens a generalisation."),
        Q("spot", "Online learning [[is the only way]] to educate children in the future.", fix="Online learning may become an important way to educate children in the future.", why="An absolute prediction. Soften it.")]),

"u15": dict(
    pairs=[("Despite of the rain, we went out.", "<b>Despite</b> the rain, we went out. (Or: <b>In spite of</b> the rain…)", "<i>Despite</i> takes no <i>of</i>."),
           ("He is rich. Although he is unhappy.", "He is rich, <b>but</b> he is unhappy. (Or: <b>Although</b> he is rich, he is unhappy.)", "An <i>although</i> clause cannot stand alone."),
           ("In spite the cost, many buy it.", "In spite <b>of</b> the cost, many people buy it.", "<i>In spite of</i>: the <i>of</i> is needed.")],
    bands=[("Cars are fast but they pollute. Trains are slow but clean.", "While cars are faster, trains are far cleaner, which is why many cities are expanding their rail networks.", "<i>While</i> balances both sides; <i>which is why</i> adds the consequence.")],
    qs=[Q("pick", "___ being tired, he finished the report.", opts=["Although", "Despite", "However"], ans=1, why="<i>-ing</i> follows: <i>despite</i>."),
        Q("pick", "___ the plan was expensive, it was approved.", opts=["Despite", "Although", "In spite of"], ans=1, why="A full clause follows: <i>although</i>."),
        Q("gap", "The north is wet, ___ the south is dry.", acc=["whereas", "while", "but"], why="A contrast between two clauses."),
        Q("spot", "Cars are fast. [[Although]] they pollute the air.", fix="Cars are fast, although they pollute the air.", why="An <i>although</i> clause must join a main clause.")]),

"u16": dict(
    pairs=[("Because of the prices are high, fewer people buy cars.", "<b>Because</b> prices are high, fewer people buy cars. (Or: <b>Because of</b> high prices…)", "<i>Because of</i> + noun; <i>because</i> + clause."),
           ("He studied hard in order that to pass.", "He studied hard <b>in order to</b> pass. (Or: <b>so that</b> he could pass.)", "Purpose: <i>in order to</i> + verb, or <i>so that</i> + clause."),
           ("Smoking results of lung cancer.", "Smoking <b>causes</b> (or <b>results in</b>) lung cancer.", "<i>Result in</i> + effect; <i>result from</i> + cause.")],
    bands=[("Many people lose jobs because of the machines are doing the work.", "The spread of automation has put many manual jobs at risk, leaving some workers unable to find comparable employment.", "Noun phrases and a participle clause replace the broken <i>because of</i> clause.")],
    qs=[Q("pick", "He took the job ___ he could pay his rent.", opts=["so that", "because of", "therefore"], ans=0, why="A clause of purpose."),
        Q("pick", "The match was cancelled ___ heavy snow.", opts=["due to", "because", "so"], ans=0, why="A noun phrase follows."),
        Q("gap", "Heavy traffic can lead ___ air pollution.", acc=["to"], why="<i>Lead to</i>."),
        Q("spot", "The train was late [[because of]] there was a signal failure.", fix="The train was late because there was a signal failure.", why="A clause follows, so <i>because</i>.")]),

"u17": dict(
    pairs=[("I like cities, they are exciting.", "I like cities<b>; they are</b> exciting. (Or: …cities <b>because</b> they are exciting.)", "A comma splice."),
           ("Which is why many people leave.", "Prices are high, <b>which is why</b> many people leave.", "A fragment: attach it to the sentence before."),
           ("There are many reasons for this firstly the cost is high and secondly it is slow.", "There are two reasons for this. <b>First</b>, the cost is high. <b>Second</b>, it is slow.", "A run-on: three ideas with no boundaries.")],
    bands=[("Students are tired, they sleep late, they do not pay attention.", "Students who sleep late are often too tired to pay attention in class.", "Three spliced clauses become one controlled sentence.")],
    qs=[Q("pick", "Which is correct?", opts=["The rent is high, many students share flats.", "The rent is high, so many students share flats.", "The rent is high so, many students share flats."], ans=1, why="<i>So</i> is a conjunction, so a comma before it is fine."),
        Q("pick", "Which is a fragment?", opts=["Because costs have risen.", "Costs have risen.", "Costs have risen because of inflation."], ans=0, why="A <i>because</i> clause has no main clause."),
        Q("gap", "Tourism brings money; ___, it can damage local culture.", acc=["however", "nevertheless", "nonetheless"], why="A semicolon is followed by a linker such as <i>however</i>."),
        Q("spot", "Many people walk to work[[,]] others cycle.", fix="Many people walk to work, while others cycle. (Or: …work; others cycle.)", why="A comma splice.")]),

"u18": dict(
    pairs=[("Because the temperature increased, the glaciers melted.", "<b>The rise in temperature</b> melted the glaciers.", "A clause becomes a noun phrase."),
           ("Cities have grown quickly, which is surprising.", "<b>The rapid growth of cities</b> is surprising.", "<i>Grown quickly</i> becomes <i>rapid growth</i>."),
           ("When people are poor, they cannot afford healthcare.", "<b>Poverty</b> limits access to healthcare.", "An adjective clause becomes a noun.")],
    bands=[("When governments spend more on schools, students do better.", "Increased government spending on schools is associated with better student outcomes.", "Two clauses become two noun phrases joined by one verb.")],
    qs=[Q("pick", "The government's ___ to raise taxes was unpopular.", opts=["decide", "decision", "decisive"], ans=1, why="A noun after <i>government's</i>."),
        Q("pick", "___ of public transport has reduced congestion.", opts=["Improve", "The improvement", "Improved"], ans=1, why="A noun phrase as the subject."),
        Q("gap", "The ___ (important) of sleep is often underestimated.", acc=["importance"], why="<i>Important → importance</i>."),
        Q("spot", "The [[grow]] of cities has put pressure on housing.", fix="The growth of cities has put pressure on housing.", why="A noun after <i>the</i>.")]),

"u19": dict(
    pairs=[("Seeing the accident, the police was called.", "Seeing the accident, <b>I called</b> the police.", "A dangling participle: the police did not see it."),
           ("The students taking the test they were nervous.", "The students <b>taking</b> the test were nervous.", "Do not repeat the subject."),
           ("Written in 1990, the author won an award.", "<b>Written</b> in 1990, the <b>book</b> won an award.", "The book was written, not the author.")],
    bands=[("The factory closed. It left hundreds of people without jobs.", "The factory closed, leaving hundreds of people without jobs.", "An <i>-ing</i> clause adds the result.")],
    qs=[Q("pick", "___ the instructions carefully, I began the test.", opts=["Read", "Having read", "Having reading"], ans=1, why="An earlier action: <i>having + past participle</i>."),
        Q("pick", "Which sentence is correct?", opts=["Driving to work, a deer ran in front of the car.", "Driving to work, I saw a deer run across the road.", "While drive to work, I saw a deer."], ans=1, why="Only here is the driver the subject."),
        Q("gap", "Students ___ (study) abroad often develop independence.", acc=["studying"], why="A reduced relative clause: <i>who study → studying</i>."),
        Q("spot", "Having lived in Dhaka for ten years, [[the city feels like home]] to me.", fix="Having lived in Dhaka for ten years, I feel at home in the city.", why="The participle's subject must be the main subject.")]),

"u20": dict(
    pairs=[("She suggested me to leave.", "She suggested <b>that I leave</b>.", "<i>Suggest</i> never takes object + <i>to</i>."),
           ("I enjoy to swim.", "I enjoy <b>swimming</b>.", "<i>Enjoy</i> + <i>-ing</i>."),
           ("He is used to get up early.", "He is used to <b>getting</b> up early.", "<i>Be used to</i>: <i>to</i> is a preposition.")],
    bands=[("The government must make people to stop smoke.", "The government should discourage people from smoking by raising tobacco taxes.", "A correct verb pattern, then <i>by + -ing</i> for the method.")],
    qs=[Q("pick", "She avoided ___ the question.", opts=["to answer", "answering", "answer"], ans=1, why="<i>Avoid</i> + <i>-ing</i>."),
        Q("pick", "The new law requires companies ___ their emissions.", opts=["reduce", "to reduce", "reducing"], ans=1, why="<i>Require</i> + object + <i>to</i>."),
        Q("gap", "He is looking forward to ___ (start) his course.", acc=["starting"], why="<i>To</i> is a preposition: <i>-ing</i>."),
        Q("spot", "My parents persuaded me [[studying]] medicine.", fix="My parents persuaded me to study medicine.", why="<i>Persuade</i> sb <i>to</i> do.")]),

"u21": dict(
    pairs=[("She likes swimming, to cycle and running.", "She likes <b>swimming, cycling and running</b>.", "Same form in a list."),
           ("The job is well paid, interesting and has a good location.", "The job is well paid, interesting and <b>well located</b>.", "Keep each item the same type."),
           ("It is both expensive and it takes time.", "It is both <b>expensive and slow</b>.", "<i>Both … and</i> joins two matching items.")],
    bands=[("The course is useful, and it has been helpful and I enjoy it.", "The course is useful, practical and enjoyable.", "Three parallel adjectives.")],
    qs=[Q("pick", "He enjoys playing football, reading and ___.", opts=["to cook", "cooking", "cooks"], ans=1, why="Match <i>playing, reading</i>."),
        Q("pick", "The plan is cheap, quick and ___.", opts=["it works well", "effective", "effectively"], ans=1, why="Adjectives in a list."),
        Q("gap", "Parents should listen, support and ___ (encourage) their children.", acc=["encourage"], why="Three base verbs."),
        Q("spot", "The aim is to reduce costs, improve quality and [[increasing]] sales.", fix="The aim is to reduce costs, improve quality and increase sales.", why="Base verbs after <i>to</i>.")]),

"u22": dict(
    pairs=[("Never I have seen such a problem.", "Never <b>have I</b> seen such a problem.", "A fronted negative: invert."),
           ("It is the lack of funding what causes delays.", "It is the lack of funding <b>that</b> causes delays.", "An it-cleft uses <i>that</i>."),
           ("Seldom people realise the danger.", "Seldom <b>do people</b> realise the danger.", "<i>Seldom</i> at the front: <i>do</i> + subject.")],
    bands=[("Education is important for the economy.", "It is education, more than any other factor, that drives long-term economic growth.", "An it-cleft puts the focus on education.")],
    qs=[Q("pick", "Seldom ___ such a clear victory.", opts=["we see", "do we see", "we do see"], ans=1, why="<i>Seldom</i> at the front: inversion."),
        Q("pick", "___ I need is more time.", opts=["That", "What", "It"], ans=1, why="A what-cleft."),
        Q("gap", "Only after the results appeared ___ the public react.", acc=["did"], why="<i>Only after</i> at the front: <i>did</i> + subject."),
        Q("spot", "Not until 1990 [[the law changed]].", fix="Not until 1990 did the law change.", why="<i>Not until</i> at the front: inversion.")]),

# ------------------------------------------------------------------ Speaking
"u23": dict(
    pairs=[("I am studying English since two years.", "I<b>'ve been studying</b> English <b>for</b> two years.", "Duration up to now: present perfect + <i>for</i>."),
           ("When I was a child I am going to the park every day.", "When I was a child I <b>used to go</b> to the park every day.", "A past habit: <i>used to</i>."),
           ("I wish I would have a car.", "I wish I <b>had</b> a car.", "<i>Wish</i> + past simple for a present wish.")],
    bands=[("In the future I will go abroad.", "I'm hoping to study abroad next year, though it depends on whether I get a scholarship.", "A natural plan with a condition.")],
    qs=[Q("pick", "Do you like your job? — Yes, I ___ there for three years.", opts=["work", "have worked", "worked"], ans=1, why="<i>For three years</i> up to now: present perfect."),
        Q("pick", "When we were kids, we ___ play in the street until dark.", opts=["would", "were used to", "are used to"], ans=0, why="A repeated past action: <i>would</i> or <i>used to</i>."),
        Q("gap", "I wish I ___ (can) speak French.", acc=["could"], why="<i>Wish</i> moves <i>can</i> to <i>could</i>."),
        Q("spot", "I [[live]] in this neighbourhood since I was born.", fix="I have lived in this neighbourhood since I was born.", why="<i>Since</i> needs the present perfect.")]),

"u24": dict(
    pairs=[("I very much like pizza.", "I <b>like pizza very much</b>.", "No adverb between the verb and its object."),
           ("I am not sure where is the station.", "I am not sure where <b>the station is</b>.", "Indirect question: statement order."),
           ("The room isn't enough big.", "The room isn't <b>big enough</b>.", "<i>Enough</i> follows an adjective.")],
    bands=[("I go sometimes to the cinema with friends.", "I sometimes go to the cinema with friends, though I rarely see more than one film a month.", "Adverbs placed correctly and a frequency contrast.")],
    qs=[Q("pick", "Choose the correct order.", opts=["I usually am tired on Mondays.", "I am usually tired on Mondays.", "I am tired usually on Mondays."], ans=1, why="After <i>be</i>."),
        Q("pick", "Could you tell me ___?", opts=["what time the shop opens", "what time does the shop open", "what time opens the shop"], ans=0, why="Indirect question: statement order."),
        Q("gap", "She hasn't got ___ to buy a car. (enough + money)", acc=["enough money"], why="<i>Enough</i> before a noun."),
        Q("spot", "She [[well speaks]] English.", fix="She speaks English well.", why="The adverb follows the object.")]),
}

# 16 more sentences for the grammar error hunt (items 25-40)
MORE_HUNT = [
    Q("spot", "The proportion of girls in science classes [[have]] risen.", fix="The proportion of girls in science classes has risen.", why="Head noun <i>proportion</i>: singular.", unit="u6"),
    Q("spot", "[[Despite of]] the high cost, many people travel abroad.", fix="Despite the high cost, many people travel abroad.", why="<i>Despite</i> takes no <i>of</i>.", unit="u15"),
    Q("spot", "Technology has made [[the life]] much easier.", fix="Technology has made life much easier.", why="General idea: no article.", unit="u9"),
    Q("spot", "The company [[have launched]] a new app last month.", fix="The company launched a new app last month.", why="<i>Last month</i> is finished: past simple.", unit="u2"),
    Q("spot", "The wheat [[is grew]] in fields across the region.", fix="The wheat grows in fields across the region.", why="Natural process: active.", unit="u3"),
    Q("spot", "Sales fell [[at]] 12% between May and June.", fix="Sales fell by 12% between May and June.", why="Size of change: <i>by</i>.", unit="u4"),
    Q("spot", "[[Less]] cars were sold in 2020 than in 2019.", fix="Fewer cars were sold in 2020 than in 2019.", why="Countable: <i>fewer</i>.", unit="u5"),
    Q("spot", "A [[ten-years]] study found no link between the two.", fix="A ten-year study found no link between the two.", why="Singular inside the phrase.", unit="u7"),
    Q("spot", "If I [[would have]] more time, I would join a club.", fix="If I had more time, I would join a club.", why="Second conditional: past simple after <i>if</i>.", unit="u13"),
    Q("spot", "She suggested [[to take]] a taxi.", fix="She suggested taking a taxi.", why="<i>Suggest</i> + <i>-ing</i>.", unit="u20"),
    Q("spot", "The research [[are]] still at an early stage.", fix="The research is still at an early stage.", why="<i>Research</i> is uncountable.", unit="u10"),
    Q("spot", "Pollution is a major problem, [[which are]] expensive to solve.", fix="Pollution is a major problem, which is expensive to solve.", why="<i>Which</i> refers to the singular <i>problem</i>.", unit="u12"),
    Q("spot", "She works two jobs [[for to]] pay her rent.", fix="She works two jobs to pay her rent.", why="Purpose: <i>to</i> + verb.", unit="u16"),
    Q("spot", "I'm [[used to]] play tennis every Sunday when I was a child.", fix="I used to play tennis every Sunday when I was a child.", why="A past habit: <i>used to</i> + base verb.", unit="u23"),
    Q("spot", "Only if governments act now [[we can]] avoid disaster.", fix="Only if governments act now can we avoid disaster.", why="<i>Only if</i> at the start: inversion.", unit="u22"),
    Q("spot", "The job is not only badly paid but also [[it is dangerous]].", fix="The job is not only badly paid but also dangerous.", why="Parallel structure.", unit="u21"),
]
