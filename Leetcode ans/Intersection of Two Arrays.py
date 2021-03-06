# -*- coding:utf-8 -*-
class Solution(object):
    def intersection(self, nums1, nums2):
    	a = sorted(nums1)
    	b = sorted(nums2)
    	len1 = len(nums1)
    	len2 = len(nums2)
    	i = 0
    	j = 0
    	c = set() #不想要重复元素就用set集合，自动去重
    	while i < len1 and j < len2:
    		if a[i] == b[j]:
    			c.add(a[i])
    			i += 1
    			j += 1
    		elif a[i] < b[j]:
    			i += 1
    		elif a[i] > b[j]:	
    			j += 1
    	d = list(c)
    	return d
"""
:type nums1: List[int]
:type nums2: List[int]
:rtype: List[int]
"""
temp = Solution()
nums1 = [1,2,3,5,6,3,7,4,6,9]
nums2 = [3,6]
ans = temp.intersection(nums1, nums2)
print ans
