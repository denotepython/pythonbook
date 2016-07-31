# -*-coding: utf-8 -*-
class Solution(object):
    def minSubArrayLen(self, s, nums):
    	i = 0
    	j = 1
    	len1 = len(nums)
    	MIN = 100000000
    	while i < len1 - 1 or j < len1 - 1:
    		temp = 0
    		for count in range(j - i + 1):
    			temp += nums[i+count]
    		if temp < s:
    			j += 1
    		elif temp > s:
    			i += 1
    		elif temp == s:
    			if j - i + 1 < MIN:
    				MIN = j - i + 1
    	return MIN
    			
"""
:type s: int
:type nums: List[int]
:rtype: int
"""

a = Solution()
nums = [2,3,1,2,4,3]
s = 7
MIN = a.minSubArrayLen(s, nums)
print MIN