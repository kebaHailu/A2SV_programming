class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        tot_product = 1
        zero_count = nums.count(0)
        
        if zero_count > 1:
            arr = [0]*len(nums)
        elif zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue 
                else:
                    tot_product *= nums[i]
            for i in range(len(nums)):
                if nums[i] == 0:
                    arr.append(tot_product)
                else :
                    arr.append(0)
        else:
            
            for i in range(len(nums)):

                tot_product *= nums[i]


            for i in range(len(nums)):
                arr.append(tot_product // nums[i])
        
        return arr
            