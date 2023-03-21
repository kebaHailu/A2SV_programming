class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []
        for idx in range(len(position)):
            cars.append([position[idx],speed[idx]])

        sort_cars = sorted(cars,key=lambda x:x[0],reverse=True)

        
        for car_pos , car_speed in cars:
            cur_location = (target-car_pos)/car_speed
            stack.append(cur_location)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(sort_cars)