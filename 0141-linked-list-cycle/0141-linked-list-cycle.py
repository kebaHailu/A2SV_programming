# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False 
        if head.next is None:
            return False
        
        tortoise = head
        hare = head.next 
        
        while hare and hare.next :
            if hare == tortoise:
                return True 
            
            hare = hare.next.next
            tortoise = tortoise.next 
        
        return False 
    
            