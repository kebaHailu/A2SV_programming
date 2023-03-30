class Solution:
    def findComplement(self, num: int) -> int:
        
        l = len(bin(num)[2:])
        arr = ['1']*l
        arr = ''.join(arr)
        n = int(arr,2)

        return num ^ n