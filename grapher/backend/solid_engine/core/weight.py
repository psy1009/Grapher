from grapher.backend.solid_engine.core import Number, Config

class Weight(Number):
    def __repr__(self):
        return f"{self.name}(data={self.data}, type=Weight)"

def weight(data: int | float, add_to_graph: bool=True, name: str="NoName"):
    number_node = Weight(data=data, name=name)
    if add_to_graph: Config.current_graph.add_node(number_node)
    return number_node
