# print absolute value of an integer:
# a = 100
# if a >= 0:
    # print a
# else:
    # print -a
	
#格式化:
# print 'hello,%s,you have to get %d %s ,and money is $%.2f' % ('mjq',20,'apple',234.5)

#list
# boys =['mich','吉吉','mjq']
# print 'this is ',len(boys),'boys\n' ,boys
# print 'add a boy named hj and delete a boy '
# boys.insert(1,'hj')
#boys.append('jj')
# boys.pop(2);
# print boys

#tuple
# classmates =('mjq','hj','tracy')
# print classmates[2]
# t=('a','b',['addr','phone'])
# print 'origin is ',t;
# t[2][1]='jodan'
# print 'now is',t

#if   
#从raw_input()读取的内容永远以字符串的形式返回，把字符串和整数比较就不会得到期待的结果，必须先用int()把字符串转换为我们想要的整型
# age = int(raw_input())
# if age >= 60:
    # print 'yor age is', age
    # print 'old'
# elif age > 18:
	# print 'you are a strong man'
	# print 'age is',age
# else:
	# print 'you are a young boy'

#循环
# names = ['jordan', 'marry', 'Tracy']
# for name in names:
    # print name

# sum=0
# for x in range(100):
	# sum+=x
# print sum

#内置字典dict  php中array, .net中有Dictionary，  java中有map
# 1.查找和插入的速度极快，不会随着key的增加而增加；
# 2.需要占用大量的内存，内存浪费多。
# list：
# 1.查找和插入的时间随着元素的增加而增加；
# 2.占用空间小，浪费内存很少。

# d={'name':'mjq','addr':'bj','age':100}
# d['addr']='sh'#modify
# print d['name'],' live in ',d['addr'],' and ',d['age'],' year old'

# if d.get('email',-1)==-1:
	# print 'not exits key email'

	
#set  set和dict的唯一区别仅在于没有存储对应的value
# s = set([1, 2, 2, 'mjq', 'mjq'])
# print 's=',s
# s2=set(['mjq',3])
# print 's2=',s2
# print 's & s2 =',s&s2
# print 's | s2 =',s|s2

#内置函数
# print abs(23.32)
# print cmp(2,4)
# print int(23.32)

#定义函数
# import math
# def getCircle(r):
	# area = float(math.pi*r*r)
	# return area
# print 'circle area is ',getCircle(2)

#默认参数,写法和其他语言类似
# def power(x,n=2):
	# s=1
	# while n>0:
		# s=s*x;
		# n=n-1
	# return s
# print power(3)
# print power(3,5)

#函数的 可变参数
# def calc(*numbers):
    # sum = 0
    # for n in numbers:
        # sum = sum + n * n
    # return sum
# print '11*11+2*2+5*5=',calc(11,2,5)

#关键字参数
# def person(name, age, **kw):
    # print 'name:', name, 'age:', age, 'other:', kw
# kw = {'city': 'Beijing', 'job': 'Engineer'}
# print person('mjq',22,**kw)

#递归  n! = 1 x 2 x 3 x ... x n
# def fac(n):
	# if n==1:
		# return 1
	# return n*fac(n-1)

# print '10 factorial =',fac(10)

###切片, 取指定索引范围的操作,使用循环太繁琐，可以使用切片
# boys =['mich','joy','mjq','lilei']
#从索引1开始取，直到索引3为止，但不包括索引3
# print boys[1:3]

# L = range(100)
# print L[:10]
# print L[::10]

###迭代 for ...in   其他语言中几乎都有，java: for(string s:lists)  php: for($arrays as $array) .net foreach(string name in names)
# names = ['jordan', 'marry', 'Tracy']
# for name in names:
    # print name

# for x, y in [(1, 1), (2, 4), (3, 9)]:
	# print x, y

###列表生成式 list  #列表生成式也可以使用两个变量来生成list ，可以使用函数处理结果
#生成 1*1，2*2，..n*n的list。   
# l=[]
# for x in range(1,11):
	# l.append(x*x)
# print 'use for:',l
# print 'List Comprehensions:',[x*x for x in range(1,11)]

# d={'a':1,'b':2,'c':3}
# for k,v in d.iteritems():
	# print k,'=',v
# print [k+'='+str(v) for k,v in d.iteritems()]
	
import os #list all the file in current directory
print [d for d in os.listdir('.')]

#isinstance函数可以判断一个变量是不是字符串
# L = ['good', 'man', 18, 'Apple', None]
# print [s.lower() for s in L if isinstance(s,str)]


