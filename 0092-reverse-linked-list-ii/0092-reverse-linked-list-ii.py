# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next == None:
            return head
			
		
        if left == right:
            return head
        
        leftNode= head
        rightNode= head
        leftPrevNode= None
        rightNextNod= None
        last= head
        steps = 1
		
        while (steps < right):
            if steps < left:
                leftPrevNode = leftNode
                leftNode = leftNode.next
            if steps < right:
                rightNode = rightNode.next
                rightNextNode = rightNode.next
            steps += 1
            last = last.next
        
        
        prev: Optional[ListNode] = leftNode
        current: Optional[ListNode] = leftNode.next
        temp: Optional[ListNode]
            
        while current != rightNextNode:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
      
        leftNode.next = rightNextNode
		
		
        if leftPrevNode == None:
            head = prev
        else:
            leftPrevNode.next = prev
      
        return head