# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return []
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        dummy, head_1 = None, slow.next
        while head_1:
            temp = head_1.next
            head_1.next = dummy
            dummy = head_1
            head_1 = temp
        
        slow.next = None
        head_2, head_3 = head, dummy
        while head_3:
            next_2 = head_2.next
            next_3 = head_3.next
            
            head_2.next = head_3
            head_3.next = next_2
            
            head_2 = next_2
            head_3 = next_3
    
        return head
            
            