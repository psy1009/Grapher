import numpy as np
import contextlib
from grapher.solid.utils import as_array

__all__ = ['FuncNode',
           'NodeList',
           'Number', 'number',
           'Input', 'input_node',
           'Output', 'output_node',
           'Graph',
           'Config', 'get_graph']

# Node class
class FuncNode(object):
    def __init__(self, name="NoName", base_grad=None):
        self.grad: int | float = base_grad
        self.name: str = name
        self.backward_available: bool = True
        self.connected_nodes: list[list[FuncNode], list[FuncNode]] = [[], []] # [뒤로 연결된 노드들, 앞으로 연결된 노드들]
        self.forward_args: list = []
        self.gy: int | float = 1
    
    def __call__(self, is_backward: bool=False):
        if not is_backward:
            print(f'forward_args: {self.forward_args}')
            for node in self.connected_nodes[1]:
                node.forward_args.append(as_array(self.forward(*self.forward_args)))
        else:
            gy = as_array(self.gy)
            self.grad = gy if self.grad is None else self.grad + gy
            if self.backward_available:
                gxs = self.backward(gy)
                # print(self.connected_nodes, gxs)
                for node, gx in zip(self.connected_nodes[0], gxs): node.gy = gx
    
    def connect(self, *nodes):
        self.connected_nodes[0] = nodes
        for node in nodes: node.connected_nodes[1].append(self)
        
    def connect_to(self, *nodes):
        self.connected_nodes[1] = nodes
        for node in nodes: node.connected_nodes[0].append(self)
        
    def unconnect(self, node):
        if node in self.connected_nodes:
            self.connected_nodes.remove(node)
    
    def forward(self, x):
        raise NotImplementedError()
    
    def backward(self, gy):
        raise NotImplementedError()
    
    def __repr__(self):
        return "{}(type=Node)".format(self.name)

class NodeList(object):
    def __init__(self, nodes: list[FuncNode]):
        self.nodes = nodes
        self._current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = len(nodes)    # 반복을 끝낼 숫자
 
    def __iter__(self):
        return self         # 현재 인스턴스를 반환
 
    def __next__(self):
        if self._current < self.stop:
            r = self._current
            self._current += 1     
            return self.nodes[r]                
        else:                           
            raise StopIteration
        
    def __len__(self):
        return self.stop
        
    def cleargrad(self):
        for node in self.nodes:
            node.grad = None

# Number class
class Number(FuncNode):
    def __init__(self, data, name: str="NoName", base_grad=None):
        super().__init__(name=name, base_grad=base_grad)
        self.backward_available = False
        self.data: int | float = as_array(data)
    
    def forward(self):
        return self.data
    
    def update_data(self, value):
        self.data = self.data + value
    
    def __repr__(self):
        return "{}(data={}, type=Number)".format(self.name, self.data)

def number(data: int | float, add_to_graph: bool=True, name: str="NoName"):
    number_node = Number(data=data, name=name)
    if add_to_graph: Config.current_graph.add_node(number_node)
    return number_node

# Input class
class Input(FuncNode):
    def __init__(self, name="NoName", base_grad=None):
        super().__init__(name=name, base_grad=base_grad)
        self.backward_available = False
        self.data: int | float = None
        
    def put_data(self, data):
        self.data = as_array(data)
        
    def forward(self):
        return self.data
    
    def __repr__(self):
        return "{}(type=InputNode)".format(self.name)

def input_node(add_to_graph: bool=True, name: str="NoName"):
    _input_node = Input(name=name)
    if add_to_graph:
        Config.current_graph.add_node(_input_node)
        Config.current_graph.add_input_node(_input_node)
    return _input_node

# Output class
class Output(FuncNode):
    def __call__(self, is_backward=False):
        if not is_backward:
            return self.forward_args
        else:
            return self.backward
    
    def set_gy(self, gy: int | float):
        self.gy = gy
    
    def forward(self):
        return self.forward_args

    def backward(self):
        gy = self.gy
        return [gy]
    
    def __repr__(self):
        return "{}(type=OutputNode)".format(self.name)
    
def output_node(node: FuncNode, add_to_graph: bool=True, name: str="NoName"):
    _output_node = Output(name=name)
    _output_node.connect(node)
    if add_to_graph: Config.current_graph.add_node(_output_node)
    return _output_node

# Graph class
class Graph(object):
    def __init__(self):
        self.forward_available: bool = True
        self.backward_available: bool = False
        self.trainable: bool = False
        self.input_nodes: list[Input] = []
        self.nodes: list[FuncNode] = []
    
    def add_node(self, node):
        self.nodes.append(node)
    
    def add_input_node(self, node):
        self.input_nodes.append(node)
    
    def set_input_data(self, *datas: int | float):
        for input_node, data in zip(self.input_nodes, datas):
            input_node.put_data(data)
    
    def forward(self, datas: list[int | float]) -> np.ndarray:
        assert self.forward_available, "This graph's attribute forward_available must be True, current forward_avaiable: {}".format(self.forward_available)
        self.set_input_data(*datas)
        for node in self.nodes:
            output = node()
        return output
    
    def backward(self, base_grad: int | float=1):
        assert self.backward_available, "This graph's attribute backward_available must be True, current backward_avaiable: {}".format(self.backward_available)
        nodes = self.nodes[::-1]
        nodes[0].set_gy(base_grad)
        for node in nodes: node(is_backward=True)
    
    @contextlib.contextmanager
    def making_structure(self):
        old_value = getattr(Config, "current_graph")
        Config.current_graph = self
        try: yield
        finally: Config.current_graph = old_value
    
    @contextlib.contextmanager
    def flow(self, direction="forward"):
        if direction == "forward":
            old_value = self.forward_available
            self.forward_available = True
        elif direction == "backward":
            old_value = self.backward_available
            self.backward_available = True
        try: yield "Current flow: {}".format(direction)
        finally:
            if direction == "forward": self.forward_available = old_value
            elif direction == "backward": self.backward_available = old_value

    def cleargrad(self):
        for node in self.nodes: node.grad = None
    
    def test_backward(self, value):
        if self.backward_available:
            print(value)


class Config:
    current_graph = Graph()
    eval_mode = False

def get_graph():
    return Config.current_graph
    