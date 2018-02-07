import time
import sys
sys.setrecursionlimit(1000)
def jiecheng(x):
    if x == 1:
        return x
    else:
        return x * jiecheng(x - 1)

a = int(input())
start = time.clock()
print(jiecheng(a))
end = time.clock()
print("%f s" % (end - start))