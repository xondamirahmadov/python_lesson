import numpy as np
# a = np.array([1, 3, 5, 4, 2])
# print(a)
#
# a = np.array([1, 3, 5, 4, 2], dtype='float32')
# print(a)
#
# a = np.array([range(i, i + 3) for i in [2, 4, 6]])
# print(a)

# a = np.zeros(10, dtype=int)
# print(a)

# a = np.ones((3, 5), dtype=int)
# print(a)

# a = np.full((3, 5), 3.20)
# print(a)

# a = np.arange(0, 20, 2)
# print(a)

# a = np.linspace(0, 1, 5)
# print(a)

# a = np.random.random((3, 4))
# print(a)

# a = np.random.randint(0, 10, (3, 3))
# print(a)

x = np.arange(4)
print('x=', x) # x= [0 1 2 3]
print('x + 5=', x + 5) # x + 5= [5 6 7 8]
print('x ‐ 5=', x - 5) # x ‐ 5= [-5 -4 -3 -2]
print('x * 2=', x * 2) # x * 2= [0 2 4 6]
print('x / 2=', x / 2) # x / 2= [0. 0.5 1. 1.5]
print('x // 2 =', x // 2) # x // 2 = [0 0 1 1] 
print('‐x=', -x) #‐x= [ 0 -1 -2 -3]
print('x ** 2 =', x ** 2) #x ** 2 = [0 1 4 9]
print('x % 2=', x % 2) #x % 2= [0 1 0 1]
print(-(0.5 * x + 1) ** 2) # [-1. -2.25 -4. -6.25]