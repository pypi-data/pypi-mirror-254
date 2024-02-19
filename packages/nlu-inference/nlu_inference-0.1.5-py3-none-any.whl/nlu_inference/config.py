import catalogue
from confection import Config


class registry(catalogue.Registry):
    
    tokenizers = catalogue.create("nlu", "tokenizers", entry_points=True)
    inference = catalogue.create("nlu", "inference", entry_points=True)
    
    

__all__ = ["registry", "Config"]