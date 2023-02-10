class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1 
        max_val = 0

        while i < j :

            sub_height = min(height[i],height[j])
            width = j - i 
            area = sub_height * width 
            max_val = max(max_val,area)
            if height[i] >= height[j]:
                j -= 1 
            else :
                i += 1
        return (max_val)

    