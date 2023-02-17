# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyleft = ListNode()
        dummyright = ListNode()
        left , right = dummyleft , dummyright 
        
        while head:
            
            if head.val >= x:
                right.next = head 
                right = right.next 
            else :
                left.next = head 
                left = left.next 
                
                
            head = head.next 
        
            
        left.next = dummyright.next 
        right.next = None 
        
        return dummyleft.next
        
        
            
            
        