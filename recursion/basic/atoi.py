class Solution:
    def helper(self, s, i, num):
        # base case
        if i >= len(s) or not s[i].isdigit():
            return num

        num = num * 10 + int(s[i])
        num = self.helper(s, i + 1, num)

        return num

    def atoi(self, s):
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        if i == len(s):
            return 0

        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            sign = 1
            i += 1

        ans = self.helper(s, i, 0)
        ans *= sign
        print(ans)
        return ans


sol = Solution()
sol.atoi("   00001234560    ")
sol.atoi("   22    ")
sol.atoi("-")
sol.atoi("+")
