class Solution:
    def __init__(self) -> None:
        self.result = []

    def generate_valid_paranthesis_of_len(self, n, o, c, s):
        if len(s) == 2 * n:
            self.result.append(s)

        if o < n:
            # add open bracket
            # print("[", s, "]", "+ (  adding open brace")
            self.generate_valid_paranthesis_of_len(n, o + 1, c, s + "(")
        if c < o:
            # add close bracket
            # print("[", s, "]", "+ )  adding close brace")
            self.generate_valid_paranthesis_of_len(n, o, c + 1, s + ")")

    def generate_paranthesis(self, n):
        self.generate_valid_paranthesis_of_len(n, 0, 0, "")
        return self.result


sol = Solution()
ans = sol.generate_paranthesis(3)
print(ans)
