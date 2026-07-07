# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = head = ListNode()
        while l1 or l2:
            nex = ListNode()
            res.next = nex
            if l1 and l2:
                num = l1.val+l2.val
            elif l1:
                num = l1.val
            else:
                num = l2.val
            if res.val + num < 10:
                res.val += num
                res = res.next
            else:
                num -= 10
                res.val += num
                res.next.val += 1
                res = res.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if res.val == 0:
            curr = head
            while curr.next != res:
                curr = curr.next
            
            curr.next = None
        return head