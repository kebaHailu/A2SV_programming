class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        for i in range(n):
            
            curr = nums[i]-1
     
            while i != curr:
                if nums[i] == nums[curr]:
                    arr.append(nums[i])
                    break
                
            
                
                curr = nums[i]-1
                nums[curr],nums[i] = nums[i],nums[curr]


        return list(set(arr))