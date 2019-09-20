from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    '''By the end of her inglorious three-year stint in Downing Street, even her most loyal supporters admitted that the robotic May would never be regarded as one of the greatest British leaders.
By comparison, Boris Johnson's off-the-cuff, sunny disposition made him a darling of Conservative Party members who chose him for the top job when May finally resigned, defeated by her inability to get a Brexit deal through Parliament.
On his first day as Prime Minister, Johnson promised a bold new Brexit deal, bashing the "doubters, doomsters, gloomsters" and the political class who he said had forgotten about the British people they serve. It was as if an upbeat attitude alone could be enough to overcome any adversity on the United Kingdom's path to exiting the European Union.
A legacy of failure: Theresa May was a disaster as Prime Minister
For a moment, it seemed he would breathe new life and, in his words, "positive energy," into the Brexit process. Some thought, just maybe, he could manage to do what May did not.
How quickly it all went wrong.
Johnson has lost every one of his first votes in parliament, an unprecedented record in the modern era. Undeterred, the Prime Minister purged 21 members of his parliamentary party who voted against him, blowing apart his majority.
Then, his efforts to secure a snap general election -- with the goal of replacing the sacked lawmakers with a new slate of candidates more aligned with his hard-Brexit views -- were scuppered when opposition Labour leader Jeremy Corbyn refused to play along.
Now, he is effectively trapped in Downing Street, with Corbyn holding the keys. The government plans to propose new elections again on Monday, but the opposition leader says his party will only support the move when its efforts to prevent a no-deal Brexit are locked down.
"Certainly his biggest tactical mistake so far was not to realize that it was Corbyn, as leader of the opposition, who effectively had veto power over when a general election could be held," said Professor Tony Travers, director of the Institute of Public Affairs at the London School of Economics.''',

    '''Newly released satellite images give a sense of just how devastating Hurricane Dorian was to parts of the Bahamas.
Dorian was a Category 5 storm when it hit the Bahamas on Saturday and then stalled over the northern Bahamas for days before continuing on its path.
Bahamas official warns people to prepare for the 'unimaginable' as hurricane death toll rises to 30
The storm is blamed for at least 30 deaths and Bahamas officials say that hundreds, or even thousands are missing.
Satellite images from Maxar Technologies show the damage to several parts of Marsh Harbour on Great Abaco Island, which suffered a direct hit from the storm.
The images from before the hurricane were taken on October 25, 2018, and the photos after Dorian hit were taken on September 5.''',

    '''India's historic attempt to soft land a rover on the moon may have ended in failure moments before landing and scientists scrambled to analyze the final communication from Chandrayaan-2.
"Vikram lander descent was as planned and normal performance was observed till the altitude of 2.1 km. Subsequently the communication from the lander to ground station was lost. The data is being analyzed," said K. Sivan, chairman of the Indian Space Research Organisation, the country's equivalent of NASA.
The control room in the city of Bengaluru filled with scientists underwent a visible change as updates from the lander faded. The crowd had celebrated every small step during the controlled descent and at 1:55 a.m. local time on Saturday (4:25 p.m. ET Friday), the moment the landing was expected to take place, silence descended.
"In life, there are ups and downs. The country is proud of you. And all your hard work has taught us something ... Hope for the best ... You have served the country well and served science and humanity well," said Prime Minister Narendra Modi after the announcement.
Later, Modi tweeted: "We remain hopeful and will continue working hard on our space programme." He was scheduled to address the nation later Saturday.
"As important as the final result is ... I can proudly say that the effort was worth it and so was the journey. Our team worked hard, traveled far and those teachings will always remain with us," Modi said in a speech posted on Twitter hours later.
Modi was in the mission control room when the lander was supposed to touch down.''',

    '''The world's appetite for travel is voracious.
Since 2009, the number of international overnight visitors has grown by 76% globally, according to third-party research and proprietary analysis by financial services company Mastercard.
For the fourth year in a row, Bangkok is the No. 1 most popular city on Mastercard's Global Destination Cities Index.
In 2018, the Thai capital welcomed 22.78 million international overnight visitors, with 3.34% growth forecast for 2019.
Many of Bangkok's visitors originate from these top five destinations, listed in order: Mainland China, Japan, South Korea, India and the United Kingdom. Popular attractions include the Grand Palace, Wat Arun and for a day trip outside the city, the Damnoen Saduak Floating Market.
Paris and London rank No. 2 and No. 3 for visitors, both welcoming more than 19 million international visitors for overnight stays in 2018.
Mastercard's index ranks 200 cities based on proprietary analysis of visitor volume and spending data that is publicly available.
All but one of the top 10 cities for visitor numbers in 2018 saw an uptick in international overnight visitors, with increases predicted across the board for 2019.
London was the only city on the current top 10 that saw a visitor decline year-over-year -- a nearly 4% drop.
Asia-Pacific cities have seen the largest regional increase in international travelers since 2009, with a more than 9% increase spurred by rising numbers of mainland Chinese travelers.
The index also ranks cities by international overnight visitor spending. By that measure, Dubai in the United Arab Emirates is the No. 1 city. International overnight visitors spent $30.82 billion there in 2018, spending a whopping $553 per day, on average.
By comparison, visitors to Bangkok -- the most popular city by visitor numbers -- spent an average of $184 per day. Bangkok ranked third for total international overnight visitor spending ($20.03 billion), with Mecca, Saudi Arabia, at No. 2 ($20.09 billion).''',

    'This is One-Piece',
]

vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w[-\w]+\b", stop_words='english')
tfidf = vectorizer.fit_transform(corpus)
words = vectorizer.get_feature_names()

for index, sentence in enumerate(corpus):
    #print(sentence)
    row = tfidf[index]
    for i, prob in zip(row.indices, row.data):
        if (prob > 0.18):
            print(words[i], ':', prob)
    print("")
