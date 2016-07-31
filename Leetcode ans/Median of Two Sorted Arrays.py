class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        left1 = 0
        right1 = len1 - 1
        left2 = 0
        right2 = len2 - 1
        while (left1 < right1 or left2 < right2):
        	mid1 = (left1 + right1) / 2
        	mid2 = (left2 + right2) / 2
        	if mid1 < mid2:
        		left1 = mid1 + 1
        		right2 = mid2 - 1
        	elif mid1 > mid2:
        		right1 = mid1 - 1
        		left1 = mid2 + 1
        	else:
        		return mid1
        return mid1
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
nums1 = [1,2,3]
nums2 = [4,5,6,7]
a = Solution()
med = a.findMedianSortedArrays(nums1, nums2)
print med
