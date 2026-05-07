# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getGCD(a, b):
            if b == 0:
                return a
            return getGCD(b, a % b)
        
        curr1 = head
        prev = None
        dummy = ListNode(0,head)


        curr2 = dummy.next # will be use to create a new list
        while curr1:
            if prev:
                gcd = getGCD(curr1.val,prev.val)
                curr2.next = ListNode(gcd,curr1)
                curr2 = curr2.next.next
            prev = curr1
            curr1 = curr1.next
        return dummy.next
        