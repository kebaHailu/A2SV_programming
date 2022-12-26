class Solution:
    def freqAlphabets(self, s: str) -> str:
        sol =[]
        i = 0
        
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                val = int(s[i: i + 2])
                sol.append(chr(val + 96)) # chr(97 - 122) is 'a' to 'z'
                i += 3
            else:
                sol.append(chr(int(s[i]) + 96))
                i += 1
        return ''.join(sol)
     