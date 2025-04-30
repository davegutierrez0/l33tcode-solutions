class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.traverse_island(grid,i,j)
                    num_islands += 1
        
        return num_islands

    def traverse_island(self,grid, row, column):
        if (
            row < 0
            or column < 0
            or row >= len(grid)
            or column >= len(grid[0])
            or grid[row][column] != "1"
        ):
            return
            
        # mark adjacent nodes as 0 or visited
        grid[row][column] = "0"

        # recursively search all adjacent nodes
        self.traverse_island(grid, row - 1, column)
        self.traverse_island(grid, row + 1, column)
        self.traverse_island(grid, row, column - 1)
        self.traverse_island(grid, row, column + 1)


# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# #IslandDFS — Sink and Count using 4-directional DFS