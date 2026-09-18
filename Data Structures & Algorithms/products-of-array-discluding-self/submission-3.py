class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zcount = 1, 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zcount += 1
        if zcount > 1: 
            return [0] * len(nums)
            
        res = [0] * len(nums)
        
        for index, value in enumerate(nums):
            if zcount > 0:
                if value == 0:
                    res[index] = prod
                else:
                    res[index] = 0
            else:
                res[index] = prod // value
        return res
        
        