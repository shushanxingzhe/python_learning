from datasets import load_dataset
import textbrewer
from textbrewer import GeneralDistiller
from textbrewer import TrainingConfig, DistillationConfig
from transformers import DistilBertForSequenceClassification, DistilBertConfig, AdamW, DistilBertTokenizerFast
from transformers import get_linear_schedule_with_warmup
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

# device
device = torch.device('cuda' if torch.cuda.is_available()  else 'cpu')

# Define models
teacher_model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english', output_hidden_states=True)
teacher_model.output_hidden_states = True
# Teacher should be initialized with pre-trained weights and fine-tuned on the downstream task.
# For the demonstration purpose, we omit these steps here

bert_config_l3 = DistilBertConfig.from_json_file('distilbert_l3.json')
bert_config_l3.output_hidden_states = True
student_model = DistilBertForSequenceClassification(bert_config_l3)  # , num_labels = 2
student_model.init_weights()
teacher_model.to(device=device)
student_model.to(device=device)

tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')


def tokenize(batch):
    return tokenizer(batch['text'], padding=True, truncation=True)


train_dataset, eval_dataset = load_dataset('imdb', split=['train', 'test'])
print(len(train_dataset), len(eval_dataset))
# train_dataset = train_dataset.shuffle().select(range(3000))
eval_dataset = train_dataset.shuffle().select(range(2000))


train_dataset = train_dataset.map(tokenize, batched=True, batch_size=32)
eval_dataset = eval_dataset.map(tokenize, batched=True, batch_size=32)

train_dataset = train_dataset.rename_column('label', 'labels')
eval_dataset = eval_dataset.rename_column('label', 'labels')
train_dataset.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'])
eval_dataset.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'])

dataloader = DataLoader(train_dataset, batch_size=32)
num_epochs = 10
num_training_steps = len(dataloader) * num_epochs
# Optimizer and learning rate scheduler
optimizer = AdamW(student_model.parameters(), lr=1e-4)

scheduler_class = get_linear_schedule_with_warmup
# arguments dict except 'optimizer'
scheduler_args = {'num_warmup_steps': int(0.1 * num_training_steps), 'num_training_steps': num_training_steps}

# display model parameters statistics
print("\nteacher_model's parametrers:")
result, _ = textbrewer.utils.display_parameters(teacher_model, max_level=3)
print(result)

print("student_model's parametrers:")
result, _ = textbrewer.utils.display_parameters(student_model, max_level=3)
print(result)


def simple_adaptor(batch, model_outputs):
    # The second element of model_outputs is the logits before softmax
    # The third element of model_outputs is hidden states
    return {'logits': model_outputs[1],
            'hidden': model_outputs[2],
            'inputs_mask': batch['attention_mask']}


# Define callback function
def predict(model, eval_dataset, step, device):
    '''
    eval_dataset: 验证数据集
    '''
    model.eval()
    pred_logits = []
    label_ids = []
    dataloader = DataLoader(eval_dataset, batch_size=32)
    for batch in dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels']
        with torch.no_grad():
            model_output = model(input_ids=input_ids, attention_mask=attention_mask)
            logits = model_output.logits.detach().cpu()

        for i in range(len(logits)):
            pred_logits.append(logits[i].numpy())
            label_ids.append(labels[i])
    model.train()
    pred_logits = np.array(pred_logits)
    label_ids = np.array(label_ids)
    y_p = pred_logits.argmax(axis=-1)
    accuracy = (y_p == label_ids).sum() / len(label_ids)
    print("Number of examples: ", len(y_p))
    print("Acc: ", accuracy)


from functools import partial

callback_fun = partial(predict, eval_dataset=eval_dataset, device=device)  # fill other arguments

# Initialize configurations and distiller
train_config = TrainingConfig(device=device)
distill_config = DistillationConfig(
    temperature=8,
    hard_label_weight=0,
    kd_loss_type='ce',
    probability_shift=False,
    intermediate_matches=[
        {'layer_T': 0, 'layer_S': 0, 'feature': 'hidden', 'loss': 'hidden_mse', 'weight': 1},
        {'layer_T': 3, 'layer_S': 1, 'feature': 'hidden', 'loss': 'hidden_mse', 'weight': 1},
        {'layer_T': 5, 'layer_S': 2, 'feature': 'hidden', 'loss': 'hidden_mse', 'weight': 1},
        {'layer_T': [0, 0], 'layer_S': [0, 0], 'feature': 'hidden', 'loss': 'nst', 'weight': 1},
        {'layer_T': [3, 3], 'layer_S': [1, 1], 'feature': 'hidden', 'loss': 'nst', 'weight': 1},
        {'layer_T': [5, 5], 'layer_S': [2, 2], 'feature': 'hidden', 'loss': 'nst', 'weight': 1}]
)

print("train_config:")
print(train_config)

print("distill_config:")
print(distill_config)

distiller = GeneralDistiller(
    train_config=train_config, distill_config=distill_config,
    model_T=teacher_model, model_S=student_model,
    adaptor_T=simple_adaptor, adaptor_S=simple_adaptor)

# Start distilling
with distiller:
    distiller.train(optimizer, dataloader, num_epochs=num_epochs,
                    scheduler_class=scheduler_class, scheduler_args=scheduler_args, callback=callback_fun)