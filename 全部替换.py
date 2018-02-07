import os
def word_replace(path, word, new_word):
    file = open(path)
    
    count = 0
    rep_lines = []
    file_list = list(file)

    for eachline in file_list:
        if word in eachline:
            count += eachline.count(word)
            eachline = eachline.replace(word, new_word) #更新需要替换的一行
        rep_lines.append(eachline) #使每一行都写入列表
    
    print("%s文件中，共有%d个%s，是否需要全部替换为%s 【yes/no】： " % (path, count, word, new_word))
    decide = input()

    if decide in ['yes', 'Yes', 'y']:
        file = open(path, 'w')
        file.writelines(rep_lines) #更新的列表写入文件
    
    file.close()
    
path = input("please input file path: ")
word = input("Which word to replace: ")
new_word = input("input a new word: ")
word_replace(path, word, new_word)
os.system("pause")
