# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def bin_find():
            left = 1
            right = mountain_arr.length() - 1

            while left <= right:
                mid = (left + right)//2 

                a = mountain_arr.get(mid)
                b = mountain_arr.get(mid+1)
                c = mountain_arr.get(mid-1)

                if c < a > b:
                    return mid
                elif c < a < b:
                    left = mid + 1
                else:
                    right = mid - 1
        print(bin_find())
        # first search 
        def searchLeft(target):
            left = 0
            right = bin_find()

            while left <= right:
                mid = (left + right)//2
                cur_val = mountain_arr.get(mid)
                if target == cur_val:
                    return mid 
                if target < cur_val:
                    right = mid - 1
                else :
                    left = mid + 1


            return -1
        
        # second search
        def searchRight(target):
            left = bin_find()
            right = mountain_arr.length()-1

            while left <= right:
                mid = (left + right)//2
                cur_val = mountain_arr.get(mid)
                if target == cur_val:
                    return mid 
                if target < cur_val:
                    left = mid + 1
                else :
                    right = mid - 1


            return -1  

        ans = searchLeft(target)
        if ans == -1:
            return searchRight(target)
        return ans