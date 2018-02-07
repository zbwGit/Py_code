def gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        temp = x % y
        x = y
        y = temp
    return x
a, b = map(int,input("求两数最大公约数\n请输入两数(逗号隔开）：").split(','))
c = gcd(a, b)
print("%d, %d的最大公约数为：%d" % (a, b, c))
input()