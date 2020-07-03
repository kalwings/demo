import numpy as np
from sys import getsizeof as size
X = [1,2,3,4,5,6,7,8,9,10]
Y = np.array(X,np.int8)
print(size([]))
print(size(np.array([])))
print(size(X)-56)
print(size(Y)-96)
Z = Y/2
print(Z)
for i in X:
    W = i/2
    print(W)
