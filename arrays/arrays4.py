import numpy as np
A = np.array([[1,2],[4,5]],np.int8)
B = np.array([[6,7],[8,10]],np.int8)
C = np.add(A,B)
#print(C)
D = np.subtract(A,B)
E = np.multiply(A,B)
F = np.divide(A,B)
#print(D)
print(E)
#print(F)
G = A%B
#print(G)
H = np.matmul(A,B)
print(H)
Inv = np.linalg.inv(A)
print(Inv)
print(np.matmul(A,Inv))