class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        # this will map the nums into [ count, start , end]
        degree_mapper = defaultdict(list)
        for i in range(len(nums)):
            if degree_mapper[nums[i]]:
                degree_mapper[nums[i]][0] += 1 
                degree_mapper[nums[i]][2] = i 
            else:
                degree_mapper[nums[i]] = list([1,i,i])
        
        ans = float("inf")
        max_val = 0
        print(degree_mapper)
        for val,start,end in degree_mapper.values():
            if val > max_val:
                ans = end - start + 1
                max_val = val 
            elif val == max_val:
                ans = min(ans,end-start+1)
                
        
        return ans