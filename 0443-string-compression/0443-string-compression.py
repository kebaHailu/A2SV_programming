class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("")
        count = 0
        prev = chars[0]
        ans = ""
        
        for i in chars:
            if i == prev:
                count += 1
            elif count == 1:
                ans += prev
                count = 1
            else:
                ans += prev + str(count)
                count = 1
            
            prev = i
            
        ans = [i for i in ans]   
        chars[:] = ans
        return len(chars)
                
                
            
