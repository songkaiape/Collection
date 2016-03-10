
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
