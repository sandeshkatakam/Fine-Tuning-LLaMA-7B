import torch
from huggingface import transformers
import json

configs = json.load("config.json")


class fine_tuning(transformers):
    def __init__(self, configs):
        super().__init__()
        self.configs = configs