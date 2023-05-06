# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def insert(node,item):
            temp = ListNode(item)
            
            if node == None:
                return temp
            else :
                prev = node
                while prev.next != None:
                    prev = prev.next
                prev.next = temp
            return node

        arr = []

        for i in lists:

            while i:
                arr.append(i.val)
                i = i.next 
            
        
        head = ListNode()
        cur = head
        arr.sort()

        for i in arr:
            cur = insert(cur,i)
        return head.next