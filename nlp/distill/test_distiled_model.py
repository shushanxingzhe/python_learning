import torch
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast, DistilBertConfig, pipeline


state_dict = torch.load('saved_models/gs282.pkl')
bert_config_l3 = DistilBertConfig.from_json_file('distilbert_l3.json')
model = DistilBertForSequenceClassification(bert_config_l3)
model.load_state_dict(state_dict)
# model.save_pretrained('distilled_model')
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')

classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
print(classifier('I love it'))
print(classifier('I don\'t love it'))
print(classifier('I hate it'))
print(classifier('I don\'t hate it'))
print(classifier('It is disgust'))
