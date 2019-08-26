from flair.data import Sentence
from flair.models import SequenceTagger

# make a sentence
sentence = Sentence('But Google is starting from behind. The company made a late push into hardware, and Apple Siri, available on iPhones, and Amazon Alexa software, which runs on its Echo and Dot devices, have clear leads in consumer adoption.')

# load the NER tagger
tagger = SequenceTagger.load('ner')

# run NER over sentence
tagger.predict(sentence)