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

            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            num = first + second
            
            total = res.val + num
            res.val = total % 10
            res.next.val += total // 10
            res = res.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if res.val == 0:
            curr = head
            while curr.next != res:
                curr = curr.next
            
            curr.next = None
        return head