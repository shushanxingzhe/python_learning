import stanfordnlp

nlp = stanfordnlp.Pipeline(processors='tokenize,lemma,pos', lang='en')


def lemma(token):
    res = nlp(token)
    return res.sentences[0].tokens[0].words[0].lemma


def tokenize(text):
    doc = nlp(text)
    tokens = []
    for i, sentence in enumerate(doc.sentences):
        for token in sentence.tokens:
            tokens.append(token.text)
    return tokens


def pos(text):
    doc = nlp(text)
    tokens = []
    for i, sentence in enumerate(doc.sentences):
        for token in sentence.tokens:
            tokens.append((token.text,token.words[0].xpos))
    return tokens

sent = "fadsgsafdsfsa,swimming, Love this so comfortable. I got it in a size medium but I am usually a size small would recommend to size up one size if you don't want the shirt to be to cropped overall perfect fit ."

tokens = tokenize(sent)
for token in tokens:
    print(token, lemma(token))

# pos_tokens = pos(sent)
# for token in pos_tokens:
#     print(token)
exit()
text = 'Soft material is very good .True to color and size .Can be paired with any top.Can be wear in office as well as any casual outing .'
tks = tokenize(text)
print(tks)

text = 'but its a_B_SIZE little_I_SIZE loose_I_SIZE on the hips .'
tks = tokenize(text)
print(tks)

text = 'it is at least wealth $100.88.'
tks = tokenize(text)
print(tks)

text = "Wasn't my favorite purchase,0,27,Wasn't my favorite purchase but the short_B_SIZE is cute ."
tks = tokenize(text)
print(tks)

