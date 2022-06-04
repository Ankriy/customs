import json
import re
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


maxSequenceLength = 40
model = load_model('models/my_model/1')

with open('categories.json', 'r') as f:
    categories = json.load(f)


with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)


reversed_categories = dict((v, int(k)) for k, v in categories.items())


def clear_text(data):
    data = re.sub(r"[^\w\s]", " ", str(data).lower()) # понижение в нижний регист и удаление знаки препинания
    data = ' '.join(words for words in data.split())
    return data


def prep_text(texts, tokenizer, max_sequence_length):
    text_sequences = tokenizer.texts_to_sequences(texts)
    return pad_sequences(text_sequences, maxlen=max_sequence_length, padding='post')


def prep_data(text):
    data = clear_text(text)
    return prep_text([data], tokenizer, maxSequenceLength)


def predict_model(data):
    data = prep_data(data)
    return model.predict(data)