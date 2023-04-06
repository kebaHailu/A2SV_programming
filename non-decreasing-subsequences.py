class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        permutation = []

        def backtrack(idx,prev):
            if idx == len(nums):
                if len(permutation) >= 2:

                    ans.add(tuple(permutation))
                return

            
            backtrack(idx+1,prev)

            if nums[idx] >= prev:
                permutation.append(nums[idx])
                backtrack(idx+1,nums[idx])
                permutation.pop()

        backtrack(0,-101)
        return list(ans)