import numpy as np
a=np.array([1,2,3,4])
print(a)
b=np.array([(1,2,3,4),(11,12,14,12)])
print(b)
c=np.array([[1,2,3],[4,5,6]],dtype=complex)
print(c)
d=np.zeros((3,5))
print(d)
e=np.ones((2,3,4),dtype=np.int16)
print(e)
f=np.empty((3,4))
print(f)
g=np.linspace(0,100,12)
print(g)
#np.set_printoptions(threshold=np.nan)
print(np.arange(10000))
print(np.arange(10000).reshape(100,100))