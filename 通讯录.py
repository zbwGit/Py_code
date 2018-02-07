def file_to_dict(filepath = "d:/contents.txt"):
    _dict = {}
    with open(filepath, 'a+') as dict_file:
        dict_file.seek(0, 0)
        for line in dict_file:
            (key, value) = line.strip().split(':')
            _dict[key] = value
    return _dict

def dict_to_file(_dict, filepath = "d:/contents.txt"):
    with open(filepath, 'w') as dict_file:
        for (key,value) in _dict.items():
            dict_file.write('%s:%s\n' % (key, value))

def new(name, number):
    content = {name:number}
    dict_txt = file_to_dict()
    dict_txt.update(content)
    dict_to_file(dict_txt)

def find(name):
    dict_txt = file_to_dict() 
    number = dict_txt.get(name)
    return number

def del_content(name):
    dict_txt = file_to_dict()
    if name in dict_txt.keys():
        dict_txt.pop(name)
        print("已删除: %s" % name)
        dict_to_file(dict_txt)
    else:
        print("未找到 %s " % name)

def show_all(filepath = "d:/contents.txt"):
    _dict = {}
    with open(filepath, 'a+') as dict_file:
        dict_file.seek(0, 0)
        for line in dict_file:
            (key, value) = line.strip().split(':')
            _dict[key] = value
    length = len(_dict)
    print("共有 %s 个联系人" % length)
    for key in _dict.keys():
        print("{}:{}".format(key, _dict[key]))

print('''
|---通讯录
|---1.查询联系人电话
|---2.新建联系人
|---3.删除已有联系人
|---4.查看所有联系人
|---5.退出
''')
while True:
    print("\n")
    a = int(input("请输入相应指令代码："))

    if a == 1:
        name = input("请输入联系人姓名：")
        num = find(name)
        print("%s：%s" % (name, num))

    if a == 2:
        name = input("请输入联系人姓名：")
        number = input("请输入电话：")
        new(name, number)
        print("创建成功")

    if a == 3:
        name = input("请输入联系人姓名：")
        del_content(name)

    if a == 4:
        show_all()

    if a == 5:
        print("感谢使用")
        break

