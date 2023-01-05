class Solution:
    def printVertically(self, s: str) -> List[str]:

        word = list(s.split())
        vertlist = []

        max_chr = max([len(i) for i in word])

        neword = []

        for i in word:
            if len(i) < max_chr:
                neword.append(i + ' '*(max_chr-len(i)))
            else :
                neword.append(i)

        for i in range(max_chr):
            myword = ""


            for j in range(len(word)):
                myword =myword + neword[j][i]


            myword = myword.rstrip()


            vertlist.append(myword)

        return vertlist