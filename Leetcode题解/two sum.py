class Solution(object):
    def twoSum(self, nums, target):
        temp = sorted(nums) #sorted函数不会改变nums本身，而是重新生成一个新的list
        i = 0
        j = len(temp) - 1  #双指针法
        while i < j:
            if temp[i] + temp[j] == target:
                break
            elif temp[i] + temp[j] < target:
                i += 1
            else:
                j -= 1
        for p in range(len(nums)):
            if nums[p] == temp[i]:
                indice1 = p
                break
        for p in range(len(nums)):
            if nums[p] == temp[j] and p != indice1:
                indice2 = p
                break
        return [indice1, indice2]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
'''
a = Solution()
List = [0, 4, 3, 0]
ans = a.twoSum(List, 0) 
print ans
'''