def file_compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0 #统计行数
    differ = [] #统计不一样的数量

    for line1 in f1:
        line2 = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ

file1 = input("input path_1: ")
file2 = input("input path_2: ")

differ = file_compare(file1, file2)

if len(differ) == 0:
    print("They are the same.")
else:
    print("%d differs: " % len(differ))
    for each in differ:
        print("differ in line %d" % each)