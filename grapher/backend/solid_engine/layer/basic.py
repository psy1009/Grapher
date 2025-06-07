# from grapher.backend.solid_engine.core import FuncNode

class Layer:
    def __init__(self):
        self.forward_args = []
        self.params = []
        
    def __call__(self):
        self.forward(*self.forward_args)
    
    def parameters(self):
        return self.params
    
    def forward(self, x):
        raise NotImplementedError()
    