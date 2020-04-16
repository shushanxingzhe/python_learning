import re
from collections import Counter

text = open('../data/west_journey.txt', encoding='utf-8').read()

sentences = re.split(r'，|。|“|”|‘|’|！|？|；|：|、|…|《|》|【|】|{|}|（|）|-|\r\n|\n|　| |\t|\[|\]', text)
sentences = list(filter(len, sentences))

print(sentences[:10])

unigram = []
bigram = []
trigram = []
fourgram = []
fivegram = []

for sent in sentences:
    unigram += [sent[i] for i in range(len(sent))]
    bigram += [sent[i:i + 2] for i in range(len(sent) - 1)]
    trigram += [sent[i:i + 3] for i in range(len(sent) - 2)]
    fourgram += [sent[i:i + 4] for i in range(len(sent) - 3)]
    fivegram += [sent[i:i + 5] for i in range(len(sent) - 4)]

unigram_size = len(unigram)
unigram_counter = Counter(unigram)
print(len(unigram_counter))
print(unigram_counter.most_common(10))
bigram_size = len(bigram)
bigram_counter = Counter(bigram)
print(len(bigram_counter))
print(bigram_counter.most_common(10))
trigram_size = len(trigram)
trigram_counter = Counter(trigram)
print(len(trigram_counter))
print(trigram_counter.most_common(10))
fourgram_size = len(fourgram)
fourgram_counter = Counter(fourgram)
print(len(fourgram_counter))
print(fourgram_counter.most_common(10))
fivegram_size = len(fivegram)
fivegram_counter = Counter(fivegram)
print(len(fivegram_counter))
print(fivegram_counter.most_common(10))

words2 = {}
words3 = {}
words4 = {}
words5 = {}
no_words2 = {}
no_words3 = {}
no_words4 = {}
no_words5 = {}
union = []

low_threshhold = 0.1
mid_threshhold = 0.7
high_threshhold = 0.4

unigram_dict = dict(unigram_counter)
for k, v in bigram_counter.most_common():
    if v < 20:
        break
    prob = (v / (unigram_dict[k[:-1]] + unigram_dict[k[1:]]))
    prob1 = (v / unigram_dict[k[:-1]])
    if prob > low_threshhold or prob1 > mid_threshhold:
        words2[k] = prob
    else:
        no_words2[k] = prob

bigram_dict = dict(bigram_counter)
for k, v in trigram_counter.most_common():
    if v < 20:
        break
    prob = (v / (bigram_dict[k[:-1]] + bigram_dict[k[1:]]))
    prob1 = (v / bigram_dict[k[:-1]])
    if prob > low_threshhold or prob1 > mid_threshhold:
        words3[k] = prob
    else:
        no_words3[k] = prob

trigram_dict = dict(trigram_counter)
for k, v in fourgram_counter.most_common():
    if v < 20:
        break
    prob = (v / (trigram_dict[k[:-1]] + trigram_dict[k[1:]]))
    prob1 = (v / trigram_dict[k[:-1]])
    if prob > low_threshhold or prob1 > mid_threshhold:
        words4[k] = prob
    else:
        no_words4[k] = prob

fourgram_dict = dict(fourgram_counter)
for k, v in fivegram_counter.most_common():
    if v < 20:
        break
    prob = (v / (fourgram_dict[k[:-1]] + fourgram_dict[k[1:]]))
    prob1 = (v / fourgram_dict[k[:-1]])
    if prob > low_threshhold or prob1 > mid_threshhold:
        words5[k] = prob
    else:
        no_words5[k] = prob

for w in list(words5.keys()):
    if words5[w] > high_threshhold and w[:-1] in words4 and w[1:] in words4:
        union.append(w)
        no_words4[w[:-1]] = words4[w[:-1]]
        no_words4[w[1:]] = words4[w[1:]]
        del words4[w[:-1]]
        del words4[w[1:]]

for w in list(words4.keys()):
    if words4[w] > high_threshhold and w[:-1] in words3 and w[1:] in words3:
        union.append(w)
        no_words3[w[:-1]] = words3[w[:-1]]
        no_words3[w[1:]] = words3[w[1:]]
        del words3[w[:-1]]
        del words3[w[1:]]

for w in list(words3.keys()):
    if words3[w] > high_threshhold and w[:-1] in words2 and w[1:] in words2:
        union.append(w)
        no_words2[w[:-1]] = words2[w[:-1]]
        no_words2[w[1:]] = words2[w[1:]]
        del words2[w[:-1]]
        del words2[w[1:]]

print(union)
print(list(words2.keys())[:10])
print(list(no_words2.keys())[:10])
print(list(words3.keys())[:10])
print(list(no_words3.keys())[:10])
print(list(words4.keys())[:10])
print(list(no_words4.keys())[:10])
print(list(words5.keys())[:10])
print(list(no_words5.keys())[:10])

all_words = list(words5.keys()) + list(words4.keys()) + list(words3.keys()) + list(words2.keys())
print(all_words)
