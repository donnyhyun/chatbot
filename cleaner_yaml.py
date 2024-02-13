# cleaner_yaml.py

import yaml


def clean_yaml(chat_file):
    with open(chat_file, 'r') as file:
        d = yaml.load(file)
    convos = d['conversations']
    return ["".join(msg) for msg in convos]
