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
 
 ## 10.Implement regular expression matching with support for '.' and '*'.

  '.' Matches any single character.
  '*' Matches zero or more of the preceding element.

  The matching should cover the entire input string (not partial).

  The function prototype should be:
  bool isMatch(const char *s, const char *p)
```
  Some examples:
  isMatch("aa","a") → false
  isMatch("aa","aa") → true
  isMatch("aaa","aa") → false
  isMatch("aa", "a*") → true
  isMatch("aa", ".*") → true
  isMatch("ab", ".*") → true
  isMatch("aab", "c*a*b") → true
```
解：
```python
class Solution(object):
    def isMatch(self, s, p, memo={("",""):True}):
        if not p and s:      return False
        if not s and p:      return set(p[1::2]) == {"*"} and not (len(p) % 2)
        if (s,p) in memo:    return memo[s,p]
        
        char, exp, prev = s[-1], p[-1], 0 if len(p) < 2 else p[-2]
        memo[s,p] =\
               (exp == '*' and ((prev in {char, '.'} and self.isMatch(s[:-1], p, memo)) or self.isMatch(s, p[:-2], memo)))\
               or\
               (exp in {char, '.'} and self.isMatch(s[:-1], p[:-1], memo))
        print(memo)
        return memo[s,p]
```
