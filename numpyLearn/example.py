import numpy as np
a=np.arange(1,11,3).reshape(2,2)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.size)
print(a.itemsize)
print(type(a))
b=np.array([1,2,3,4,7])
print(b)