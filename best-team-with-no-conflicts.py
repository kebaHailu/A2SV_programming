class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ageScore = sorted(zip(ages,scores))

        n = len(ageScore)
        dp = [0]*n 
        dp[0] = ageScore[0][1]


        for i in range(1,n):
            max_sum = 0
            for j in range(i-1,-1,-1):
                if ageScore[i][1] >= ageScore[j][1]:
                    max_sum = max(dp[j],max_sum)
                
            
            dp[i] = max_sum + ageScore[i][1]

        return max(dp)