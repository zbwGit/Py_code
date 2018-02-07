import time
import os
def f(n):
    if (n == 1) or (n == 2):
        return 1
    elif n <= 0:
        print("wrong")
        return -1
    else:
        s = f(n - 1) + f(n - 2)
        return s
a = int(input())
start = time.clock()
b = f(a)
end = time.clock()
if b != -1:
   print(b)
   print("%f s" % (end - start))
   os.system("pause")
