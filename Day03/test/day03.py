#/usr/bin/env/ python
# _*_ coding:utf-8 _*_
'''ceshishuru
'''



#name = 'alex'
#action = 'doubi'

#print(name,action)


#from file import demo

#.foo()

#print(__name__)

#if __name__ == '__main__':
#    pass

#print(__file__)
#print(__doc__)

'''
def foo(name):
    print(name,'去砍柴')
    
foo('liyang')
foo('yuanli')
'''
'''
def login(username):
    if username == 'alex':
        return 'deng lu cheng gong'
        
    else:
        return 'denglushibai'
    
        
def detail(username):
    print('ssssssss')
    
    
if __name__ == '__main__':
    user = raw_input('请输入用户名：')
    result = login(user)#检查用户合法
    if result == 'deng lu cheng gong':
        detail(user)#显示详细
    else:
        print('没有明细')
'''

'''
def foo(name,action='打车',where='北京'):
    print(name,'去',action,where)
    
foo('liyang','砍柴')
foo('yuanli','吃饭')
foo('Heloo','上海')
'''


'''
#可变参数 *arg,**kargs
#函数只有一个参数，调用函数时候参数不固定，加一个*,函数会将传入
#的参数自动汇聚成列表传进函数，加两个*,函数会将参数汇聚成字典

def show(**kargs):
    for item in kargs.items():
        print(item)
user_dict = {'k1':123,"k2":345}
show(**user_dict)#传入的时候要必须带**，传参数只需要key:value格式
show(name='alex',age=18)
'''

'''
def show(*arg):
    for item in arg:
        print(item)
#show('liyang','zhuag','sss')
a = ['liyang','zhuag','sss']
b = ('liyang','zhuag','sss')
show(*a)
show(*b)
'''

#yield
'''
print(range(10))
for item in range(10):
    print(item)
'''
'''
def foo():
    yield 1
    yield 2
    yield 3
    yield 3
    yield 3
    yield 3
re = foo()
#print(re)
for item in re:
    print(item)
'''
'''
#yield 返回的为生成器，迭代时候才产生数值

def AlexReadlines():
    seek = 0
    while True:
        with open('D:/jiangjie.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return

print(AlexReadlines())
for item in AlexReadlines():
    print(item)
'''
'''
def AlexReadlines():
    seek = 0
    while True:
        with open('D:/jiangjie.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                return data
            else:
                return

print(AlexReadlines())
'''


#三元运算
'''
temp = None
if 1>3:
    temp = 'gt'
else:
    temp = 'lt'
print(temp)
    
result = 'gt' if 1>3 else 'lt'
print(result)
'''

'''
#lambda表达式
temp = lambda x,y:x+y
print(temp(4,10))
'''
'''
a = []
a1 = list()
print(dir())
print(vars())
print(type(a1))
'''

'''
from file import demo
from file import demo
#demo.bar()
reload (demo)
'''

'''
#dir()以列表内字符串形势列出内置函数
#vars()以字典形势列出key和value
a = 13
b = 13
print(id(a))
print(id(b))
#开发过程中分页显示
print(divmod(9, 3))
print(divmod(9, 3)[1])
print(max(11,12))
print(sum([11,12]))#sum参数必须是列表
print(pow(2,10)) #指数
'''
'''
print(len('zhongguo'))
print(len('中国'))
print(all([1,2,3,4]))#all输入可迭代东西，遍历整个整个都为真，返回True.
print(all([1,0,0,0 ]))
print(all([0,0,0,0 ]))
print(hex(2))
print(bin(2))
print(oct(2))

shoping = ['手表','汽车','轮子']
for item in shoping:
    print(item)
#enumerate 给列表加序列,%s占位符，
for item in enumerate(shoping,1):
    print(item[0],item[1])
#{}占位符，然后用format()函数传入值    
s = 'i am {0},{1}'
print(s.format('liqinglong', 25))
'''

'''
def foo(arg):
    return arg + 100
li = [11,22,33]

for item in li:
    item = foo(item)
    print(item)

a = map(foo,li)
print(a)
for item in a:
        print(item)

temp = map(lambda x:x+100,li)
print(temp)
for item in temp:
        print(item)
'''

'''
li = [11,22,33]
def foo(arg):
    if arg < 22:
        return True
    else:
        return False
temp = filter(foo,li)
for item in temp:
        print(item)

#reduce 累加，必须要传入两个值
li = [11,22,33]
print(reduce(lambda x,y:x+y,li))

#zip 参数为 列表，返回一个zip object 拼接列表
a = [1,2,3,4,5]
b = [2,3,4,5,]
c = [3,4,5,6,7]
temp = zip(a,b,c)
for item in temp:
        print(item)
'''
'''
a = '8*8'
#a = a.split('*')
#print(a)
#sum = int(a[0])*int(a[1])
#print(sum)

print(eval(a))    
'''

#通过字符串模式导入模块

'''
import sqlserverhelper
print(sqlserverhelper.count())

import mysqlhelper
print(mysqlhelper.count())

temp = 'mysqlhelper'
model = __import__(temp)
model.count()
'''
'''
#以字符串形式执行函数
temp = 'mysqlhelper'
func = 'count'
model = __import__(temp)
function = getattr(model, func)#在model模块找func函数
print(function())
'''


