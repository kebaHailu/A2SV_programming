class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0



        for i in s:
            if i.isdigit():
                cur_num = cur_num * 10 + int(i)
            
            elif i == "[":
                stack.append(cur_str)
                stack.append(cur_num)

                # reset the values 
                cur_str = ""
                cur_num = 0 

            
            elif i == "]":
                perv_num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + cur_str * perv_num

            
            else :
                cur_str += i

        while stack:
            cur_str += stack.pop()
        
        return cur_str