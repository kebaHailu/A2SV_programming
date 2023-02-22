# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mylist =[]
        
        
        
        
        
        while list1:
            mylist.append(list1.val)
            list1 = list1.next 
        while list2:
            mylist.append(list2.val)
            list2 = list2.next 
            
        mylist.sort()
        if mylist:
            mergedlist = ListNode(mylist[0])
        else :
            return 
        mglist = mergedlist
        for i in range(1,len(mylist)):
            
            mergedlist.next = ListNode(mylist[i])
            
            mergedlist = mergedlist.next 
            
            
            
            
        return mglist 
            
        
        
        
        