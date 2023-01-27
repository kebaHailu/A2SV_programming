class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        num_sorted = sorted(nums)
        count = num_sorted.count(target)
        
        if count > 0:
            
            target_index = num_sorted.index(target)


            arr = [target_index]
            if count > 1:

                for i in range(1,count):
                    arr.append(target_index + i)
            return arr
        
        return []