class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeroCount = 1, 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zeroCount += 1
            
        if zeroCount > 1: 
            return [0] * len(nums)

        res = [0] * len(nums)
        for index, character in enumerate(nums):
            if zeroCount:
                if character == 0:
                    res[index] = prod
                else:
                    res[index] = 0
            else:
                res[index] = prod // character
        return res