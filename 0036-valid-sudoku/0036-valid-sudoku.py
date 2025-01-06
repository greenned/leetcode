class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for rows in board:
            counter = {}
            for row in rows:
                if row != ".":
                    counter[row] = counter.get(row,0) + 1
                    if counter[row] >= 2:
                        return False
        
        for col in range(9):
            counter = {}
            for rows in board:
                row = rows[col]
                if row != ".":
                    counter[row] = counter.get(row,0) + 1
                    if counter[row] >= 2:
                        return False

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

                
        return True
        
        # columns, rows = 9, 9
        # sub_box_list = []
        # for row in range(rows):
        #     row_list = []
        #     col_list = []
            

        #     if row % 3 == 0:
        #         sub_box_list.append([])
            
        #     for col in range(columns):
                
        #         # sub box condition
        #         if col % 3 == 0:    
        #             sub_box_list[row // 3].append([])
        #             print(sub_box_list)
                    
                
        #         # column condition
        #         col_value = board[row][col]
        #         if col_value != "." and col_value in col_list:
        #             return False
        #         else:
        #             col_list.append(col_value)
                
        #         # row condition
        #         row_value = board[col][row]
        #         if row_value != "." and row_value in row_list:
        #             return False
        #         else:
        #             row_list.append(row_value)

        #         if col_value != ".":
        #             if col_value in sub_box_list[row//3][col//3]:
        #                 return False
        #             else:
        #                 sub_box_list[row//3][col//3].append(col_value)

        # return True
                    
                
                
                    
            
            
            
            
        