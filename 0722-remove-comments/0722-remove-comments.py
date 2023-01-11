class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        

        buffer = []
        char = ""
        open = False
        res = []
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]

                if char == '/' and (i + 1) < len(line) and line[i + 1] == '/' and not open:
                    i = len(line) 

                elif char == '/' and (i + 1) < len(line) and line[i + 1] == '*' and not open:
                    open = True
                    i += 1

                elif char == '*' and (i + 1) < len(line) and line[i + 1] == '/' and open:
                    open = False
                    i += 1

                elif not open:
                    buffer += char
                i += 1
            if buffer and not open:
                res.append(''.join(buffer))
                buffer = ''
        return res

