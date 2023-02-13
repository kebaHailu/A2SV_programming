# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_val =  None 
        current_val = head 
        
        while current_val:
            next_val = current_val.next 
            current_val.next = pre_val 
            pre_val = current_val 
            current_val = next_val
        return pre_val