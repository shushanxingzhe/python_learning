from transformers import pipeline, DistilBertForSequenceClassification, DistilBertTokenizerFast
import pprint
from transformers import RobertaTokenizer, RobertaModel


unmasker = pipeline('fill-mask', model='roberta-base')
pprint.pprint(unmasker("Hello I'm a <mask> model."))


tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaModel.from_pretrained('roberta-base')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
pprint.pprint(output)


model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
print(classifier('I very like natural language processing', padding=True, truncation=True, max_length=512))

