def compare(path1, path2):
    file1 = open(path1)
    file2 = open(path2)
    list_1 = []
    list_2 = []
    for each_line in file1:
        list_1.append(each_line)

    for each_line in file2:
        list_2.append(each_line)
     #把每行存为列表
    if list_1 != list_2:
        if len(list_1) < len(list_2):
            x = len(list_1)
        else:
            x = len(list_2)
         #取两者最小的以便每行比较
        for n in range(x):
            if list_1[n] != list_2[n]:
                _list_1 = list(list_1[n])
                _list_2 = list(list_2[n])
                 #每行单独作为列表
                count1 = 0
                
                for each_word in _list_1: #逐字比较
                    if each_word == _list_2[count1]:
                        count1 += 1
                    else:
                        count = count1
                        break
                
                print("different line: %d, different word: %d" % (n + 1, count + 1))
    else:
        print("They are the same.")
    file1.close()
    file2.close()

path1 = input("address1: ")
path2 = input("adsress2: ")
compare(path1, path2)

 #问题：若两个文件行数不同，多余行数的比较无法显示