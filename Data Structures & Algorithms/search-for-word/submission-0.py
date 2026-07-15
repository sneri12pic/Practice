class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(row, col, moves):
            if moves > len(word):
                # Not valid
                return True
            if moves == len(word):
                return True

            if (
                row < 0 or row >= len(board)
                or col < 0 or col >= len(board[0])
                or board[row][col] != word[moves]
            ):
                return False

            letter = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row + 1, col, moves + 1)
                or dfs(row - 1, col, moves + 1)
                or dfs(row, col + 1, moves + 1)
                or dfs(row, col - 1, moves + 1)
            )
            # Restore it for another possible path
            board[row][col] = letter
            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False

            # i, j = 0, 0
            # cur = []
            # moves = 0

            # while j <= len(board[i]) and len(cur) < len(word):
            #     if board[i][j] == word[0]:
            #         # Append Head
            #         cur.append(board[i][j])
            #         moves += 1
                    
            #         if board[i+moves][j] == word[moves]:
            #             # Check Neighbours {i: 0 | i: 1 | i: 2}
            #             while board[i+moves][j] == word[moves] and moves < len(word): # mvs = 1 : 2nd letter
            #                 cur.append(board[i+moves][j])
            #                 moves += 1
            #             if moves == len(word): return True
            #         else:

            #         # Check Neighbours {j: 1 | j: 2 | j: 3 ...} <= len(word)
            #         while board[i][j+moves] in word[moves] and moves < len(word):
            #             cur.append(board[i][j+moves])
            #             moves += 1
            #     else:
            #         j += 1
                
