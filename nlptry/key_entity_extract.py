import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def extract_nourphrase(text):
    grammar = r'''
        NPART:
            {<NN.*>*<NN.*>}
        NP:
            {<DT><NPART|CC|JJ|CD|IN>*<NPART>}
            {<NPART|JJ|CD><NPART|CC|JJ|CD|IN>*<NPART>}
            {<NPART>}
            '''

    cp = nltk.RegexpParser(grammar)
    chunks = cp.parse(nltk.pos_tag(nltk.word_tokenize(text)))
    candidate = []
    for vp in list(chunks.subtrees(filter=lambda x: x.label() == 'NP')):
        leaves = vp.leaves()
        if 1 < len(leaves) < 10:
            if leaves[0][1] == 'DT' and leaves[0][0].lower() != 'the':
                continue
            candidate.append(" ".join([i[0] for i in leaves]))

    return candidate


txt = '''Trump Organization chief financial officer Allen Weisselberg surrendered to the Manhattan district attorney's office Thursday morning ahead of expected criminal charges against him and the company in connection with alleged tax crimes, his attorney told CNN.
Weisselberg is set to be arraigned later Thursday at a lower Manhattan courthouse. Weisselberg's attorneys, Mary Mulligan and Bryan Skarlatos, said he plans to plead not guilty and "will fight these charges in court."
A Manhattan grand jury filed the indictments Wednesday, and they are set to be unsealed Thursday around 2 p.m. ET, according to two sources familiar with the matter. The precise type or number of charges they are expected to face was not immediately clear.
Allen Weisselberg, center, CFO of the Trump Organization, surrendered on Thursday to the Manhattan district attorney's office, in New York, on July 1, 2021. (Jefferson Siegel for The New York Times)
Though former President Donald Trump faced multiple federal and state prosecutorial inquiries during his administration, the district attorney's indictment would be the first to charge his namesake company, the Trump Organization, for conduct that occurred when he led it.
Trump himself is not expected to be charged, his attorney has said.
The indictment of the Trump Organization is the product of more than two years of investigation by the district attorney, Cyrus Vance Jr., a probe that began with questions about accounting practices tied to hush-money payments made by former Trump lawyer Michael Cohen and eventually led to a Supreme Court fight over a subpoena for Trump's tax documents.
It is rare, according to lawyers who specialize in tax evasion cases, for prosecutors to bring charges solely related to fringe benefits provided by a company, and in recent weeks, lawyers for the Trump Organization met with prosecutors in Vance's office, hoping to persuade them not to bring the case.
Indictments of firm and top executive test Trump's charmed life
The Trump Organization released a statement Thursday saying that Weisselberg is being used by Manhattan prosecutors "as a pawn."
"The District Attorney is bringing a criminal prosecution involving employee benefits that neither the IRS nor any other District Attorney would ever think of bringing. This is not justice; this is politics," said the statement, attributed to a spokesperson from the Trump Organization.
Over the course of the probe, prosecutors have examined a wide array of possible violations, including whether the real-estate company misled lenders and insurers or committed tax fraud, even adding a special prosecutor, Mark Pomerantz, to aid in the expansive inquiry. But in recent months, the focus has narrowed to taxes on benefits.
In particular, it came to center on Trump's longtime lieutenant Weisselberg, a top company executive who has worked for him since 1973.
Beginning late last year, prosecutors gathered evidence on Weisselberg with the cooperation of his former daughter-in-law, Jennifer Weisselberg. In the months since she began speaking to authorities, she has turned over boxes of financial records and has met with investigators multiple times, her lawyer told CNN.
Former daughter-in-law of Trump exec on potential of him flipping
Documents from Jennifer Weisselberg's divorce from Allen Weisselberg's son Barry show thousands of dollars in payments for cars, rent, tuition, medical bills and more going from Allen Weisselberg to his son's family.
An indictment of Weisselberg would intensify the pressure for him to cooperate with prosecutors in their wide-ranging investigation of Trump, the company and its executives, an outcome prosecutors have been seeking for months but which his lawyers have told authorities he has rejected.'''

txt1 = '''Israeli forces have demolished a building in the East Jerusalem neighborhood of Al Bustan, the first in what locals fear could be a string of demolitions in the area.
The operation comes during a period of heightened tension in Jerusalem, with Palestinian residents in another neighborhood, Sheikh Jarrah, facing the threat of forced removal from their homes, and a series of violent clashes in May between Israeli police and Palestinians around the Aqsa mosque in the Old City.
Bulldozers, along with Israeli police forces, arrived in Al Bustan around 8:00 in the morning, locals said, and took about two hours to bring down the building, which housed a butcher's shop.
The owner of the shop, Nidal Rajibi, had received the mandated warning letter, locals said, which had instructed him to pull the building down by last Sunday.
Israeli authorities say the shop, along with several other buildings in the area on which residents say notices have also been served, were constructed without the necessary permissions. Locals say they have tried to get building permits but are always refused.
Palestinian activist dies during 'brutal beating and arrest' by Palestinian Authority security forces
Rajibi was taken away by police, along with his brother, during the operation, while six people received injuries caused by rubber bullets, as security forces clashed with locals, according to the Palestinian Red Crescent.
"The Israelis told us to demolish our homes by ourselves, but the residents said we will not destroy our own homes with our own hands. They demolished one store to put out a feeler for what is to come, they wanted to test the reaction of the Palestinian street," Kutayba Odeh told CNN outside the demolished shop.
About ninety structures in Al Bustan could be facing eventual demolition, according to Jerusalem-based attorney Daniel Seidemann, who has chronicled Israel's settlement policies for decades, though more than 70 of the demolition orders have been stayed by the court, he says, making clearance of the neighborhood in one operation highly unlikely.
Al Bustan lies next to the City of David archaeological site, immediately to the south of the Old City. Lying in East Jerusalem, it is regarded as illegally occupied territory by most of the international community, though Israel regards all of the city as its sovereign territory.
While the immediate fate of the neighborhood might be unclear, Seidemann says Israel's long-term intentions are plain. "It is part of a project to ring the Old City with settlements and settlement-related open spaces with biblically inspired themes," he said.
A truce halted the bloodshed, but the frustration of young Palestinians is stronger than ever
Another East Jerusalem neighborhood, Sheikh Jarrah, has been the scene of repeated violence in the last few months, with Israeli police accused of heavy-handed tactics in the face of protests over the possible expulsion of several Palestinian families from their homes.
The families are trying to prevent the loss of their homes to a Jewish organization which says it holds the title deeds to the properties.
The Palestinian families were settled in the neighborhood decades ago, when East Jerusalem was under Jordanian control, after losing their homes in what became the state of Israel, during fighting in the late 1940s.'''

corpus = [txt, txt1]
vectorizer = TfidfVectorizer(stop_words=ENGLISH_STOP_WORDS)

tfidf = vectorizer.fit_transform(corpus)

id2words = vectorizer.get_feature_names()
docs = []
for item in tfidf:
    doc = []
    for idx, w in zip(item.indices, item.data):
        if w > 0.1:
            doc.append((id2words[idx], w))
    docs.append(doc)

for i in range(len(docs)):
    print(docs[i])
    entities = extract_nourphrase(corpus[i])

    keep = []
    for entity in entities:
        for w in docs[i]:
            if entity.lower().find(w[0]) > -1:
                keep.append(entity)
                break
    print(keep)
