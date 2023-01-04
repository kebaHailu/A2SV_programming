class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        left = 0
        right = 1
        arr = []
        arr.append(s[0:spaces[0]])

        while right < len(spaces):

            word = s[spaces[left]:spaces[right]]
            arr.append(word)
            left += 1
            right += 1

        arr.append(s[spaces[len(spaces)-1]:])
        return " ".join(arr)