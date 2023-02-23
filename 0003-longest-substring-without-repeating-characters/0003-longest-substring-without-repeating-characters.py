class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checkset = set()
        left=0
        right=0
        result = 0
        while right < len(s):
            while s[result] in checkset:
                checkset.remove(s[left])
                left +=1
            checkset.add(s[right])
            result = max(result,right-left+1)
            right += 1
        return result
