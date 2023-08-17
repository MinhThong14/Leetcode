# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        defer = 0
        dummy = l1
        
        while l1 or l2:
            if l1 and l2:
                current_sum = l1.val + l2.val
                if not l1.next and l2.next:
                    l1.next = l2.next
                    l2.next = None
                l2 = l2.next
            else:
                current_sum = l1.val
                
            if defer:
                current_sum += 1
                defer = 0
            if current_sum > 9:
                current_sum %= 10
                defer = 1

            l1.val = current_sum
            if not l1.next and defer:
                l1.next = ListNode()
            l1 = l1.next

        return dummy
        