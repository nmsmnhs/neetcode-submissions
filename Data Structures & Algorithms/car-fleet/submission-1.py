class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [[position[i],speed[i]] for i in range(len(position))]
        time.sort(key = lambda x:x[0], reverse = True)
        time = [(target - time[i][0]) / time[i][1] for i in range(len(position))]
        stack = []
        for i in range(len(position)):
            if stack and time[i] <= stack[-1]:
                continue
            else:
                stack.append(time[i])
        return len(stack)
        
