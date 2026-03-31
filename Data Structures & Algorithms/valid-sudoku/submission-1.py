class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
                
        n = len(board)
        sqrt_n = int(n ** 0.5)

        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for row in range(n):
            for column in range(n):
                value = board[row][column]
                if value == ".":
                    continue
                
                box_index = (row //3) * 3 + (column//3)
                
                if value in rows[row] or value in columns[column] or value in boxes[box_index]:
                    return False

                
                rows[row].add(value)
                columns[column].add(value)
                boxes[box_index].add(value)

        return True