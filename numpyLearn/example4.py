import numpy as np
a=np.ones((2,3),dtype=np.float64)
b = np.random.random((2,3))
a*=3
print(a)
b+=a
print(b)
a+=b
print(a)
print(a.sum())
print(a.max())
print(a.min())
print(a.sum(axis=0))
print(a.cumsum(axis=0))

B = np.arange(3)
print(np.exp(B))
print(np.sqrt(B))