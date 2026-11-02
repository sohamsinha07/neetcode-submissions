class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        
        l, r = 0, row * col - 1
        while l <= r:
            m = l + (r - l) // 2
            ro, c = m // col, m % col
            if target > matrix[ro][c]:
                l = m + 1
            elif target < matrix[ro][c]:
                r = m - 1
            else:
                return True
        return False