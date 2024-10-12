from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Helper function to check rows and columns
        def check_dimension(row_or_column):
            filtered_row = [number for number in row_or_column if number != '.' ]
            row_set = set(filtered_row)
            return len(row_set) == len(filtered_row)
             
        # Check all rows
        for row in board:
            if not check_dimension(row):
                return False
             
        # Check all columns
        for column in [column for column in zip(*board)]:
            if not check_dimension(column):
                return False
            
        # Check all 3x3 sub-arrays        
        for three_by_three_slice in [[row[j:j+3] for row in board[i:i+3]] for i in range(0,9,3) for j in range(0,9,3)]:
            slice_list = []
            slice_set = set()
            for row in zip(*three_by_three_slice):
               
                for number in row:
                    if number != '.':
                        slice_list.append(number)
                        slice_set.add(number)
            if len(slice_set) != len(slice_list):
                return False
            
        return True

# Test case
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    print(solution.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    

    
# Time Complexity O(1)
# Space Complexity O(1)