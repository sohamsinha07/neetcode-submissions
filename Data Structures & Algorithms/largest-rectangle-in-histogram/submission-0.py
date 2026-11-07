class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #find the longest consecutive heights with a minimum height
        #calculate the area of that rectangle, compare with a global maxArea, then return that maxArea
        #keep track of the mostMin element you've encountered so far and when a new height is lower than that element work with that new height
        maxArea = 0
        stack = [] #pair of (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start,h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
