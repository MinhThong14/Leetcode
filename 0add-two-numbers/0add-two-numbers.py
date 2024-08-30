# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = l1
        
        while l1 or l2:
            if l1 and l2:
                cur_sum = l1.val + l2.val + carry
                if not l1.next and l2.next:
                    l1.next = l2.next
                    l2.next = None
                
                l2 = l2.next
            else:
                cur_sum = l1.val + carry
            
            
            if cur_sum > 9:
                cur_digit = cur_sum % 10
                carry = 1
            else:
                cur_digit = cur_sum
                carry = 0
            
            l1.val = cur_digit
            if not l1.next and carry:
                new_node = ListNode()
                l1.next = new_node
            l1 = l1.next
        
        return dummy