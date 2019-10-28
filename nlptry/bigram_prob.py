import nltk

word_data = '''
His Republican shock troops storm secure hearing rooms, he blasts Republican doubters as "human scum" and his aides slam diplomats who testify about his alleged abuses of power as "radical bureaucrats" at war with the Constitution.
Yet neither Trump nor his White House has come up with a strong counterargument to the potential smoking-gun testimony of the US top diplomat in Ukraine, which is still reverberating through Washington.
A day of inflammatory behavior by the President and his allies on Wednesday actually hinted at the depth of Trump's troubles on Capitol Hill and in courtrooms beyond instead of its apparent purpose in distracting from it.
In a remarkable moment Wednesday morning, around two dozen Republican lawmakers stormed a secure hearing room that was due to hear a deposition by a senior Pentagon official on the Ukraine scandal.
Top US diplomat in Ukraine Bill Taylor's deposition on Tuesday added to a pile of damning testimony alleging that Trump used presidential power to pressure a foreign government to try to sway the 2020 election, which Republicans and the White House are struggling to refute with facts and arguments of their own.
And it led to a rare sign of concern in the Republican ranks on which Trump will rely to save him in any Senate impeachment trial -- from senior GOP Sen. John Thune.
"The picture coming out of it, based on the reporting that we've seen, I would say is not a good one," said the South Dakotan, though like many of his colleagues he faulted the so-far closed Democratic investigative process.
The President did what he often does when an unappealing political reality threatens: He simply invented a more advantageous one, launching misleading attacks on the conduct of the inquiry and picking new fights.
"The Never Trumper Republicans, though on respirators with not many left, are in certain ways worse and more dangerous for our Country than the Do Nothing Democrats. Watch out for them, they are human scum!" he tweeted.
Republican lawmaker says its beneath the office of the presidency for Trump to call critics human scum
It was not clear who the President was singling out, though his tweet could be a catchall for any Republican -- such as Sen. Mitt Romney of Utah -- who has called out his behavior.
On Tuesday, Trump's press secretary, Stephanie Grisham, blasted officials who testify against the President as radical bureaucrats "waging war on the Constitution."
On Wednesday evening, the top Republican members of the three committees involved in the impeachment inquiry asked Intelligence Chairman Adam Schiff, a California Democrat, to bring in the whistleblower who's at the heart of the investigation for public testimony. Democrats have said they won't do that, given concerns about protecting the person's identity.
Trump also scheduled a televised statement in the White House on Wednesday to congratulate himself on the outcome of the Syria crisis, which a senior member of his administration described as a "tragedy."
"People are saying, wow, what a great outcome," Trump said of a drama that caused a humanitarian crisis, boosted Turkey, Iran and Russia at US expense and deserted America's Kurdish allies.
A 'nuts' room invasion
The hearing room stunt Wednesday morning, which saw the braying invaders refuse to leave for around five hours, came days after the President told Republicans they needed to be tougher in his defense.
"It was closest thing I've seen around here to mass civil unrest as a member of Congress," said one source in the room.
Another source familiar with the matter said Trump had advance knowledge of the plans to attempt entry to the secure area. Many of the angry Republican lawmakers involved had been at the White House on Tuesday.
The testimony of the official, Deputy Assistant Defense Secretary Laura Cooper, did eventually go ahead, but hours late.
Republicans say their protest was to call attention to Democrats who are holding impeachment depositions behind closed doors.
Democrats say they are acting within their constitutional powers and eventually plan open hearings but want to ensure witness depositions cannot be contaminated at this early stage.
The episode hinted at how badly a string of testimony by senior and former foreign policy officials is hurting Trump as Democrats investigate whether he abused his power by coercing Ukraine to dig up dirt on 2016 Democrats and his potential 2020 political foe, former Vice President Joe Biden.
Days of revelations appear to be building a solid case for impeachment. That's especially the case since there has been a paucity of counter-leaks with mitigating evidence from GOPers who are inside the hearings.
One Republican, Rep. Mo Brooks of Alabama, accused Democrats of plotting to oust the President in secret.
"Show your face where we can all see the travesty that you are trying to foist on America and the degradation of our republic that you're engaged in," he said.
But another one of Trump's sworn defenders, Republican Sen. Lindsey Graham of South Carolina, failed to appreciate the spectacle in the sensitive compartmented information facility -- shorthanded on Capitol Hill to "SCIF" -- into which some lawmakers had plunged with insecure cellphones in contravention of the rules.
"This is nuts. They're making a run on the SCIF. That's not the way to do it," Graham said, though he later rowed back in a tweet, arguing the protest was "peaceful" and that he understood the GOP frustration.
There's a note of irony in the GOP's demands for transparency. The Trump administration has done everything it can to subvert Democratic oversight of the President. Even as the protest went on in the House, one of Trump's lawyers was in court close by arguing against the release of the President's tax returns -- to restore a tradition followed by previous commanders in chief but flouted by the current one.
Wednesday's mayhem was all the more jarring since lawmakers are expected to restore decorum on Thursday, the start of two days of mourning for the late Democratic Rep. Elijah Cummings of Maryland.
US envoy offered the 'why' in quid pro quo
The uproar doesn't change much in the substance of the growing impeachment case.
While the closed-door nature of the hearings provides only a selective impression of evidence, Trump's plight seems to darken by the day. His lawyers and allies will likely get the chance to cross-examine witnesses in a later stage of the House process, and they definitely would in a Senate impeachment trial.
But there are growing questions about the defense they can make given the torrent of damaging testimony so far.
Taylor testified on Tuesday about a rogue foreign policy operation in the White House involving the President's personal lawyer Rudy Giuliani. He also says he was told that Trump insisted there was no quid pro quo with Ukraine but wanted its President to publicly state that he would investigate a conspiracy theory about 2016 election interference, along with Biden and the former vice president's son.
"He definitely alleges a quid pro quo and it is an incredibly detailed statement. ... It is very convincing," Ross Garber, an experienced impeachment attorney, told CNN's Jake Tapper.
Democrats insist that there need not be a quid pro quo for Trump to have committed an impeachable offense -- simply abusing his power to set foreign policy for political gain would be enough.
"The issue is -- the why. Why was this happening? That's why I think Taylor's testimony was so devastating: He offers the why," Garber said.
"Right now, there hasn't been a White House answer to counter the Bill Taylor narrative for why -- which was essentially campaign assistance."
Trump's Republican defenders refashioned a previous defense of the President, saying Taylor's testimony was not based on firsthand knowledge of Trump's actions and intentions.
House GOP leader Kevin McCarthy of California referred to a transcript of a phone call between Trump and Ukraine's President Volodymyr Zelensky on July 25.
"Nowhere in that phone call is there a quid pro quo," McCarthy told CNN's Manu Raju. Many observers have looked at the call and concluded exactly the opposite, however.
Trump's growing exposure was not exclusive to Capitol Hill.
A federal judge in Washington ordered the State Department to release Ukraine-related records, including communications between Secretary of State Mike Pompeo and Giuliani.
The documents could shed more light on the off-the-books foreign policy shop on Ukraine that Democrats charge the President used to hide his abuses of power.
In a federal appeals court in Manhattan, meanwhile, one of Trump's lawyers argued that the President is effectively above the law as he sought to block the release of Trump's tax returns to New York state prosecutors.
Attorney William Consovoy argued that local authorities in New York City could not prosecute the sitting President even if he shot someone in the street.
'''
nltk_tokens = nltk.word_tokenize(word_data)

bigram = list(nltk.bigrams(nltk_tokens))

pregram_count_map = {}
bigram_count_map = {}

for first,second in bigram:
    if first in pregram_count_map:
        pregram_count_map[first] = pregram_count_map[first] + 1
    else :
        pregram_count_map[first] = 1

    if (first,second) in bigram_count_map:
        bigram_count_map[(first,second)] = bigram_count_map[(first,second)] + 1
    else :
        bigram_count_map[(first,second)] = 1


def get_bigram_prob(first_word, second_word, pregram_count_map, bigram_count_map):
    if first_word in pregram_count_map:
        if (first_word, second_word) in bigram_count_map:
            return bigram_count_map[(first_word, second_word)] / pregram_count_map[first_word]
        else:
            return 0
    else:
        return 0


print("P(testimony|Taylor)=", get_bigram_prob("Taylor", "testimony", pregram_count_map, bigram_count_map))
print("P(testified|Taylor)=", get_bigram_prob("Taylor", "testified", pregram_count_map, bigram_count_map))
print("P(President|the)=", get_bigram_prob("the", "President", pregram_count_map, bigram_count_map))
print("P(White|the)=", get_bigram_prob("the", "White", pregram_count_map, bigram_count_map))

