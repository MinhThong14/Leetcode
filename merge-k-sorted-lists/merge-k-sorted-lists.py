# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoList(self, list1, list2):
        dummy = prev = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
            
        if list1:
            prev.next = list1
        
        if list2:
            prev.next = list2
        
        return dummy.next
        
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        
        if n == 0:
            return None
        
        i = 1
        
        
        while i < n :
            for j in range(0, n-i, i*2):
                if j+i < n:
                    lists[j] = self.mergeTwoList(lists[j], lists[j+i])

            i *= 2
        
        return lists[0]
                
            