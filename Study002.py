import random
L = [ i for i in range(10)]
print(list(L))
random.shuffle(L)
L1 = tuple(L)
print(tuple(L1))
print(sorted(L1))