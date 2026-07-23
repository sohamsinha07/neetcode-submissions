class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #base case is if the currSum + currElement = target
        #use backtracking
        #two choices, either use the number again, or go onto another index
        #break if the sum is GREATER than target

        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res
