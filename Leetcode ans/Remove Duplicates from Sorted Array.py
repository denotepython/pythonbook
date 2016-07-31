# -*- coding:utf-8 -*-
class Solution(object):
    def removeDuplicates(self, nums):
        s = set(nums)
        nums = list(s)
        length = len(nums)
        return nums
        """
        :type nums: List[int]
        :rtype: int
        """
a = Solution()
nums = [1,1,1,1,2,2,3]
nums = a.removeDuplicates(nums)
print nums