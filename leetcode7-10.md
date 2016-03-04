## 7. Reverse Integer
> Reverse digits of an integer.
> Example1: x = 123, return 321
> Example2: x = -123, return -321 

提交的时候报错，原因是Python会自动把INT转换为long所以python整数是没有上限的。超过int上限需要返回0
加上2**31-1才通过
```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minus=False
        if x<0:
            minus=True
            x=-x
        num=0
        while x:
            num=num*10+x%10
            x=x//10
        if num>2**31-1:
            return 0
        else:
            return -num if minus else num
 ```
 
