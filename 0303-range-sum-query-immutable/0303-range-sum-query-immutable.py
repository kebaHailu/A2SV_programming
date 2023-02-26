class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        
        
        
        
            
            
        

    def sumRange(self, left: int, right: int) -> int:
        
        prefix_sum = [0]
        all_sum = 0
        for num in self.nums:
            all_sum += num 
            prefix_sum.append(all_sum)
            
       
        return prefix_sum[right+1] - prefix_sum[left]
    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)