•编写代码, 打印1-1亿之内的偶数


•写一个函数, 用正则表达式清除字符串中[]和其中的内容。
s = "[lol]你好，帮我把这些markup清掉，[smile]。谢谢！"


•请使用python, 对下面的函数进行处理,

def hello(name):
    print "hello, %s" % name


在函数被调用时打印耗时详情
<function name: hello>
<function call begin>
hello, tom
<function call end>
[timecosts: 3.81469726562e-06s]


•写一个函数, 将驼峰命名法字符串转成下划线命名字符串(需考虑各类编码中常见的命名)

e.g.  GetItem -> get_item
      getItem -> get_item
      doIT    -> do_IT


•有一个列表：[1, 2, 3, 4...n]，n=20；请编写代码打印如下规律的输出：
>1. [1*, 2, 3, 4, 5]
>2. [1, 2*, 3, 4, 5]
>3. [1, 2, 3*, 4, 5]
>4. [2, 3, 4*, 5, 6]
>5. [3, 4, 5*, 6, 7]
>6. [4, 5, 6*, 7, 8]
...

20 [16, 17, 18, 19, 20*]



•写一个程序模拟银行排队, 只有一个队伍, 一个用户进入时允许插队(进入队伍任意位置), 但要保证每次导致队伍变更, 队伍中受影响的人都收到通知

Customer A line up at position 11


Customer B: order changed to 12
Customer C: order changed to 13
Customer D: order changed to 14



•用户系统, 存在相互关注的动作, 当进入某个人的个人主页, 需要展示其粉丝数, 关注数, 粉丝列表以及关注列表. 请简要描述解决方案, 
包括db建模/数据层/业务层, 以及应对高并发/关注取关等情况的处理逻辑


•给定一些NxN的矩阵，对于任意的路线，定义其【和】为其线路上所有节点的数字的和，计算从左上角到右下角的路线和最小值。
每条路线只能从某一点到其周围（上下左右）的点，不可斜行。 例如，


4,6
2,8 的路线和最小值为 4-2-8 14

1,2,3
4,5,6
7,8,9 的路线和最小值为 1-2-3-6-9 21

1.求整数n的阶乘n!的末尾有多少个0？ （如：50!的末尾就有12个0）

2. 买啤酒问题：假设你的有n(n=10）元钱，一瓶啤酒的价格是2元，每3个空瓶可以换取一瓶啤酒，请问你最多可以喝到多少瓶啤酒？

练习题：有一百个人，分别从1一直到100。现在有人拿枪从第一个开始枪毙，每枪毙一个跳过一个，
一直到一轮完成。接着在活着的人里面再次枪毙第一个，间隔一个再枪毙一个，请问最后活着的是这一百个人里的第几个人？看谁写的简单。


```python
l=list(range(100))
while len(l)>1:
    for i in range(100):
        if i >=len(l):
            break
        l.pop(i)
    print(l)
print(l) 

l=range(1,101)
while len(l)!=1:
    l=l[1::2]
    print(l)
print(l[0])
```
约瑟夫环
约瑟夫环：约瑟夫环是一个数学的应用问题：已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。从编号为k的人开始报数，数到m的那个人出列；他的下一个人又从1开始报数，数到m的那个人又出列；依此规律重复下去，直到圆桌周围的人全部出列。

```python
def func(n,m):
    l=list(range(1,n+1))
    while len(l)>0:
        for i in range(m-1):
            l.append(l.pop(0))
        print(l.pop(0))
```
取巧解法
```python
def jeus(n,m):
    r=0
    for i in range(2,n+1):
        r=(r+m)%i
    return r+1
    
print(jeus(100,2))  
```
简单的闭包实现：
```python   
def new_counter(i):
    
    def c():
        c.num+=1 
        return c.num
    c.num=i
    return c 
def add(i):
    count=i
    def c():
        nonlocal count
        count+=1 
        return count
    return c 
c1 = add(10)
c2 = add(20)
print(c1(),c2(),c1(),c2())
```
# 经典排序算法序
```python
def bubble_sort(array):
    
    for i in range(len(array)):
        flag=1
        for j in range(1,len(array)-i):
            if array[j-1]>array[j]:
                array[j-1],array[j] = array[j], array[j-1]
                flag=0
        if flag:
            break
        print(array)
    return array

def select_sort(ary):
    for i in range(len(ary)):
        minx=i
        for j in range(i+1,len(ary)):
            if ary[j] < ary[minx]:
                minx=j
        ary[minx],ary[i] = ary[i],ary[minx]
        print(ary)
    return ary
def insert_sort(ary):
    for i in range(1,len(ary)):
        if ary[i]<ary[i-1]:
            temp=ary[i]
            index=i
            for j in range(i-1,-1,-1):
                if ary[j]>temp:
                    ary[j+1]=ary[j]
                    index=j
                else:
                    break
            ary[index]=temp
    return ary
def shell_sort(ary):
    n=len(ary)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=ary[i]
            j=i
            while(j>=gap and ary[j-gap] >temp):
                ary[j]=ary[j-gap]
                j=j-gap
            ary[j]=temp
        gap=gap//2
    return ary
    
def merge_sort(ary):
    if len(ary)<=1:
        return ary
    num=int(len(ary)/2)
    left=merge_sort(ary[:num])
    right=merge_sort(ary[num:])
    return merge(left,right)
def merge(left,right):
    l,r=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result+=left[l:]
    result+=right[r:]
    return result
def qsort(ary):
    if not ary:
        return []
    else:
        pivot=ary[0]
        less=[x for x in ary if x<pivot]
        more=[x for x in ary[1:] if x>=pivot]
        return qsort(less)+[pivot]+qsort(more)
print(qsort([1000,5,77,9,22,0,100,60]))
```
单例模式：
```
#new方法
class Singleton(object):
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance'):
            orig=super(Singleton,cls)
            cls._instance=orig.__new__(cls,*args,**kw)
        return cls._instance

#共享属性
class Borg(object):
    _state={}
    def __new__(cls,*args,**kw):
        ob=super(Borg,cls).__new__(cls,*args,**kw)
        ob.__dict__=cls._state
        return ob
        
#装饰器
class singleton(cls,*args,**kw):
    instances={}
    def getinstance():
        if cls not in instances:
            instances[cls]=cls(*args,**kw)
        return instances[cls]
    return getinstance
```
