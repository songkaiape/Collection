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
## 8. String to Integer (atoi)
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Solution:
```python
class Solution(object):
    def myAtoi(self, str):
        num, sign, cur = 0, 1, 0
        while cur < len(str):
            if str[cur] == ' ':
                cur += 1
            elif str[cur] == '-':
                sign, cur = -1, cur+1
                break
            elif str[cur] == '+':
                cur += 1
                break
            elif ord(str[cur]) > 57 or ord(str[cur]) < 48:
                cur += len(str)
            else:
                break
            
        while cur < len(str) and ord(str[cur]) >= 48 and ord(str[cur]) <= 57:
            if num > 214748364 or (num == 214748364 and ord(str[cur]) - 48 > 7):
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648
            num, cur = 10 * num + ord(str[cur]) - 48, cur+1
        
        return num * sign
```
solution2:
```python
def myAtoi(self, s):
    try:
        s = s.lstrip() + '$' # remove leading spaces and append an end mark
        for i, ch in enumerate(s):
            if not (ch in '+-' or '0' <= ch <= '9'):
                result = int(s[:i])
                return -2 ** 31 if result < -2 ** 31 else 2 ** 31 - 1 if result > 2 ** 31 - 1 else result
    except:
        return 0
```
 
solution3:
```python
class Solution:
# @return an integer
def atoi(self, str):
    str = str.strip()
    str = re.findall('(^[\+\-0]*\d+)\D*', str)

    try:
        result = int(''.join(str))
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if result > MAX_INT > 0:
            return MAX_INT
        elif result < MIN_INT < 0:
            return MIN_INT
        else:
            return result
    except:
        return 0
```

## 9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
```python

class Solution:
    def isPalindrome(x):
        if x<0 or (x!=0 and x%10==0):
            return False
        sum=0
        while x>sum:
            sum=sum*10+x%10
            x=x/10
        return (x==sum) or (x==sum/10)
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
