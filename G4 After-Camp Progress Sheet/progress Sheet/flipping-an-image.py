class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        array = []
        for img in image:
            
            array.append(img[::-1])

        
        for i in range(len(image)):
            for j in range(len(image[0])):
                if array[i][j] == 1:
                    array[i][j] = 0
                else:
                    array[i][j] = 1 
        

        return array
