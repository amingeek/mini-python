# import numpy as np
import random as rnd

tass = [1, 2 ,3 ,4 ,5 ,6]
seke = [0, 1]
list1 = []

for _ in range(5):
    for _ in range(10):
        list1.append(rnd.choice(tass) * rnd.choice(seke))
    for _ in range(100):
        list1.append(rnd.choice(tass) * rnd.choice(seke))
    for _ in range(100000):
        list1.append(rnd.choice(tass) * rnd.choice(seke))

avg = sum(list1) / len(list1)

print(avg)
