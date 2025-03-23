class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # If first spot is blocked returned zero
        if obstacleGrid[0][0] == 1:
            return 0

        # Otherwise always one way to get to first cell
        else:
            obstacleGrid[0][0] = 1

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # Iterate First Row
        for j in range(1,n):
            # Blocked spot set to zero ways
            if obstacleGrid[0][j] == 1:
                obstacleGrid[0][j] = 0

            else: 
                obstacleGrid[0][j] = obstacleGrid[0][j-1]

        # Iterate First Column
        for i in range(1,m):
            # Blocked spot to zero
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]

        # Now Iterate from 1x1 the same way
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[-1][-1]


        


# Time Complexity: O(m*n)
# Space Complexity: O(1)