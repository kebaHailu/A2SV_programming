class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9+7
        n = len(nums)
        freq = [0]*(n+1)

        for start , end in requests:
            freq[start] += 1
            freq[end+1] -= 1
        
        for i in range(1,n+1):
            freq[i] += freq[i-1]
        freq.pop()
        
        ans = 0
        for n , f in zip(sorted(nums),sorted(freq)):
            ans += n * f
        
        
        return ans%mod