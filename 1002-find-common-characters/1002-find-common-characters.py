class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        check = list(words[0])

        for word in words:
            newCheck = []

            for ch in word:
                if ch in check:
                    newCheck.append(ch)
                    check.remove(ch)
            check = newCheck

        return (check)