class Trie(object):
    def __init__(self):
        self.trie = {}
        self.count = 0
        self.max_retrieve_words = 3

    def build_trie(self, words):
        for w in words:
            w = w.strip()
            cur = self.trie
            for c in w:
                if c in cur:
                    cur = cur[c]
                else:
                    cur[c] = {}
                    cur = cur[c]
            cur[None] = None

    def retrieve_word(self, cur, prefix):
        if cur == {}:
            return [prefix]
        ret = []
        if self.count >= self.max_retrieve_words:
            return []
        for c in cur:
            if c is None:
                ret.append(prefix)
                self.count += 1
            else:
                ret.extend(self.retrieve_word(cur[c], prefix + c))
        return ret

    def find_words(self, word):
        cur = self.trie
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur = {}
                break
        if cur != {}:
            print(cur)
            self.count = 0
            return self.retrieve_word(cur, word)
        else:
            return []


trie = Trie()
words_counter = {'hello': 10, 'world': 7, 'whereas': 2, 'where': 8, 'what': 9, 'when': 7, 'who': 6}
words_counter_list = sorted(words_counter.items(), key=lambda kv: kv[1], reverse=True)
words_sorted = [word[0] for word in words_counter_list]
trie.build_trie(words_sorted)
print(trie.find_words('wh'))
print(trie.find_words('whe'))
print(trie.find_words('wherever'))

trie = Trie()
words_counter = {'连衣裙': 20, '连衣裙 红色': 5, '牛仔裤': 30, '牛仔裤 男': 13, '连衣裙 长袖': 9, '牛仔裤 破洞': 7}
words_counter_list = sorted(words_counter.items(), key=lambda kv: kv[1], reverse=True)
words_sorted = [word[0] for word in words_counter_list]
trie.build_trie(words_sorted)
print(trie.find_words('连衣裙'))
print(trie.find_words('牛仔'))
print(trie.find_words('啤酒'))
