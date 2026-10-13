class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #both arrays are of the same length n
        #destination is at index target 
        # 1, 1+3 = 4, 4+3 = 7, 7+3 = 10
        # 4, 4+2 = 6, 6+2 = 8, 8+2 = 10
        #both cars meet at the target
        #position[i] + speed[i] = newPosition[i] (add to stack)

        pair = []
        for p, s in zip(position, speed):
            pair.append((p,s))
        pair.sort(reverse=True)
        stack = []
        for p, s in pair: #reverse sorted order
            stack.append((target-p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)