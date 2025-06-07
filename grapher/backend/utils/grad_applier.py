__all__ = ['GradApplier', 'grad_applied']

class GradApplier(object):
    def __init__(self, nodes):
        self.nodes = nodes
        
    def update(self):
        for node in self.nodes:
            self.update_one(node)
            
    def update_one(self, node):
        raise NotImplementedError()

def grad_applied(value, grad, lr):
    return value - grad * lr
