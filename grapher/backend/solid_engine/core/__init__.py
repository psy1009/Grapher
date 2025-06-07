# From basic.py
from .basic import FuncNode, NodeList, Graph, Config # basic classes
from .basic import Input, Number, Output # classes
from .basic import input_node, number, output_node, get_graph # functions

# From calculators.py
from .calculators import Add, Multiply, Negative, Subtract, Divide, Power # classes
from .calculators import add_node, multiply_node, negative_node, subtract_node, r_subtract_node, div_node, r_div_node, power_node # functions

FuncNode.__add__ = add_node
FuncNode.__mul__ = multiply_node
FuncNode.__neg__ = negative_node
FuncNode.__sub__ = subtract_node
FuncNode.__rsub__ = r_subtract_node
FuncNode.__truediv__ = div_node
FuncNode.__rtruediv__ = r_div_node
FuncNode.__pow__ = power_node

# # From advanced_calulators.py
# from .advanced_calculators import MatMul # classes
# from .advanced_calculators import matmul # functions

# From weight.py
from .weight import Weight # classes
from .weight import weight # functions