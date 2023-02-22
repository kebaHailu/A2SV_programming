# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next 
        
        i = 0
        j = len(arr)-1
        max_twin = 0
        
        while i < j :
            minsum = arr[i] + arr[j]
            max_twin = max(max_twin,minsum)
            i += 1
            j -= 1
            
        return max_twin
            