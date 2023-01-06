class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        # to find the first maximum even sum
        mysum = sum([i for i in nums if i%2 == 0])

        # to collect all final values
        mylist = []

        # to iterate every value of queries and append the valid numbers
        for i in queries:
            if nums[i[1]] % 2 == 0:
                mysum -= nums[i[1]]

            nums[i[1]] += i[0]

            if nums[i[1]] % 2 == 0:
                mysum += nums[i[1]]

            mylist.append(mysum)
            
        return mylist