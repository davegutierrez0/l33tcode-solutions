class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        self.transpose(matrix)
        self.reflect(matrix)
        

    def transpose(self,matrix: List[List[int]])-> None:
        matrix[:] = map(list,zip(*matrix))

    def reflect(self, matrix: List[List[int]])-> None:
        n = len(matrix)

        for i in range(n): 
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
                
# Time complexity: O(N^2)
# Space complexity: O(N^2)
```