class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m_rows = len(matrix)
        n_cols = len(matrix[0])

        num_elements = m_rows * n_cols
        output = []

        left_bound = 0
        upper_bound = 0
        right_bound = n_cols - 1
        lower_bound = m_rows -1 



        while left_bound <= right_bound and upper_bound <= lower_bound:

            # Move Right
            for x in range(left_bound, right_bound + 1):
                output.append(matrix[upper_bound][x])
            
            upper_bound += 1


            # Move Down
            for y in range(upper_bound, lower_bound + 1):
                output.append(matrix[y][right_bound])
       
            right_bound -= 1

            # Move Left 
            if upper_bound <= lower_bound:
                for x in range(right_bound, left_bound - 1,-1):
                    output.append(matrix[lower_bound][x])
                
                lower_bound -= 1



            # Move Up   
            if left_bound <= right_bound:
                for y in range(lower_bound, upper_bound - 1, -1):
                    output.append(matrix[y][left_bound])
                
                left_bound += 1
        

            

        return output

# Time Complexity: O(m*n)
# Space Complexity: O(1)