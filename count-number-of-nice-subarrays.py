class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        count = defaultdict(int)
        count[0] = 1
        oddSum = 0
        for n in nums:
            oddSum += n % 2
            count[oddSum] += 1

        
      
        
        loop = oddSum - k + 1
        ans = 0
        for i in range(loop):
            ans += count[i] * count[k+i]

       
        return ans