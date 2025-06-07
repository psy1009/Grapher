class ConnectLimitError(Exception):
    def __init__(self, erorr_node):
        super().__init__(f"Too many connected nodes: limit: {erorr_node.connects}, connected: {max(len(erorr_node.backward_connected_nodes), len(erorr_node.forward_connected_nodes))}")