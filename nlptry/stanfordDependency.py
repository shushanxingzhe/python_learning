import stanfordnlp
import spacy

text = "Chris Manning is a nice person. Chris wrote a simple sentence. He also gives oranges to people."
#text = "Apple is looking at buying U.K. startup for $1 billion"
text = u"But Google is starting from behind. The company made a late push into hardware, and Apple Siri, available on iPhones, and Amazon Alexa software, which runs on its Echo and Dot devices, have clear leads in consumer adoption."
text = u"where is my order 18090600905502294345"
text = u"Google is built in 1990"
text = u"i give the children the toys"



stanfordModel = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
doc = stanfordModel(text)
doc.sentences[0].print_dependencies()


print('------------------------------')

spacyModel = spacy.load("en_core_web_sm")
doc = spacyModel(text)

for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])