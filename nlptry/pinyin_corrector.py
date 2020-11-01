import re

import jieba
from pypinyin import lazy_pinyin


def build_pinyin_index():
    stop_words = open('../data/chinese_stop_words.txt', encoding='utf-8').read().split()
    text = open('../data/west_journey.txt', encoding='utf-8').read()
    sentences = re.split(r'，|。|“|”|‘|’|！|？|；|：|、|…|《|》|【|】|{|}|（|）|-|\r\n|\n|　| |\t|\[|\]', text)
    sentences = list(filter(len, sentences))

    all_words = {}

    for sent in sentences:
        words = jieba.lcut(sent)
        for w in words:
            if w not in stop_words:
                if w in all_words:
                    all_words[w] += 1
                else:
                    all_words[w] = 1

    pinyin_index_result = {}

    all_words = sorted(all_words.items(), key=lambda item: item[1])
    for w, n in all_words:
        pinyin = ' '.join(lazy_pinyin(w))
        if pinyin in pinyin_index_result:
            pinyin_index_result[pinyin].append((w, n))
        else:
            pinyin_index_result[pinyin] = [(w, n)]
    return pinyin_index_result


pinyin_index = build_pinyin_index()


def str_product(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    return [v1 + v2 for v1 in list1 for v2 in list2]


def pinyin_product(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    return [v1 + ' ' + v2 for v1 in list1 for v2 in list2]


def possible_pinyin(words):
    start_possible_map = {
        'l': ['l', 'n'],
        'n': ['l', 'n'],
        's': ['s', 'sh'],
        'sh': ['s', 'sh'],
        'c': ['c', 'ch'],
        'ch': ['c', 'ch'],
        'z': ['z', 'zh', 'j'],
        'zh': ['z', 'zh'],
        'j': ['z', 'j'],
        'f': ['f', 'h'],
        'h': ['f', 'h'],
    }
    end_possible_map = {
        'n': ['n', 'ng'],
        'ng': ['n', 'ng'],
    }
    py = lazy_pinyin(words)
    zi_yin_list = []
    for zi in py:
        start = []
        mid = zi
        end = []
        if len(zi) > 1 and zi[:2] in start_possible_map:
            start = start_possible_map[zi[:2]]
            mid = mid[2:]
        elif zi[:1] in start_possible_map:
            start = start_possible_map[zi[:1]]
            mid = mid[1:]

        if len(zi) > 1 and zi[-2:] in end_possible_map:
            end = end_possible_map[zi[-2:]]
            mid = mid[:-2]
        elif zi[-1:] in end_possible_map:
            end = end_possible_map[zi[-1:]]
            mid = mid[:-1]
        res = [mid]
        if start:
            res = str_product(start, res)
        if end:
            res = str_product(res, end)
        zi_yin_list.append(res)

    possible_result = []
    for zi in zi_yin_list:
        possible_result = pinyin_product(possible_result, zi)
    return possible_result


def similar_words(word):
    global pinyin_index
    possible_py = possible_pinyin(word)
    option_result = []
    for item in possible_py:
        if item in pinyin_index:
            option_result += pinyin_index[item]
    option_result = sorted(option_result, key=lambda v: v[1], reverse=True)
    return option_result


print('大审: ', similar_words('大审'))
print('妹纸: ', similar_words('妹纸'))
print('肚几: ', similar_words('肚几'))
print('福利精: ', similar_words('福利精'))
