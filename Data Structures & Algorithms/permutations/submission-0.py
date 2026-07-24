class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #go all the way down on one index at a time
        #yes or no for every other possible index
        #base case is when 
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res
        
    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False