class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #check the first two spots if they add up to the target
        # if the value is too small, move the right pointer to the right
        # if the value is too large, move the left pointer to the right
        #return the index + 1 of the two indices where the condition is true
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
