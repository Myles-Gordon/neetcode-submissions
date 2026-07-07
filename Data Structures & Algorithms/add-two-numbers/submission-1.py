# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = head = ListNode()
        while l1 and l2:
            nex = ListNode()
            res.next = nex
            num = l1.val+l2.val
            if res.val + num < 10:
                res.val += num
                res = res.next
            else:
                num -= 10
                res.val += num
                res.next.val += 1
                res = res.next
            
            l1 = l1.next
            l2 = l2.next

        while l1:
            nex = ListNode()
            res.next = nex
            if res.val + l1.val < 10:
                res.val += l1.val
                res = res.next
            else:
                l1.val -= 10
                res.val += l1.val
                res.next.val += 1
                res = res.next
            l1 = l1.next

        while l2:
            nex = ListNode()
            res.next = nex
            if res.val + l2.val < 10:
                res.val += l2.val
                res = res.next
            else:
                l2.val -= 10
                res.val += l2.val
                res.next.val += 1
                res = res.next
            l2 = l2.next

        if res.val == 0:
            curr = head
            while curr.next != res:
                curr = curr.next
            
            curr.next = None
        return head