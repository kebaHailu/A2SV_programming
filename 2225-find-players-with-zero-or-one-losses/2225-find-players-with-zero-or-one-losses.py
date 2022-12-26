class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winner = set(chain(*matches))
        loss = Counter([l for _ , l in matches ])
        
        zero =[al for al in winner if loss[al] == 0 ]
        ones =[al for al in winner if loss[al] == 1 ]
        
        return sorted(zero), sorted(ones)