#import random
#print(random.random())
#print(random.randint(1,5))
#print(random.randrange(1,3))
#temp = chr(random.randint(65,90))
#print(temp)

'''
code = []
for i in range(6):
    if i == randint(1,5):
        code.append(str(random.randint(1,5)))
        #print(random.randint(1,5))
    else:
        temp = chr(randint(65,90))
        #print(temp)
        code.append(temp)
#join将字符串链接成字符
''.join(code)
print(''.join(code))
'''

#逐个相加会每次开辟空间，用join会一次开辟
'''
import random
checkcode = ''
for i in range(5):
    current = random.randint(0,5)
    if current != i :
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print(checkcode)
'''

#md5加密

'''
hash = hashlib.md5()
#python 3以上必须要将字符串encode
hash.update('admin'.encode(encoding='utf_8', errors='strict'))
print(hash.hexdigest())
print(hash.digest())
'''

'''
import sys
import hashlib
def md5encode(arg):
    hash = hashlib.md5()
    hash.update(arg.encode(encoding='utf_8', errors='strict'))
    return hash.hexdigest()
    #print(hash.digest())


def register():
    username = input('please input ur name')
    username = md5encode(username)
    f = open('D:\\name.txt','r+')
    f.write(username)
    f.close()
    sys.exit()
    
def login():
    username = input('please input ur name:')
    tryname = md5encode(username)
    f = open('D:\\name.txt','r')
    for line in f.readlines():
        if tryname in line:
            print('Welcom')
        else:
            print(error)
    f.close()

login()

'''


'''
#序列化和json
import pickle
data1 = ['alex',11,22,'ok']

p_str = pickle.dumps(data)
p_str1 = pickle.dumps(data1)
print(type(p_str))
print(p_str)
print(p_str1)
result = pickle._loads(p_str)
result1 = pickle._loads(p_str1)
print(result)
print(result1)

p_str = pickle.dump(data,open('D:/temp.txt','wb'))
#fb = open('D:/temp.pk','rb')
result = pickle.load(open('D:/temp.txt','rb'))
print(result)


import json
name_dic = {'name':'linqinglong','age':18}
j_str = json.dumps(name_dic)
print(j_str)
print(json.loads(j_str ))

'''

'''
1:  用\d可以匹配一个数字，\w可以匹配一个字母或数字
2:  用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：
3:我们来从左到右解读一下：
 
\d{3}表示匹配3个数字，例如'010'；
 
\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
 
\d{3,8}表示3-8个数字，例如'1234567'。
 
综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码
如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。
但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。
4: 进阶
进阶
 
要做更精确地匹配，可以用[]表示范围，比如：
 
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
 
[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
 
[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
 
[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
 
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
 
^表示行的开头，^\d表示必须以数字开头。
 
$表示行的结束，\d$表示必须以数字结束。
 
你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
'''

'''
import re
#match从开始找，找不到结束
result1 = re.match('\d+','adfdga123dfdg')
if result1:
    result1 = result1.group()
    print(result1)
else:
    print(None)
#search找到为止
result2 = re.search('\d+','222adfdga123dfdg')
result2 = result2.group()
print(result2)
#findall 寻找所有，返回列表
result3 = re.findall('\d{1,2}','adfdga123dfdg222sfgsg3333')
print(result3)
 
 
#match(先compile,后match)
#和findall（先compile，后findall） 结果一样，先编译，后寻找，比findall节省效率
#com = re.compile('\d+')
com = re.compile('\d+').findall('adfdga123dfdg222sfgsg3333')
print(type(com))
print(com)
 
#groups跟正则表达式分组有关系
result2 = re.search('(\d+)\w*(\d+)','222adfdga123dfdg')
result2 = result2.group()
print(result2)
'''
'''
import re
ip = '12.34.43.dasg.sgsg.ddasdg..sg...192.168.32.43ddad_as'
 
ip_r = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip)
print(ip_r)
 
ip_r1 = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip)
print(ip_r)
 
#（?:表示重复）{3}：表示重复3次
ip_r2 = re.findall('(?:\d{1,3}\.){3}\d{1,3}',ip)
print(ip_r2)
'''


'''
# Time 三种表示方式：1、时间戳 1970年之后的秒2、元祖包含了：年、日、星期等3、格式化的字符串
#时间戳
import time
print(time.time())
print(time.gmtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
'''

#sys模块
'''
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.maxunicode     最大的Unicode值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
print val
'''

#OS模块
'''
os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
os.curdir  返回当前目录: ('.')
os.pardir  获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')    可生成多层递归目录
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  删除一个文件
os.rename("oldname","newname")  重命名文件/目录
os.stat('path/filename')  获取文件/目录信息
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    输出用于分割文件路径的字符串
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  运行shell命令，直接显示
os.environ  获取系统环境变量
os.path.abspath(path)  返回path规范化的绝对路径
os.path.split(path)  将path分割成目录和文件名二元组返回
os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
 
'''


