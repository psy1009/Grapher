import numpy as np

class Input:
    def __init__(self):
        self.data = None
        
    def forward(self, data: float | int):
        self.data = data
        return self.data
    
    def backward(self, inheriting_value: np.ndarray | float):
        return np.array([inheriting_value])

class Add:
    def __init__(self, connects):
        self.connects = connects
    
    def forward(self, values: np.ndarray | list):
        self.inputs = [value[0] for value in values]
        return np.array([sum(values)])
    
    def backward(self, inheriting_value: np.ndarray | float):
        if type(inheriting_value) in [list, np.ndarray]: inheriting_value = inheriting_value[0]
        return np.array([inheriting_value for _ in range(self.connects)])

class Multiply:
    def __init__(self, connects):
        self.connects = connects
        self.inputs = None
        self.ans = None
            
    def forward(self, values: np.ndarray | list):
        self.inputs = [value[0] for value in values]
        self.ans = 1
        for value in values:
            self.ans *= value[0]
        return np.array([self.ans])
    
    def backward(self, inheriting_value: np.ndarray | float):
        if type(inheriting_value) in [list, np.ndarray]: inheriting_value = inheriting_value[0]
        return np.array([(self.ans / self.inputs[input_idx]) * inheriting_value for input_idx in range(self.connects)])

class Square:
    def __init__(self, connects: int=1):
        self.connects = connects
        self.inputs = None
        
    def forward(self, values: np.ndarray | list):
        self.inputs = [value[0] for value in values]
        return np.array([values[0][0] ** 2])
    
    def backward(self, inheriting_value: np.ndarray | float):
        if type(inheriting_value) in [list, np.ndarray]: inheriting_value = inheriting_value[0]
        print(self.inputs[0], inheriting_value)
        return np.array([2 * self.inputs[0] * inheriting_value])

        