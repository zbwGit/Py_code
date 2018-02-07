def hanoi(n, x, y, z):
    '从x借助y移动到z'
    if n == 1:
        print(x, ' -> ', z)
    else:
        hanoi(n - 1,x, z, y)#从x借助z移动到y
        print(x, ' -> ', z)
        hanoi(n - 1, y, x, z)#从y借助x移动到z
a = int(input('输入汉诺塔层数：'))
hanoi(a, 'X', 'Y', 'Z')
