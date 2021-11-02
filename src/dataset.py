# 
import os 

# perform http/https/queries
import requests

class Dataset:
    def __init__(self) -> None:
        self.data_sources = []
        self.target_genes = None

    def get_data(self, data_source:int=0, n_samples:int=100) -> list:
        pass

    def convert_to(self, format:str="txt")-> None:
        pass