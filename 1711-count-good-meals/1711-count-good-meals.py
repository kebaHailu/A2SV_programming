import math
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        result = 0
        hm = Counter()
        for num in deliciousness:
            for i in range(22): result += hm[2**i-num]
            hm[num] += 1
        return result % ((10 ** 9) + 7)