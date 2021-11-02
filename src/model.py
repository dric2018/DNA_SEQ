import numpy as np

class Model:
    def __init__(self) -> None:
        self.bases = {
            'A':0, 'C':1, 'T':2, 'G':3
        }
        self.transition_matrix = np.zeros()

    def compute_transition_matrix(self, genome:str) -> None:
        """
            Updates the transition matrix given some genomes (DNA sequences)

            :param :genome (str)
                The genome sequence 
        """
        pass

    def find_pattern(self, pattern:str) -> int:
        pass

