class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [0,1,0]
        ans = [[1]]
        for i in range(1,numRows):
            
            arr = nums[:]
            arr.append(0)
            for i in range(1,len(nums)):
                arr[i] = nums[i-1]+ nums[i]
            
            nums = arr[:]
            ans.append(nums[1:-1])
           
        
        return ans