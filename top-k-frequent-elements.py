class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        arr = list(map(list,count.items()))

        arr.sort(key=lambda x:x[1],reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(arr[i][0])
        return ans