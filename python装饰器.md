
```python
def counter(func):
    
    def wrapper(*args,**kw):
        wrapper.count=wrapper.count+1
        res = func(*args,**kw)
        print("%s has been used: %sx" % (func.__name__,wrapper.count))
        return res
    wrapper.count=0
    return wrapper


def log(text):
    if isinstance(text, (str, int, float)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('start %s %s():' % (text, func.__name__))
                result = func(*args, **kw)
                print('end %s %s():' % (text, func.__name__))
                return result
            return wrapper
        return decorator
    else:
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('start call %s():' % func.__name__)
            result = func(*args, **kw)
            print('end call %s():' % func.__name__)
            return result
        return wrapper
```

Python 定制类：
```python
>  __str__
>  __repr__
>  __getitem__
>  __iter__
>  __next__ 
>  __getattr__ 动态获取属性
> __call__ 
 slice 切片 start stop
 ```
```python
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a 
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a 
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            l=[]
            for x in range(stop):
                if x>=start:
                    l.append(a)
                a,b=b,a+b
                return l 
for i in Fib():
    print(i)
f=Fib()
print('this is',f[100])
```
```python
class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
    _repr__=__str__
    def __call__(self,path):
        return Chain('%s/%s' % (self,_path,path))
Chain().status.usre.timeline.list
Chain().users('michael').repo.list
