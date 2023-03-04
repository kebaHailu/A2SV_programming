class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        myd = defaultdict(int)
        myd[0] = 1

        ans =0
        runsum =0 

        for num in nums:
            runsum += num 
            val = runsum % k 
            ans += myd[val]
            myd[val] += 1

        return ans