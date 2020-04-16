class Trie(object):
    def __init__(self):
        self.trie = {}

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
        for c in cur:
            if c is None:
                ret.append(prefix)
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
            return self.retrieve_word(cur, word)
        else:
            return []


trie = Trie()
trie.build_trie(['hello', 'world', 'whereas', 'where', 'what', 'when', 'who'])
print(trie.find_words('wh'))
print(trie.find_words('whe'))
print(trie.find_words('wherever'))

trie = Trie()
trie.build_trie(['连衣裙', '连衣裙 红色', '牛仔裤', '牛仔裤 男', '连衣裙 长袖', '牛仔裤 破洞'])
print(trie.find_words('连衣裙'))
print(trie.find_words('牛仔'))
print(trie.find_words('啤酒'))
