class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times 
        self.leaders = []
        result = Counter()
        leader = 0


        for person in persons:
            result[person] += 1
            if result[person] >= result[leader]:
                leader = person
            self.leaders.append(leader)
    def bs(self, t):
        l = 0
        r = len(self.times)-1
        ans = -1
        while l <= r:
            m = (l+r)//2
            c = self.times[m]
        
            if c == t:
                return m
            elif c < t:
                ans = max(ans, m)
                l = m+1
            else:
                r = m-1
        # print ans, len(self.times)-1
        return ans
    def q(self, t: int) -> int:
        return self.leaders[self.bs(t)]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)