import os
import sys
import collections
import csv
import pandas as pd
import numpy as np
import tensorflow as tf
import pandas as pd
import numpy as np
import time

# BERT files

os.listdir("../bert")
sys.path.insert(0, '../bert')

from run_classifier import *
import modeling
import optimization
import tokenization


# import data

train=pd.read_csv('../input/jigsaw-unintended-bias-in-toxicity-classification/train.csv')
test=pd.read_csv('../input/jigsaw-unintended-bias-in-toxicity-classification/test.csv')

# remove new lines etc.

train['comment_text'] = train['comment_text'].replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)
test['comment_text'] = test['comment_text'].replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)

# force train into cola format, test is fine as it is

train['dummy_1'] = 'meh'
train['dummy_2'] = '*'

train = train[['dummy_1','target','dummy_2','comment_text']]
train['target'] = np.where(train['target']>=0.5,1,0)

train = train.sample(frac=0.33)

# export as tab seperated

train.to_csv('train.tsv', sep='\t', index=False, header=False)
test.to_csv('test.tsv', sep='\t', index=False, header=True)

task_name = 'cola'
bert_config_file = '../input/pretrained-bert-including-scripts/uncased_l-12_h-768_a-12/uncased_L-12_H-768_A-12/bert_config.json'
vocab_file = '../input/pretrained-bert-including-scripts/uncased_l-12_h-768_a-12/uncased_L-12_H-768_A-12/vocab.txt'
init_checkpoint = '../input/pretrained-bert-including-scripts/uncased_l-12_h-768_a-12/uncased_L-12_H-768_A-12/bert_model.ckpt'
data_dir = './'
output_dir = './'
do_lower_case = True
max_seq_length = 72
do_train = True
do_eval = False
do_predict = False
train_batch_size = 32
eval_batch_size = 32
predict_batch_size = 32
learning_rate = 2e-5
num_train_epochs = 1.0
warmup_proportion = 0.1
use_tpu = False
master = None
save_checkpoints_steps = 99999999 # <----- don't want to save any checkpoints
iterations_per_loop = 1000
num_tpu_cores = 8
tpu_cluster_resolver = None
