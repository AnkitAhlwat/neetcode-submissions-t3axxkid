class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
                
        n = len(board)
        sqrt_n = int(n ** 0.5)

        rows = [[False] * n for _ in range(n)]
        columns = [[False] * n for _ in range(n)]
        boxes = [[False] * n for _ in range(n)]

        for row in range(n):
            for column in range(n):
                value = board[row][column]
                if value == ".":
                    continue
                
                box_index = (row //3) * 3 + (column//3)
                room_index = ord(value) - ord('1')
                if rows[row][room_index] or columns[column][room_index] or  boxes[box_index][room_index]:
                    return False

                
                rows[row][room_index] = True
                columns[column][room_index] = True
                boxes[box_index][room_index] = True

        return True