def bin1(n):
    s = ''
    
    if n:
        s = bin1(n // 2)
        return s + str(n % 2)
    else:
        return s
a = int(input("Dec to Bin\ninput an Dev:"))        
print(bin1(a))