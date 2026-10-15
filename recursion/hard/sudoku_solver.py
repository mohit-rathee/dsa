from utils.matrix import printgrid


class Solution:
    def find_empty_cell(self, sudoku):
        # 9*9
        for x in range(len(sudoku)):
            for y in range(len(sudoku)):
                if sudoku[x][y] == ".":
                    return [x, y]
        return False

    def is_valid(self, sudoku, row, col, number):
        for i in range(len(sudoku)):
            if sudoku[row][i] == str(number):
                return False
            if sudoku[i][col] == str(number):
                return False

            # index of grid's first index
            grid_x = (row // 3) * 3
            grid_y = (col // 3) * 3

            dx = i // 3
            dy = i % 3

            nx = grid_x + dx
            ny = grid_y + dy
            if sudoku[nx][ny] == str(number):
                return False

        return True

    def find_ans(self, sudoku):
        # 1. find first empty #(optimize by choosing most crowded cell)
        # 2. place all possible values
        empty_cell = self.find_empty_cell(sudoku)
        if not empty_cell:
            # solution done
            return True

        x, y = empty_cell
        for number in range(1, 10):
            # check if number is valid or not
            if not self.is_valid(sudoku, x, y, number):
                continue
            # mark number
            sudoku[x][y] = str(number)
            # recurse
            result = self.find_ans(sudoku)
            if result:
                return True
            # unmark it
            sudoku[x][y] = "."

    def sudoku_solver(self, sudoku):
        printgrid(sudoku)
        self.find_ans(sudoku)
        printgrid(sudoku)
        pass


sol = Solution()
sudoku = [
    [
        ".",
        ".",
        ".",
        ".",
        ".",
        ".",
        "7",
        ".",
        ".",
    ],
    [
        "7",
        ".",
        "5",
        ".",
        ".",
        ".",
        "9",
        ".",
        ".",
    ],
    [
        ".",
        ".",
        ".",
        "9",
        "7",
        "5",
        "4",
        "3",
        "1",
    ],
    [
        "9",
        ".",
        ".",
        ".",
        "4",
        "1",
        ".",
        ".",
        "7",
    ],
    [
        ".",
        "5",
        ".",
        "8",
        ".",
        "7",
        "6",
        "4",
        ".",
    ],
    [
        ".",
        "7",
        ".",
        ".",
        "2",
        ".",
        ".",
        ".",
        ".",
    ],
    [
        ".",
        "4",
        ".",
        ".",
        ".",
        ".",
        ".",
        "6",
        "9",
    ],
    [
        "1",
        "6",
        ".",
        "4",
        "3",
        ".",
        ".",
        ".",
        ".",
    ],
    [
        ".",
        ".",
        ".",
        ".",
        "6",
        "2",
        "3",
        ".",
        "4",
    ],
]
sol.sudoku_solver(sudoku)
