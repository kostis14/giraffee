import time
import random

a = [random.choice(range(random.randint(1, 101))) for i in range(random.randint(50, 101))]
b = [random.choice(range(random.randint(1, 101))) for i in range(random.randint(50, 101))]
c = []
a.sort()
b.sort()
print(a)
print(b)
for k in range(len(a)):
    for j in range(len(b)):
        if a[k] == b[j]:
            if a[k] not in c:
                c.append(a[k])
print("Here's your list!")
time.sleep(0.33)
c.sort()
print(c)