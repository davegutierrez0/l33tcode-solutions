class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []      
        
        triangle = []
        
      

        
        for row in range(numRows):
            
            row_length = row + 1

            row_n = [0] * row_length

            for col in range(row_length):
                if col == 0 or col == row_length-1:
                    row_n[col] = 1
                else:
                    row_n[col] = triangle[row-1][col-1] + triangle[row-1][col]
            
            triangle.append(row_n)
        
        return triangle

    # Time Complexity: O(numRows^2)
    # Space Complexity: O(1) (excluding output)