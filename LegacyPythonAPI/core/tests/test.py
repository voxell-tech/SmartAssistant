import numpy as np

# import tensorflow as tf
# from transformers import BertTokenizer, TFBertForNextSentencePrediction, BertConfig


# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = TFBertForNextSentencePrediction.from_pretrained('bert-base-uncased')
# input_ids = tf.constant(tokenizer.encode("Hello, my dog is cute", add_special_tokens=True))[None, :]  # Batch size 1
# outputs = model(input_ids)
# seq_relationship_scores = outputs[0]
# print(seq_relationship_scores)
# print(outputs)


# import tensorflow as tf
# from transformers import BertTokenizer, TFBertModel

# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = TFBertModel.from_pretrained('bert-base-uncased')
# input_ids = tf.constant(tokenizer.encode("Hello, my dog is cute", add_special_tokens=True))[None, :]  # Batch size 1
# outputs = model(input_ids)
# last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple
# print(len(outputs))
# print(last_hidden_states.shape)
# print(last_hidden_states)


import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2Model

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2Model.from_pretrained('gpt2')
input_ids = tf.constant(tokenizer.encode("Hello, my dog is cute", add_special_tokens=True))[None, :]  # Batch size 1
outputs = model(tf.constant(np.zeros(512), dtype=tf.int32))
last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple
print(last_hidden_states)

"""
2/1000  [..............................] - ETA: 35:11 - loss: 4.8702 - accuracy: 0.3667
3/1000  [..............................] - ETA: 27:15 - loss: 4.0524 - accuracy: 0.4778
4/1000  [..............................] - ETA: 23:17 - loss: 3.8355 - accuracy: 0.5167
5/1000  [..............................] - ETA: 20:49 - loss: 3.4946 - accuracy: 0.5467
6/1000  [..............................] - ETA: 19:10 - loss: 2.9788 - accuracy: 0.6111
7/1000  [..............................] - ETA: 18:01 - loss: 2.8357 - accuracy: 0.6238
8/1000  [..............................] - ETA: 17:07 - loss: 2.5323 - accuracy: 0.6667
9/1000  [..............................] - ETA: 16:25 - loss: 2.7100 - accuracy: 0.6481
10/1000 [..............................] - ETA: 15:52 - loss: 2.6429 - accuracy: 0.6567
"""
