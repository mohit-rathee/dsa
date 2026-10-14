class Solution:
    # queen = [row,col]
    def is_valid(self, row, col, columns, diag1,diag2):
        # print(queens, row, col, end="")
        if col in columns:
            # print("false")
            return False
        # upper-left diagonal check
        # upper-right diagonal check
        if row+col in diag1 :
            return False
        if row-col in diag2 :
            return False
        return True

    def place_in_row(self, row, columns,diag1,diag2):
        if row == self.n:
            # print("done")
            placement = []
            for index, queen_pos in enumerate(columns):
                q_col = queen_pos
                res_row = ["." for i in range(self.n)]
                res_row[q_col] = "Q"
                placement.append("".join(res_row))
            self.result.append(placement)
            return
        for col in range(self.n):
            # check if valid
            if self.is_valid(row, col, columns,diag1,diag2):
                columns.append(col)
                diag1.add(row+col)
                diag2.add(row-col)
                self.place_in_row(row + 1, columns,diag1,diag2)
                columns.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)
        # print(row, queens)

    def n_queen(self, n):
        self.n = n
        columns = []
        diag1 = set()
        diag2 = set()
        self.result = []
        self.place_in_row(0, columns,diag1,diag2)
        # print(n)
        for p in self.result:
            for r in p:
                for c in r:
                    print(c,end = ' ')
                print()
            print()
        return self.result


sol = Solution()
sol.n_queen(4)
