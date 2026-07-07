class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeroCount = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zeroCount += 1
        if zeroCount > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zeroCount: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
            
