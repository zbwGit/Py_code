 #输入13:21打印13到21行，输入:21打印前21行，输入21:打印第21行到文件尾部，输入:打印全部
def read_file(path, target):
    if target.strip() == ':':
        prompt = 'All the paper:'
        file_all = open(path)
        file_all_list = list(file_all)
        for each_line in file_all_list:
            print(each_line)
    else:
        (start, end) = target.split(":")

        if start == '':
            prompt = 'From start to line %s:' % end
        elif end == '':
            prompt = 'From line %s to the end:' % start
        else:
            prompt = 'From line %s to line %s:' % (start, end)
        
        print('\n%s\n' % prompt)

        file = open(path)
        if end == '':
            for i in range(int(start)):
                file.readline()
            print(file.readline())  #此处有误


path = input("input the file path: ")
target = input("what do you want to print: ")
read_file(path, target)