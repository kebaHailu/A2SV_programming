class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x =len(word1)
        subword = ""
        if len(word1) < len(word2):
            x = len(word1)
            subword =word2[x:len(word2)+1]

        if len(word1) > len(word2):
            x = len(word2)
            subword = word1[x:len(word1)+1]


        added = []
        for i in range(x):
            added.append(word1[i]+word2[i])

        added = ''.join(added)
        
        return added + subword
