from stanfordnlp.server import CoreNLPClient
import spacy

text = "Chris Manning is a nice person. Chris wrote a simple sentence. He also gives oranges to people."
#text = "Apple is looking at buying U.K. startup for $1 billion"
text = u"But Google is starting from behind. The company made a late push into hardware, and Apple Siri, available on iPhones, and Amazon Alexa software, which runs on its Echo and Dot devices, have clear leads in consumer adoption."
text = u"where is my order 18090600905502294345"
text = u"Google is built in 1990"

# set up the client
with CoreNLPClient(start_server=False,annotators=['tokenize','ssplit','pos','lemma','ner','depparse','coref'], timeout=30000, memory='2G') as client:
    # submit the request to the server
    ann = client.annotate(text)
    # get the first sentence
    for sentence in ann.sentence:
        for token in sentence.token:
            if token.ner != 'O':
             print(token.word,"\t",token.beginChar,"\t",token.endChar,"\t",token.pos,"\t",token.ner)


print('------------------------------')

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)