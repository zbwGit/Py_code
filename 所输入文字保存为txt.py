file = open("writen.txt", 'a+')
print("input sentence(:wq to exit): ")

while True:
    writen = input()
    if writen != ':wq':
        file.write("%s\n" % writen)
    else:
        break

file.close()
