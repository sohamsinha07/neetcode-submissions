class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)): # if list is length 5
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return[i, j]
        return[]
