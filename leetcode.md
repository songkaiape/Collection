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



## 5. Longest Palindromic Substring
>Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists >one unique longest palindromic substring.





 
