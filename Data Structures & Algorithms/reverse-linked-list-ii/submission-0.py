# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        pos = 1

        leftPrev,curr = dummy, head 
        while pos < left:
            leftPrev,curr = curr,curr.next
            pos += 1
        
        # phase 2 curr at left and prev at left -1
        prev = None
        while pos >= left and pos <= right:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
            pos += 1
        
        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next

        