import numpy as np

class Sin:
    def __init__(self, connects: int=1):
        self.connects = connects
        self.inputs = None

    def forward(self, values: np.ndarray | list):
        self.inputs = [value[0] for value in values]
        return np.sin(self.inputs)
    
    # TODO: backward 만들기
    