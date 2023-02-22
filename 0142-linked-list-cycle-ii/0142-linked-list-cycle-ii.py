# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        tortoise = head
        hare = head

        while hare and hare.next:
            hare = hare.next.next 
            tortoise = tortoise.next 
            if hare == tortoise:
                # tortoise = head 
                while tortoise != head:
                    tortoise = tortoise.next 
                    head = head.next 
                return head 

       
        return 
            
            
            
     