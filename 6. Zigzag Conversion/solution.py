import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert string to zigzag pattern and return read line by line.
        
        Args:
            s: Input string
            numRows: Number of rows in zigzag pattern
            
        Returns:
            String read line by line from zigzag pattern
        """
        # Handle edge case
        if numRows == 1 or numRows >= len(s):
            return s
            
        n = len(s)
        
        # Calculate number of columns needed for the matrix
        cycle_length = 2 * numRows - 2
        numCols = math.ceil(n / cycle_length) * (numRows - 1)
        
        # Initialize matrix
        matrix = [[''] * numCols for _ in range(numRows)]
        
        # Fill matrix with zigzag pattern
        currRow, currCol = 0, 0
        i = 0
        
        while i < n:
            # Move down
            while currRow < numRows - 1 and i < n:
                matrix[currRow][currCol] = s[i]
                i += 1
                currRow += 1
            
            # Move diagonally up
            while currRow > 0 and i < n:
                matrix[currRow][currCol] = s[i]
                i += 1
                currRow -= 1
                currCol += 1
        
        # Convert matrix back to string
        result = ''
        for row in matrix:
            result += ''.join(char for char in row if char)
            
        return result


        # Time complexity: O(numRows * n)
        # Space complexity: O(n)