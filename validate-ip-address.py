class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        v4 = queryIP.split('.')
        v6 = queryIP.split(':')
        
        if len(v4) == 4:
            count = 0
            for val in v4:
                if val.isdigit() and 0 <= int(val) <= 255:
                    if len(val) > 1 and val[0] == '0':
                        continue  
                    count += 1
            
            if count == 4:
                return "IPv4"
        
        elem = {'a','b','c','d','e','f'}
        if len(v6) == 8:
            count = 0
            for val in v6:
                if 1<=len(val) <=4 and all(i.isdigit() or i.lower() in elem for i in val):
                    count += 1
            
            if count == 8:
                return "IPv6"
        
        return "Neither"