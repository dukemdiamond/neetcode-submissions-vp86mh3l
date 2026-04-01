class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Sudoku board
        int[][] board (9x9)

        Valid Conditions:
        - Each ROW contains digits 1-9 without duplicates
        - Each COL contains digits 1-9 without duplicates
        - Each of the 9 3x3 BOXES must contain digits 1-9 without duplicates

        Else false

        Brute force: 
        - 1 & 2: Loop thorugh each row and column, check for numbers iwthout duplicates
            - We can store that in a set
        
        - 3: Divy loop by 3x3 board coordinates


        '''
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    box_idx = (r // 3) * 3 + (c // 3)
                    if board[r][c] in rows[r] or  board[r][c] in cols[c] or  board[r][c] in boxes[box_idx]:
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[box_idx].add(board[r][c])
                    
        return True