class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        nums = [0]*n 
      

        count = 0

        for i in range(n):
            nums[i] = nums1[i] - nums2[i]
     
        def merge(arr1,arr2):
          
            
            i = 0
            j = 0 
            merged_arr = []

            while i < len(arr1) and j < len(arr2):
                

                if arr1[i] < arr2[j]:
                    merged_arr.append(arr1[i])
                    i += 1
                else:
                    merged_arr.append(arr2[j])
                    j += 1 
                
            merged_arr.extend(arr1[i:])
            merged_arr.extend(arr2[j:])

            return merged_arr 
        
        def merged_sort(arr):
            nonlocal count , diff
            if len(arr) == 1:
                return arr 
            
            mid = len(arr) // 2 

            left_arr = merged_sort(arr[:mid])
            right_arr = merged_sort(arr[mid:])
            
            i = 0
            j = 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j] + diff:
                    count += len(right_arr) - j 
                    i += 1
                else:
                    j += 1




            return merge(left_arr,right_arr)
        
        merged_sort(nums)

        return count