#!/usr/bin/python3
# coding=utf-8
# 数据处理模块
import time,re

filepath = ''

def set_file_path(path = ''):
    global filepath
    filepath = path
    print("用户数据文件路径已经改变")

def open_file(filepath = '',ms = 'a+'):
    def p(func):
        def q(*args, **kwargs):
            if filepath != '':
                try:
                    f = open(filepath, ms, encoding = 'utf-8')   # r 只读打开 a末尾加入 +可读写
                    f.seek(0, 0)
                    print(time.strftime("%H:%M:%S", time.localtime()) + "路径文件用户数据读取成功，共读取到%d条数据！" % len(list(f)))
                    f.seek(0,0)
                    func(f, *args, **kwargs)
                    f.close()

                except (EOFError, FileNotFoundError) :
                    print(time.strftime("%H:%M:%S", time.localtime()) + "路径文件用户数据读取失败！可能是文件路径异常！")
            else:
                try:
                    f = open('./user_data.txt', ms, encoding = 'utf-8')  # r 只读打开 a末尾加入 +可读写
                    f.seek(0, 0)
                    print(time.strftime("%H:%M:%S", time.localtime()) + "用户数据读取成功，共读取到%d条数据！" % len(list(f)))
                    f.seek(0, 0)
                    func(f, *args, **kwargs)
                    f.close()
                except (EOFError, FileNotFoundError) :
                    print(time.strftime("%H:%M:%S", time.localtime()) + "用户数据读取失败！")
        return q
    return p

@open_file(filepath)
def search(f,k):
    user_data = re.search('.+' + k + '.+', f.read(), re.M)
    if user_data:
        print(user_data.group())
    else:
        print("查无此人")

@open_file(filepath)
def add_user(f,userdata):
    f.write('%s %s %s %s %s %s %s %s %s %s %s %s end\n' % (str(len(list(f))), userdata[0], userdata[1], userdata[2], userdata[3], userdata[4], userdata[5], userdata[6], userdata[7], userdata[8], userdata[9], userdata[10]))
    f.seek(0,0)
    print("用户添加成功,目前共有%s条数据" % str(len(list(f))))

@open_file(filepath)
def del_user(f,k):
    user_data = re.search('.+' + k + '.+', f.read(), re.M)
    if user_data :
        del_user_data = user_data.group().split(' ')
        f.seek(0,0)
        old_data = f.readlines()
        del old_data[int(del_user_data[0])]
        new_data = ''
        j = 0 #新计数
        for i in old_data:
            u = i.split(' ')
            u[0] = j
            i = ''
            for x in u:
                i = i + str(x)
                if x != 'end' and x != 'end\n':
                    i = i + ' '
            new_data = new_data + str(i)
            j = j + 1
        f.truncate(0) #清空文件
        f.write(new_data)
        f.seek(0, 0)
        print('原编号%s 用户%s 姓名%s 删除完毕！' % (del_user_data[0],del_user_data[1],del_user_data[3]))
        print("用户删除成功,目前共有%s条数据" % str(len(list(f))))
    else :
        print("删除查无此人")

@open_file(filepath)
def update(f,u,k,v):
    pass

if __name__ == '__main__':
    #search('山东')
    userdata = ['1701070235','password','李xx','必须是详细准确的系名称','178xxxxxxxx','山东省菏泽市曹县','1','3','xx区','耕文路419号','154xxxxxxx@qq.com']
   ''' 
   i = 0
    while i <= 999:
        add_user(userdata)
        i = i + 1
    '''
    #del_user('1701070235')
else:
    print("用户数据管理模块导入成功")