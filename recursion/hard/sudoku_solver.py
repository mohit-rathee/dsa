from utils.matrix import printgrid


# TODO: Optimize Sudoku solver by maintaining candidate sets
#       for every empty cell and updating only affected peers
#       when placing a number.
#       Implement an undo trail/log that records each candidate
#       removal and uses checkpoints to restore changes during
#       backtracking, without accidentally restoring invalid candidates.


class Solution:
    def find_best_cell_and_candidates(self, sudoku):
        best_cell = None
        best_candidates = None

        for row in range(9):
            for col in range(9):
                if sudoku[row][col] != ".":
                    continue

                candidates = self.get_candidates(sudoku, row, col)

                # Impossible branch: no candidate for this empty cell
                if not candidates:
                    return (row, col), set()

                # Keep the cell with the fewest candidates
                if best_candidates is None or len(candidates) < len(best_candidates):
                    best_cell = (row, col)
                    best_candidates = candidates

                    # Can't improve on one candidate
                    if len(best_candidates) == 1:
                        return best_cell, best_candidates

        # No empty cells remain
        if best_cell is None:
            return None

        return best_cell, best_candidates

    def get_candidates(self, sudoku, row, col):
        candidates = set(range(1, 10))

        for i in range(9):
            row_val = sudoku[row][i]
            if row_val != ".":
                candidates.discard(int(row_val))

            col_val = sudoku[i][col]
            if col_val != ".":
                candidates.discard(int(col_val))

            # Check the 3x3 subgrid
            nx = (row // 3) * 3 + i // 3
            ny = (col // 3) * 3 + i % 3

            grid_val = sudoku[nx][ny]
            if grid_val != ".":
                candidates.discard(int(grid_val))

        return candidates

    def find_ans(self, sudoku):
        selection = self.find_best_cell_and_candidates(sudoku)

        # No empty cells: solved
        if selection is None:
            return True

        cell, candidates = selection

        # Empty cell with no valid candidates: contradiction
        if not candidates:
            return False

        row, col = cell

        for number in candidates:
            sudoku[row][col] = str(number)

            if self.find_ans(sudoku):
                return True

            # Backtrack
            sudoku[row][col] = "."

        return False

    def sudoku_solver(self, sudoku):
        printgrid(sudoku)

        solved = self.find_ans(sudoku)

        if solved:
            printgrid(sudoku)
            return sudoku

        # print("No solution exists.")
        return None


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
