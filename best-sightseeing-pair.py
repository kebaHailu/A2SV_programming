class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        ith = [values[i]+i for i in range(len(values))]
        jth = [values[j]-j for j in range(len(values))]

        for i in range(1,len(ith)):
            ith[i] = max(ith[i],ith[i-1])
        
        ans = 0
        for j in range(len(jth)-1,0,-1):
            jth[j-1] = max(jth[j-1],jth[j])
            ans = max(ans,ith[j-1]+jth[j])
        
        return ans