import pandas as pd
from itertools import combinations
import time
import math


def word2ngrams(word, n=2):
    word = '$' + word + '$'
    return list(set([word[i:i+n] for i in range(len(word)-1)]))


def edit_distance(str1, str2, m, n):
    if m <= 0 or n<=0:
        if str1[0] == str2[0]:  # first letter is always right
            return max(m,n)-0.5
        else:
            return max(m,n)

    if str1[m - 1] == str2[n - 1]:
        return edit_distance(str1, str2, m - 1, n - 1)

    options = [
        edit_distance(str1, str2, m, n - 1),  # Insert
        edit_distance(str1, str2, m - 1, n),  # Remove
        edit_distance(str1, str2, m - 1, n - 1)  # Replace
    ]
    if str1[m - 1] == str2[n - 2] and str1[m - 2] == str2[n - 1]:
        options.append(edit_distance(str1, str2, m - 2, n - 2))  # Swap

    return 1 + min(options)


def get_inverted_index():
    df = pd.read_table('../data/english_words.txt', sep=' ', header=None)
    df = df[df[1] > 50]
    english_words = df[0].values
    words_frequency = df[1].values
    all_words = {}

    inverted_index = {}
    for words,frequency in zip(english_words,words_frequency):
        words = str(words).lower()
        all_words[words] = frequency
        ngrams = word2ngrams(words)
        for ngram in ngrams:
            if ngram in inverted_index:
                inverted_index[ngram].append(words)
            else:
                inverted_index[ngram] = [words]

    # export = pd.DataFrame({'ngram': list(inverted_index.keys()), 'words': list(inverted_index.values())})
    # export.to_csv('../data/letter_2gram_index.csv', index=False)
    return inverted_index,all_words


def spelling_correction(query, inverted_index, all_words):
    query = str(query).lower()
    if query in all_words:
        return {query:1}
    query_ngrams = word2ngrams(query)
    ngrams_match = []
    query_ngrams_count = 0
    query_length = len(query)

    for ngram in query_ngrams:
        if ngram in inverted_index:
            match_set = []
            for item in inverted_index[ngram]:
                # 跳过可能性低的匹配项
                if len(item) > query_length + 3 or len(item) < query_length - 3:
                    continue
                match_set.append(item)
            ngrams_match.append(match_set)
            query_ngrams_count = query_ngrams_count + 1

    if query_length > 3:
        combines = [c for c in combinations(ngrams_match, 2)]
    else:
        combines = [c for c in combinations(ngrams_match, 1)]

    alternatives = set()
    for combine in combines:
        mid = None
        for item in combine:
            if mid is None:
                mid = set(item)
            elif len(mid) == 0:
                break
            else:
                mid = mid.intersection(set(item))

        alternatives = alternatives.union(mid)

    alternatives = list(alternatives)
    alternatives = [item.lower() for item in alternatives]

    filter_result = []
    weight_map = {}
    for item in alternatives:
        intersect = len(set(query_ngrams).intersection(set(word2ngrams(item))))
        jaccard = intersect / (len(item) + query_ngrams_count - intersect)
        if jaccard > 0.3 or jaccard * math.log(all_words[item]) > 2.5:
            weight_map[item] = jaccard * math.pow(math.log(all_words[item]),2)
            filter_result.append(item)

    dist2words = {}
    for item in filter_result:
        distance = edit_distance(query,item,len(query),len(item))
        if distance in dist2words:
            dist2words[distance].append(item)
        else:
            dist2words[distance] = [item]

    result = dict()
    for i in range(2):
        min_key = min(dist2words.keys())
        for item in dist2words[min_key]:
            result[item] = weight_map[item] / (min_key+1)
        dist2words.pop(min_key)

    sorted_result = {}
    counter = 1
    for k in sorted(result, key=lambda k: result[k], reverse=True):
        sorted_result[k] = result[k]
        counter = counter + 1
        if counter > 10:
            break

    return sorted_result


def similar_words(query, inverted_index, all_words):
    query = str(query).lower()
    if query not in all_words:
        return {}
    query_ngrams = word2ngrams(query)
    ngrams_match = []
    query_ngrams_count = 0
    query_length = len(query)

    for ngram in query_ngrams:
        if ngram in inverted_index:
            match_set = []
            for item in inverted_index[ngram]:
                # 跳过可能性低的匹配项
                if len(item) > query_length + 3 or len(item) < query_length - 3:
                    continue
                match_set.append(item)
            ngrams_match.append(match_set)
            query_ngrams_count = query_ngrams_count + 1

    if query_length > 3:
        combines = [c for c in combinations(ngrams_match, 2)]
    else:
        combines = [c for c in combinations(ngrams_match, 1)]

    alternatives = set()
    for combine in combines:
        mid = None
        for item in combine:
            if mid is None:
                mid = set(item)
            elif len(mid) == 0:
                break
            else:
                mid = mid.intersection(set(item))

        alternatives = alternatives.union(mid)

    alternatives = list(alternatives)
    alternatives = [item.lower() for item in alternatives]

    filter_result = []
    weight_map = {}
    for item in alternatives:
        intersect = len(set(query_ngrams).intersection(set(word2ngrams(item))))
        jaccard = intersect / (len(item) + query_ngrams_count - intersect)
        if jaccard > 0.3 or jaccard * math.log(all_words[item]) > 2.5:
            weight_map[item] = jaccard * math.pow(math.log(all_words[item]),2)
            filter_result.append(item)

    dist2words = {}
    for item in filter_result:
        distance = edit_distance(query,item,len(query),len(item))
        if distance in dist2words:
            dist2words[distance].append(item)
        else:
            dist2words[distance] = [item]

    result = dict()

    for i in range(3):
        min_key = min(dist2words.keys())
        for item in dist2words[min_key]:
            result[item] = weight_map[item] / (min_key+1)
        dist2words.pop(min_key)

    if len(result) > 10:
        topk = {}
        counter = 1
        for k in sorted(result, key=lambda k: result[k], reverse=True):
            topk[k] = result[k]
            counter = counter + 1
            if counter > 10:
                break
        result = topk

    return result

def norvig_corrent(word, all_words):
    if word in all_words:
        return {word:1}

    edits_1 = known(edits1(word), all_words)
    edits_2 = known(edits2(word), all_words)

    result = {}
    for w in edits_1:
        result[w] = math.log(all_words[w]) / 2
    for w in edits_2:
        result[w] = math.log(all_words[w]) / 3
    return result

def known(words,all_words):
    "The subset of `words` that appear in the dictionary of all_words."
    return set(w for w in words if w in all_words)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


inverted_index, all_words = get_inverted_index()
start = time.time()
# query is pamphorse, while real word is: pumphouse

query = 'pamphorse'
print("query:   " + query)
print('spelling_correction:')
result = spelling_correction(query, inverted_index, all_words)

print(result)
print('time consuming:', time.time()-start)
start = time.time()
result = similar_words(query, inverted_index, all_words)
print('similar_words:')
print(result)
print('time consuming:', time.time()-start)


start = time.time()
result = norvig_corrent(query, all_words)
print('norvig_corrent:')
print(result)
print('time consuming:', time.time()-start)


