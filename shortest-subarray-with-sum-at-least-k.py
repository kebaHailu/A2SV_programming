class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        prifixsum = [0]
        monoqueue = deque()
        minlen = float("inf")
        for i in nums:
            prifixsum.append(prifixsum[-1]+i)
        
        for idx,val in enumerate(prifixsum):
            while monoqueue and prifixsum[monoqueue[-1]] >= val:
                monoqueue.pop()
            while monoqueue and val - prifixsum[monoqueue[0]] >= k:
                minlen = min(minlen,idx-monoqueue.popleft())
            monoqueue.append(idx)
        return -1 if minlen == float("inf") else minlen