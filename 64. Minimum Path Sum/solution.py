class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        memo = [[None for column in range(n)] for row in range(m)]

        def dp(row,col):
            # Bound
            if row >= m or col >= n:
                return float('inf')
            
            # Base Case
            if row == m-1 and col == n - 1:
                return grid[row][col]

            # Return memo if defined
            if memo[row][col] is not None:
                return memo[row][col]

            down = dp(row+1,col)
            right = dp(row,col+1)

            memo[row][col] = min(down,right) + grid[row][col]
            return memo[row][col]

        return dp(0,0)

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)