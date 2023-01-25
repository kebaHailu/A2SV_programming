class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        newbe =[]
        for i in nums:
            listi = list(reversed(str(i)))
            inti = int(''.join(listi))
            newbe.append(inti)
        nums = nums + newbe

        return (len(set(nums)))
