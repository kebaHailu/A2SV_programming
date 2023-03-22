class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

     
        f = lambda x: x.count(min(x))
        W = sorted(list(map(f, words)))
        return [len(W) - bisect_right(W, i) for i in map(f, queries)]