class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        list1 =[x for x in nums if x%2==0]
        list2 =[x for x in nums if x%2!=0]
        return list1 + list2