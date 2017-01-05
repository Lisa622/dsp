# Matrix Algebra

import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([[6,2,-3,5]])
v = np.array([[3,5,-1,4]])
w = np.array([[1],[8],[0],[5]])

print (np.shape(A))
print (np.shape(B))
print (np.shape(C))
print (np.shape(D))
print (np.shape(u))
print (np.shape(v))
print (np.shape(w))
print (np.add(u,v))
print (np.subtract(u,v))
print (np.multiply(6,u))
print (np.inner(u,v))
print (np.linalg.norm(u))
print (np.add(A,C))
print (np.subtract(A,C.transpose()))
print (np.add(C.transpose(),3*D))
print (np.dot(B,A))
print (np.dot(B,A.transpose()))