####Python中，循环的过程中不断推算出后续的元素，一边循环一边计算的机制，称为生成器..可以不用创造出完成的list,节省存储空间
####只要把一个列表生成式的[]改成()，就创建了一个generator  ,还可以使用yield关键字 
##斐波拉契数列1, 1, 2, 3, 5, 8, 13, 21, 34... 
# def fib(max):
	# n,a,b=0,0,1
	# while n<max:
		# yield b
		# a,b=b,a+b
		# n=n+1
# for d in fib(10):
	# print d

###高阶函数 ,php有类似实现，  
###.net中的委托可实现相同的功能，Func<int,int,Func<int,int>,int> sum = delegate(int x,int y,Func<int,int> f){return f(x)+f(y);)};
###稍简单的写法Func<int,int,Func<int,int>,int> sum = (x,y,f)=>f(x)+f(y)
# def add(x, y, f):
    # return f(x) + f(y)
# print add(-2,9,abs)

### map /reduce函数reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# def fn(x,y):
	# return x*10+y
# def char2num(s):
	# return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# print reduce(fn,map(char2num,'26578'))

#lambda表达式实现,和上面函数实现一样的功能.
# def char2num(s):
	# return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# def str2int(s):
	 # return reduce(lambda x,y:x*10+y,map(char2num,s))
# print str2int('23490')

# def prod(L):#python提供sum可实现list累加。prod实现list 累乘积
	# return reduce(lambda x,y:x*y,L)
# print prod([1, 3,5,9,22])

# boys =['mich','joy','mJq','liLEi']#转换函数，将list中字符串第一个字母大写，其他字母小写
# def strFormat(s):
	# return s[:1].upper()+s[1:len(s)].lower()
# print map(strFormat,boys)

##filter 过滤序列
# def not_empty(s):
    # return s and s.strip()
# print filter(not_empty, ['A', '', 'B', None, 'C', '  '])

# def not_prime(n):##过滤所有素数
	# c=2
	# while(c<=(n/2)):
		# if n%c==0:
			# return True
		# c=c+1
	# return False
# print range(1,101)
# print filter(not_prime,range(1,101))

###sorted 排序函数
# def cmp_ignore_case(s1, s2):
	# u1 = s1.upper()
	# u2 = s2.upper()
	# if u1 < u2:
		# return -1
	# if u1 > u2:
		# return 1
	# return 0
# print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)


#序列化 cPickle  pickle
# try:
    # import cPickle as pickle
# except ImportError:
    # import pickle
# d = dict(name='Mjq', addr='beijing', score=98)
# f = open("dump.txt",'wb')
# pickle.dump(d,f)
# f.close()

# r = open('dump.txt','rb')
# content = pickle.load(r)
# r.close()
# print content
 
 
##json
# import json

# class Student(object):
    # def __init__(self, name, addr, score):
        # self.name = name
        # self.addr = addr
        # self.score = score
# def student2dict(std):
    # return {
        # 'name': std.name,
        # 'addr': std.addr,
        # 'score': std.score
    # }
# def dict2student(d):
    # return Student(d['name'], d['addr'], d['score'])

# s = Student('Bob', 'beijing', 88)
# jsonstr = json.dumps(s,default=student2dict)
# obj=json.loads(jsonstr,object_hook=dict2student)
# print 'object be trans to json  ',jsonstr

# print 'json trans to a object: ',obj


###文件读写
# import codecs
# with open('readAndwrite.txt', 'w') as f:
    # f.write("hello,m!!")
# with codecs.open('readAndwrite.txt','r','gbk') as rf:
	# print rf.read()

# import os
####print 'os: ',os.name,'\npath: ',os.getenv('path'),'\nabsulute route: ',os.path.abspath('.')
####[x for x in os.listdir('.') if os.path.isdir(x)]
###搜索某个目录及子目录下包含关键字的文件名称(子目录的子目录未实现)
# def search(dir,s):
	# L=[]
	# if dir!='.':
		# L = ([os.path.join(dir,f) for f in os.listdir(dir) if os.path.isfile(f) and f.find(s)>0])
	# else:
		# L=([f for f in os.listdir(dir) if os.path.isfile(f) and f.find(s)>0])
	# p = [x for x in os.listdir(dir) if os.path.isdir(x)]
	# for dirt in p:
		# L.append(search(os.path.join(dir,dirt),s))
	# return L
# l = search('.','test')
# print l
#from Student import Student
#s = Student('Michael')
#print s()


 