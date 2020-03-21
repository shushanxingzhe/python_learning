from pywubi import wubi
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def letter2gram(text):
    if len(text) == 0:
        return []
    text = text.lower()
    text = re.sub(r'\W+', '_', text)
    text = '_' + text + '_'
    result = re.findall(r'(?=([a-z_]{2}))', text)
    return result


def get_letter_bigram_map():
    alphabet = 'abcdefghijklmnopqrstuvwxyz_'
    alphabet_len = len(alphabet)
    bigram_map = {}
    for i, li in enumerate(alphabet):
        for j, lj in enumerate(alphabet):
            bigram_map[li + lj] = i * alphabet_len + j
    return bigram_map


letter_bigram_map = get_letter_bigram_map()
letter_bigram_map_len = len(letter_bigram_map)


def encode_letter_bigram(text):
    text = ' '.join(wubi(text))
    data = letter2gram(text)
    encode = np.zeros(letter_bigram_map_len, dtype=np.float32)
    for item in data:
        encode[letter_bigram_map[item]] += 1
    return encode


query = encode_letter_bigram('南冒')
target = encode_letter_bigram('南昌')

print(cosine_similarity(query.reshape(1, -1), target.reshape(1, -1)))

districts = ['福州', '广州', '北京', '上海', '深圳', '兰州', '长沙', '武汉', '沈阳', '南京', '洛阳', '岳阳', '天津',
             '西安', '昆明', '拉萨', '南昌', '浏阳', '南宁', '南阳', '南海']
vectors = []
for i in districts:
    vectors.append(encode_letter_bigram(i))

import faiss

index = faiss.IndexFlatL2(letter_bigram_map_len)
print(index.is_trained)
index.add(np.array(vectors))
print(index.ntotal)

print('query:', '南冒')
D, I = index.search(np.array([query]), 3)
for i in I[0]:
    print(districts[i])

# query: 南冒
# 南昌
# 南宁
# 南京


print('query:', '刘阳')
query = encode_letter_bigram('刘阳')
D, I = index.search(np.array([query]), 3)
for i in I[0]:
    print(districts[i])
# query: 刘阳
# 浏阳
# 沈阳
# 岳阳
