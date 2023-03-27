class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        

        

        def backtrack(nums,index,path,ans):
            
            ans.append(path)

            for i in range(index,len(nums)):

                backtrack(nums,i+1,path+[nums[i]],ans)

        backtrack(nums,0,[],ans)
        return ans