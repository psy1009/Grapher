import numpy as np
from grapher.backend.solid_engine.core.basic import FuncNode, Config, number
from grapher.backend.solid_engine.core.calculators import *

class MatMul(FuncNode):
    def forward(self, x0, x1):
        output = x0.dot(x1)
        return output

    def backward(self, gy):
        x0, x1 = self.forward_args
        gx = np.dot(gy, x1.T)
        gW = np.dot(x0.T, gy)
        return [gW, gx]
    
    def __repr__(self):
        return f'{self.name}(type=MatMul)'
    
def matmul(x, W, add_to_graph: bool=True, name: str="NoName"):
    _matmul_node = MatMul(name=name)
    _matmul_node.connect(x, W)
    if add_to_graph: Config.current_graph.add_node(_matmul_node)
    return _matmul_node
