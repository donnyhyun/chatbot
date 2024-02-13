# cleaner_yaml.py

import yaml


def clean_yaml(chat_file):
    with open(chat_file, 'r') as file:
        d = yaml.load(file)
    return [text for convo in d['conversations'] for text in convo]
