class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zCnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zCnt += 1
        if zCnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zCnt:
                if c == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else: res[i] = prod // c
        return res
        