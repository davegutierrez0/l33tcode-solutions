class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = [[None] * n for _ in range(n)]




        def findMinFallingPathSum(row,col):
            # Out of Bounds Check
            if col < 0 or col >= n:
                return float('inf')
            # Base case is last row
            if row == n - 1:
                return matrix[row][col]

            # Return memoized value if available
            if memo[row][col] is not None:
                return memo[row][col]
        
            # Recursively compute minimum falling path sum for next row
            left = findMinFallingPathSum(row+1,col-1)
            middle = findMinFallingPathSum(row+1,col)
            right = findMinFallingPathSum(row+1,col+1)

            memo[row][col] = matrix[row][col] + min(left,right,middle)
            return memo[row][col]

        # Compare starting from every column in the first row 
        minimum_sum = float('inf')
        
        for i in range(len(matrix[0])):
            minimum_sum = min(minimum_sum, findMinFallingPathSum(0,i))
        
        return minimum_sum 

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)