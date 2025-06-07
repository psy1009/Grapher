import numpy as np
from grapher.solid.core import *
from grapher.solid.dl import *

class Block(object):
    def __init__(self):
        pass
    
    def forward(self, *args):
        raise NotImplementedError()
    
    def backward(self, *args):
        raise NotImplementedError('You cannot use backward method in Block objects.')
