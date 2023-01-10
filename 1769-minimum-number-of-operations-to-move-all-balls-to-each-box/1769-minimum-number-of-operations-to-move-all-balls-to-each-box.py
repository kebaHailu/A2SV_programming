class Solution:
    def minOperations(self, boxes: str) -> List[int]:
       
        i = 0
        arr =[]
        while i < len(boxes):
            j = 0
            x = 0
            while j < len(boxes):
                if boxes[j] == "1":
                    x += abs(i - j)

                j += 1

            arr.append(int(x))

            i += 1


        return arr


