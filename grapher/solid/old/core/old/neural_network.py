from grapher_core import *
from tqdm import tqdm

layer1 = [Node('input', 1)]
layer2 = [Node('input', 1), Node('*', 2)]
mse = [Node('input', 1), Node('+', 2), Node('square', 1)]

layer1[0].connect_to(layer2[1])
layer2[0].connect_to(layer2[1])
layer2[1].connect_to(mse[1])
mse[0].connect_to(mse[1])
mse[1].connect_to(mse[2])
x = np.arange(1, 11)
y = x ** 2

print(layer1, layer2, mse)
layer2[0].forward_args = [1]
for epoch in range(1):
    for i in tqdm(range(len(x))):
        x_i, y_i = x[i], y[i]
        print('X, Y: ', x_i, y_i)
        mse[0].forward_args = [y_i]
        layer1[0].forward_args = [x_i]
        layer1[0].forward()
        layer2[0].forward()
        mse[0].forward()
        mse[2].backward()
        print('Gradient: ', layer2[0].grad)
        layer2[0].forward_args -= layer2[0].grad
        
print('Final weight: ', layer2[0].forward_args)
