# -*- coding:utf-8 -*-
class Solution(object):
    def intersect(self, nums1, nums2):
    	a = sorted(nums1)
    	b = sorted(nums2)
    	len1 = len(nums1)
    	len2 = len(nums2)
    	i = 0
    	j = 0
    	c = list() 
    	while i < len1 and j < len2:
    		if a[i] == b[j]:
    			c.append(a[i])
    			i += 1
    			j += 1
    		elif a[i] < b[j]:
    			i += 1
    		elif a[i] > b[j]:	
    			j += 1
    	return c
"""
:type nums1: List[int]
:type nums2: List[int]
:rtype: List[int]
"""
temp = Solution()
nums1 = [1,2,3,5,6,3,7,4,6,9]
nums2 = [3,6,3]
ans = temp.intersect(nums1, nums2)
print ans
