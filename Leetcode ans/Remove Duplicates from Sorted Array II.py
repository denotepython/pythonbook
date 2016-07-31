# -*- coding:utf-8 -*-
class Solution(object):
    def removeDuplicates(self, nums):
        length1 = len(nums)
        count = 1
        for i in range(length1 - 1):
        	if nums[i+1] != nums[i]:
        		count += 1
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
a = Solution()
nums = [1,1,2,2,3]
length = a.removeDuplicates(nums)
print length
print nums