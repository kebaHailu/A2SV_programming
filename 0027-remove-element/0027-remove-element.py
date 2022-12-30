class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        counter = nums.count(val)
        
        for i in nums:
            if i == val:
                nums.pop(nums.index(i))
                nums.append(i)
            
        return len(nums)-counter