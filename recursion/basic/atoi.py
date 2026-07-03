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
        # count number
        ans = self.helper(s, i, 0)
        # handle number
        ans *= sign
        # handle 32-bit int-overflow
        ans = max(-2147483648, ans)
        ans = min(2147483648, ans)
        print(ans)
        return ans


sol = Solution()
sol.atoi("   2147483648222    ")
sol.atoi("   22    ")
sol.atoi("-")
sol.atoi("+")
