import random

i = 0
j = 0

n = int(input('input times: '))
while i < n:
    x = random.random()
    y = random.random()
    i += 1
    if (x*x + y*y) < 1:
        j += 1
s = 4 * (j / i)
print('pai=',end=' ')
print(s)
    