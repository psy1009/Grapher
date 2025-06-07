import numpy as np
from grapher.solid.core.basic import Config, FuncNode
from grapher.solid.utils import *

__all__ = ['Add', 'add_node',
           'Multiply', 'multiply_node',
           'Negative', 'negative_node',
           'Subtract', 'subtract_node', 'r_subtract_node',
           'Divide', 'div_node', 
           'Power', 'power_node']

# Adder class
class Add(FuncNode):
    def forward(self, x0, x1):
        output = as_array(x0) + as_array(x1)
        return output

    def backward(self, gy):
        return [gy, gy]

    def __repr__(self):
        return "{}(type=Add)".format(self.name)
    
def add_node(x0, x1, add_to_graph: bool=True, name: str="NoName"):
    _add_node = Add(name=name)
    _add_node.connect(x0, x1)
    if add_to_graph: Config.current_graph.add_node(_add_node)
    return _add_node    

# Multiplier class
class Multiply(FuncNode):
    def forward(self, x0, x1):
        output = as_array(x0) * as_array(x1)
        return output
    
    def backward(self, gy):
        x0, x1 = self.forward_args
        return [as_array(x1) * gy, as_array(x0) * gy]

    def __repr__(self):
        return "{}(type=Multiply)".format(self.name)
    
def multiply_node(x0, x1, add_to_graph: bool=True, name: str="NoName"):
    _multiply_node = Multiply(name=name)
    _multiply_node.connect(x0, x1)
    if add_to_graph: Config.current_graph.add_node(_multiply_node)
    return _multiply_node    

# Negativer class
class Negative(FuncNode):
    def forward(self, x):
        return -as_array(x)
    
    def backward(self, gy):
        return [-gy]
    
    def __repr__(self):
        return "{}(type=Negative)".format(self.name)
    
def negative_node(x, add_to_graph: bool=True, name: str="NoName"):
    _negative_node = Negative(name=name)
    _negative_node.connect(x)
    if add_to_graph: Config.current_graph.add_node(_negative_node)
    return _negative_node

#Subtracter class
class Subtract(FuncNode):
    def forward(self, x0, x1):
        output = as_array(x0) - as_array(x1)
        return output
    
    def backward(self, gy):
        return [gy, -gy]
    
    def __repr__(self):
        return "{}(type=Subtract)".format(self.name)
    
def subtract_node(x0, x1, add_to_graph: bool=True, name: str="NoName"):
    _subtraction_node = Subtract(name=name)
    _subtraction_node.connect(x0, x1)
    if add_to_graph: Config.current_graph.add_node(_subtraction_node)
    return _subtraction_node

def r_subtract_node(x0, x1, add_to_graph: bool=True, name: str="NoName"):
    _r_subtraction_node = Subtract(name=name)
    _r_subtraction_node.connect(x1, x0)
    if add_to_graph: Config.current_graph.add_node(_r_subtraction_node)
    return _r_subtraction_node

# Divider class
class Divide(FuncNode):
    def forward(self, x0, x1):
        return as_array(x0) / as_array(x1)
    
    def backward(self, gy):
        x0, x1 = self.forward_args
        gx0 = gy / x1
        gx1 = gy * (-x0 / x1 ** 2)
        return [gx0, gx1]
    
    def __repr__(self):
        return "{}(type=Divide)".format(self.name)
    
def div_node(x0, x1, add_to_graph: bool=True, name: str="NoName"):
    _div_node = Divide(name=name)
    _div_node.connect(x0, x1)
    if add_to_graph: Config.current_graph.add_node(_div_node)
    return _div_node

def r_div_node(x0, x1, add_to_graph: bool=True, name: str="NoName"):
    _r_div_node = Divide(name=name)
    _r_div_node.connect(x1, x0)
    if add_to_graph: Config.current_graph.add_node(_r_div_node)
    return _r_div_node

# Powerer class
class Power(FuncNode):
    def forward(self, x, c):
        return as_array(x) ** as_array(c)
    
    def backward(self):
        gy = self.gy
        x, c = self.forward_args
        gx = c * x ** (c - 1) * gy
        return [gx]
    
    def __repr__(self):
        return "{}(type=Power)".format(self.name)
    
def power_node(x, c, add_to_graph: bool=True, name: str="NoName"):
    _power_node = Power(name=name)
    _power_node.connect(x, c)
    if add_to_graph: Config.current_graph.add_node(_power_node)
    return _power_node
