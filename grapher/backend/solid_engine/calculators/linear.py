import numpy as np
from grapher.backend.solid_engine.core.basic import FuncNode, Config, number

# TODO: gb 식 완성하기

class Linear(FuncNode):
    def forward(self, x0, x1, b):
        output = x0.dot(x1)
        output = output + b
        return output

    def backward(self, gy):
        x0, x1, b = self.forward_args
        gx = np.dot(gy, x1.T)
        gW = np.dot(x0.T, gy)
        gb = np.ones_like(b)
        return [gW, gx, gb]
    
    def __repr__(self):
        return f'{self.name}(type=Linear)'
