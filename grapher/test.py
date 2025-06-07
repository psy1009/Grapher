# import slow_grapher
# from slow_grapher.grapher_core import *

# node = Node('input', 1)
# node2 = Node('input', 1)
# node3 = Node('*', 2)
# node4 = Node('input', 1)
# node5 = Node('input', 1)
# node6 = Node('*', 2)
# node7 = Node('*', 2)
# node.connect_to(node3)
# node2.connect_to(node3)
# node4.connect_to(node6)
# node5.connect_to(node6)
# node3.connect_to(node7)
# node6.connect_to(node7)
# node.forward_args = [1]
# node2.forward_args = [2]
# node4.forward_args = [3]
# node5.forward_args = [4]
# node.forward()
# node2.forward()
# node4.forward()
# node5.forward()

# node7.backward()
# print(node.grad, node2.grad, node3.grad, node4.grad, node5.grad, node6.grad, node7.grad)
