## 1.Two sum

>Given an array of integers, return indices of the two numbers such that they add up to a specific target.

>You may assume that each input would have exactly one solution.

mysolution:
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==temp:
                    return [i,j]
```
Best solution:
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i+1]
            else:
                buff_dict[target - nums[i]] = i+1
```

## 2.Add Two Numbers

>You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes >contain a single digit. Add the two numbers and return it as a linked list.

>Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
>Output: 7 -> 0 -> 8

solution:
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
    carry = 0
    res = n = ListNode(0)
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        carry, val = divmod(carry, 10)
        n.next = n = ListNode(val)
    return res.next
```
## 3.Longest Substring Without Repeating Characters

>Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without >repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.


```python
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
```
## 4.Median of Two Sorted Arrays

>There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run >time complexity should be O(log (m+n)).


求中位数需要根据数组长度是奇数还是偶数分别讨论，奇数长度时中位数为最中间的一个数，偶数长度时中位数为最中间的两个数的平均值，为了方便，可以实现一个比题目更一般化的函数，求A和B的第k小数的函数，那么中位数的问题很容易解决。

求一个有序数组的第k个数只需要O(1)的复杂度，现在有两个数组，显然花费额外空间以O(n)时间归并然后O(1)寻找不满足题目要求。

既然要求log时间复杂度，一般需要使用到二分思想。分别考虑A和B的第k/2个元素：
如果它们相等，则第k个数为其中的任意一个
如果A中的比较大，则B中前k/2个元素都不可能是第k个数了，因为这个数至少应该为A的第k/2个数，把B的前k/2去掉，然后重新寻找。
如果B中的比较大，则把A的前k/2个数去掉，重新寻找。

直到A和B中某个变为空时或者寻找第1个数时可以停止递归，直接找到结果。

注意，上面的k/2只是理想的简单情况，实际上A和B的长度可能不够k/2，或者k为奇数等，但这些不是主要问题，可以让A取第k/2个数字，然后A不够长，则取A的最后一个数字，然后B取剩下长度对应的那个数字，具体参考代码。

```python
def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   

def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2 , len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices 
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)
```
## 5. Longest Palindromic Substring
>Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists >one unique longest palindromic substring.



中心扩展法：
```python
def longestPalindrome(s):
    l=len(s)
    if l<=1:
        return s
    start=maxlen=0
    for i in range(l):
        low,high=i-1,i
        while low>=0 and high<l and s[low]==s[high]:
            low-=1
            high+=1
        if high-low-1>maxlen:
            maxlen=high-low-1
            start=low+1
        low,high=i-1,i+1
        while low >=0 and high<l and s[low]==s[high]:
            low-=1
            high+=1
        if high-low-1>maxlen:
            maxlen=high-low-1
            start=low+1
    return s[start:maxlen+start]
```

```python
class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring

    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
```

## 6. ZigZag Conversion
 
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 
> P   A   H   N
> A P L S I I G
> Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows: 
> string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
 
 ```python
 def convert(self, s, numRows):
    if numRows <= 1:
        return s

    lines = ["" for i in range(numRows)]
    index, step = 0, 1

    for i in s:
        lines[index] += i
        index += step
        if index == 0 or index == numRows - 1:
            step = -step

    return "".join(lines)
```
