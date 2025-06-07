import numpy as np
from grapher.backend.solid_engine import *
from grapher.solid.blocks.basic import Block

__all__ = ['Linear']

class Linear(Block):
    def __init__(self, in_features, out_features):
        self.w = weight(np.random.random((in_features, out_features)))
        self.b = number(np.random.random((out_features,)))
        
    def forward(self, x):
        return matmul(x, self.w) + self.b
