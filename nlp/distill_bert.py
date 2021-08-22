from transformers import BertConfig, BertModel, AdamW

from transformers import BertTokenizer, BertForPreTraining
from torch.utils.data import TensorDataset, DataLoader, RandomSampler


tokenizer = BertTokenizer.from_pretrained('F:/ml/models/bert-base-cased')
teacher_model = BertForPreTraining.from_pretrained('F:/ml/models/bert-base-cased')


config = BertConfig.from_json_file('F:/ml/models/config.json')
student_model = BertModel(config=config)
student_model.init_weights()


import textbrewer
from textbrewer import GeneralDistiller
from textbrewer import TrainingConfig, DistillationConfig

# Show the statistics of model parameters
print("\nteacher_model's parametrers:")
result, _ = textbrewer.utils.display_parameters(teacher_model,max_level=3)
print (result)

print("student_model's parametrers:")
result, _ = textbrewer.utils.display_parameters(student_model,max_level=3)
print (result)

# Define an adaptor for interpreting the model inputs and outputs
def simple_adaptor(batch, model_outputs):
    # The second and third elements of model outputs are the logits and hidden states
    return {'logits': model_outputs[1],
            'hidden': model_outputs[2]}

# Training configuration
train_config = TrainingConfig()
# Distillation configuration
# Matching different layers of the student and the teacher
# We match 0-0 and 8-2 here for demonstration
distill_config = DistillationConfig(
    intermediate_matches=[
    {'layer_T':0, 'layer_S':0, 'feature':'hidden', 'loss': 'hidden_mse','weight' : 1},
    {'layer_T':8, 'layer_S':2, 'feature':'hidden', 'loss': 'hidden_mse','weight' : 1}])

# Build distiller
distiller = GeneralDistiller(
    train_config=train_config, distill_config = distill_config,
    model_T = teacher_model, model_S = student_model,
    adaptor_T = simple_adaptor, adaptor_S = simple_adaptor)

params = list(student_model.named_parameters())
all_trainable_params = divide_parameters(params, lr=args.learning_rate)
optimizer = AdamW(all_trainable_params, lr=args.learning_rate, correct_bias = False)

train_sampler = RandomSampler(train_dataset)
train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=args.forward_batch_size,drop_last=True)

# Start!
with distiller:
    distiller.train(optimizer, dataloader, num_epochs=1, scheduler_class=scheduler_class, scheduler_args=scheduler_args, callback=None)


