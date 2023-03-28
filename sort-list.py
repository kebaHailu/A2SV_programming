# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def sorter(h1,h2):
            pre = None
            cur1 = h1
            cur2 = h2 

            while cur1 and cur2:
                if cur1.val > cur2.val:
                    if not pre:
                        pre = cur2 
                        h1 = pre
                        cur2 = cur2.next 
                        pre.next = cur1 
                    else:
                        pre.next = cur2 
                        cur2 = cur2.next 
                        pre = pre.next 
                        pre.next = cur1 
                else:
                    if not cur1.next:
                        cur1.next = cur2
                        break 
                    else:
                        pre = cur1 
                        cur1 = cur1.next 
            return h1

        
        def merger(head):
            slow = head 
            fast = head 

            if not head.next:
                return head 
            if not head.next.next:
                h1 = head
                h2 = head.next 
                head.next = None 
            
            else:
                while fast.next and fast.next.next:
                    slow = slow.next
                    fast = fast.next.next 
                h1 = head 
                h2 = slow.next 
                slow.next = None 

            h1 = merger(h1)
            h2 = merger(h2)

            
            return sorter(h1,h2)

            
        
        if not head:
            return 
        return merger(head)