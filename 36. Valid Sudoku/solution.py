from itertools import product

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        # Check Rows
        for row in board:
            row_list = [num for num in row if num.isnumeric()]

            if len(row_list) != len(set(row_list)):
                return False


        # Check Columns
        for column in range(9):
            column_list = [row[column] for row in board if row[column].isnumeric()]

            if len(column_list) != len(set(column_list)):
                return False


        # Check boxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                pairs = list(product(range(i,i+3),range(j,j+3)))

                box = []

                for pair in pairs:
                    if board[pair[0]][pair[1]].isnumeric():
                        box.append(board[pair[0]][pair[1]])
                
                if len(box) != len(set(box)):
                    return False

        return True
                


                

# Time Complexity: O(1)
# Space Complexity: O(1)
# Vibes coding percentage? 100%