import time
def f(n):
    a1 = 1
    a2 = 1
    a3 = 1
    #变量初始化，方便输出n = 1, 2时情况

    if n <= 0:
        print("wrong")
        return -1
    while (n-2) > 0:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        n -= 1
    return a3
a = int(input())
start = time.clock()
b = f(a)
end = time.clock()
if b != -1:
   print(b)
   print("%f s" % (end - start))