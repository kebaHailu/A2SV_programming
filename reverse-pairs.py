class Solution:
    def reversePairs(self, nums: List[int]) -> int: 
        count = 0 
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
        
        def merge_sort(arr):
            nonlocal count
            if len(arr) == 1:
                return arr 
            
            mid = len(arr)//2 
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            i = 0
            j = 0
            
            while i<len(left) and j < len(right):
                if  left[i] > right[j] * 2:
                    count += len(left) - i
                    j += 1 
                else:
                    i += 1
              
                
            return merge(left,right)
        merge_sort(nums)
        return count