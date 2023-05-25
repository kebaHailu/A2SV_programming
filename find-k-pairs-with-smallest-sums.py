class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        def add(i, j):
            if i<len(nums1) and j<len(nums2):
                heappush(heap, (nums1[i]+nums2[j], i, j))
        
        add(0, 0)
        ans = []
        while k and heap:
            k -= 1
            _, a, b = heappop(heap)
            
            ans.append((nums1[a], nums2[b]))
            add(a, b+1)
            if b==0:
                add(a+1, b)
        return ans