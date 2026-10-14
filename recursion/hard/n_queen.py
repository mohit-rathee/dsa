class Solution:
    # queen = [row,col]
    def is_valid(self, row, col, queens):
        # print(queens, row, col, end="")
        for queen_pos in queens:
            q_row, q_col = queen_pos
            # being in same row is immpossible
            # column check
            if q_col == col:
                # print("false")
                return False
            d_row = row - q_row
            # upper-left diagonal check
            d_col_ul = col - d_row
            # upper-right diagonal check
            d_col_ur = col + d_row
            if q_col == d_col_ur or q_col == d_col_ul:
                # print("false with diagonal")
                return False
        # print("turu")
        return True

    def place_in_row(self, row, queens):
        if row == self.n:
            # print("done")
            placement = []
            for queen_pos in sorted(queens):
                q_row, q_col = queen_pos
                res_row = ["." for i in range(self.n)]
                res_row[q_col] = "Q"
                placement.append("".join(res_row))
            self.result.append(placement)
            return
        for col in range(self.n):
            # check if valid
            if self.is_valid(row, col, queens):
                queens.add((row, col))
                self.place_in_row(row + 1, queens)
                queens.remove((row, col))
        # print(row, queens)

    def n_queen(self, n):
        self.n = n
        queens = set()
        self.result = []
        self.place_in_row(0, queens)
        # print(n)
        for p in self.result:
            for r in p:
                for c in r:
                    print(c,end = ' ')
                print()
            print()
        return self.result


sol = Solution()
sol.n_queen(9)
