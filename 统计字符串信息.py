#分别统计传入字符串参数（可能不止一个）的英文字母，空格，数字和其他字符的个数
def check(*p):
    length = len(p)
    for n in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in p[n]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                others += 1
        print("in %d parameter, have %d letters, %d spaces, %d digits, %d others" % (n + 1, letters, space, digit, others))

check("i love you", "i love china")