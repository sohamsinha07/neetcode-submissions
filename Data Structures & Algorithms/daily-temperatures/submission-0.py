class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #add values to stack
        #keep a counter to count for output
        #calculate the difference between the next 
        res = [0] * len(temperatures)
        stack = [] #pair : [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))
        return res


        #70, 71, 75, 53, 983

        res = [0] * len(temperatures)
        stack = [] #pair : [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res