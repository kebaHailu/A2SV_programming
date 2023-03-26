class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            
            curr = nums[i]-1

            while curr < n and curr != i and curr+1 != nums[curr]:
                nums[curr],nums[i]=nums[i],nums[curr]
                curr = nums[i]-1
        
        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(i+1)
        
        return ans