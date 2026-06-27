# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count+=1
            current = current.next

        if count == n:
            return head.next

        count2 = 0
        current2 = head
        while count2 < count-n-1:
            count2+=1
            current2 = current2.next

        if current2.next:
            current2.next = current2.next.next
        else:
            current2.next = None

        return head
        

