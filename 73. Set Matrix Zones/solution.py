class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_coordinates = [] 

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    zero_coordinates.append((y,x))

        # print(zero_coordinates)

        for pair in zero_coordinates:
            y, x = pair

            # Set Row to Zero
            for i in range(len(matrix[0])):
                matrix[y][i] = 0

            # Set Column to Zero
            for j in range(len(matrix)):
                matrix[j][x] = 0

# Time Complexity: O(N*M)
# Space Complexity: O(N*M)