class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        res = [] 
        current = len(arr) 
        flip_index = -1 
        while current > 0:
            if arr[current - 1] == current: 
                current -= 1
                continue 
            flip_index = arr.index(current)
            if flip_index != 0:
                arr[:flip_index+1] = arr[:flip_index + 1][::-1]
                res.append(flip_index + 1)
            arr[:current] = arr[:current][::-1]
            res.append(current)
            current -= 1 
        return res 