import random
import time

i = 0
j = 0

n = int(input('input times: '))
start = time.clock()

while i < n:
    x = random.random()
    y = random.random()
    i += 1
    if (x*x + y*y) < 1:
        j += 1
s = 4 * (j / i)
print('pai=',end=' ')
print(s)
stop = time.clock() 
print('Time used: %f s' % (stop - start))
input()