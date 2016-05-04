#题目不让用循环，用python循环灰超时，C++循环pass
class Solution(object):
    def isPowerOfFour(self, num):
        count = 0
        check = 1
        temp = num
        while temp != 0:
            if temp % 4 == 0:
                count += 1
            temp /= 4
        for i in range(count):
            check *= 4
        if check == num:
            return True
        else:
            return False

'''
a = Solution()
flag = a.isPowerOfFour(16)

print flag
'''