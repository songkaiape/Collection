##1.Two sum

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
                if nums[j]>temp:
                    continue
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
