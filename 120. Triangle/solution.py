class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = [[None for j in range(len(triangle[-1])) if j <= i] for i in range(len(triangle))]

        def dp(row,col):
            # Bound it
            if col < 0 or col > row:
                return float('inf')
            # Base Case 
            if row == len(triangle) - 1:
                return triangle[row][col]

            # Return memo value immediately if we have one
            if memo[row][col] is not None:
                return memo[row][col]
            
            left = dp(row+1,col)
            right = dp(row+1,col+1) 
            
            # Add current to next result
            memo[row][col] = triangle[row][col] + min(left,right)
            
            return memo[row][col]
        
        return dp(0,0)

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)