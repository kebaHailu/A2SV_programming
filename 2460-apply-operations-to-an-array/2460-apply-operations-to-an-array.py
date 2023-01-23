class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                nums[i] = 2 * nums[i]
                nums[j] = 0


            i += 1
            j += 1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)


        return nums