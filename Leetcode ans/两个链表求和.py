# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        count = 0
        SUM = ListNode()
        while l1.next != None:
            count += 1
        
        temp = l1.val + l2.val
        yushu = temp % 10
        jinwei = temp / 10
        SUM.next.val = yushu
        
        for i in range(count - 1):
            temp = l1.next.val + l2.next.val
            yushu = temp % 10
            SUM.next.val = yushu + jinwei
            jinwei = temp / 10
        return SUM

a = Solution()
l1 = ListNode([2, 4, 3])
l2 = ListNode([5, 7, 4])

SUM =a.addTwoNumbers(l1, l2)
print SUM
'''

:type l1: ListNode
:type l2: ListNode
:rtype: ListNode
'''

        