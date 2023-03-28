class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        st = 0
        end = len(nums) - 1
        res = [0] * len(nums)
        self.merge_process(list(enumerate(nums)), st, end, res)
        return res
        
    def merge_process(self, nums, st, end, res):
        if st == end:
            return
            
        mid = (st + end) // 2
        self.merge_process(nums, st, mid, res)
        self.merge_process(nums, mid + 1, end, res)
        self.merge(nums, st, end, res)
    
    def merge(self, nums, st, end, res):
        mid = (st + end)//2
        l_pt = st
        r_pt = mid + 1
        temp = []
        
        while(l_pt <= mid and r_pt <= end):
            if nums[r_pt][1] < nums[l_pt][1]:
                temp.append(nums[r_pt])
                r_pt += 1
            else:
                temp.append(nums[l_pt])
                res[nums[l_pt][0]] += r_pt - (mid + 1)
                l_pt += 1
                
        while(l_pt <= mid):
            temp.append(nums[l_pt])
            res[nums[l_pt][0]] += end - mid
            l_pt += 1
            
        while(r_pt <= end):
            temp.append(nums[r_pt])
            r_pt += 1
        
        for i in range(st, end + 1):
            nums[i] = temp[i - st]