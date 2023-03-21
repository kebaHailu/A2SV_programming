class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        check = set()

        for i in s:
            if i not in check:
                while stack and stack[-1] > i and count[stack[-1]] > 0:
                    check.remove(stack.pop())
                stack.append(i)
                check.add(i)
            
            count[i] -= 1 
                
        return ''.join(stack)