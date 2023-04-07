class Solution:
    def isValid(self, s: str) -> bool:
        hash = {"}":"{",")":"(","]":"["}
        stack = []

        for i in range(len(s)):
            if s[i] in hash:
                if not stack:return False
                val = stack.pop()
                if hash[s[i]] != val:
                    return False
            else:
                stack.append(s[i])

        return not stack