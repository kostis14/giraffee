import random
import numpy as np
number = random.randint(1,101)
print(number)
for i in range(0,number+1):

    if i != 0:
        if number % i == 0:
            print(i)