class Solution:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return self.pow(1 / x, -n)
        if n > 0:
            if n % 2 == 0:
                return self.pow(x * x, n // 2)
            else:
                return x * self.pow(x, n - 1)


sol = Solution()
ans = sol.pow(2, -2)
print(ans)
ans = sol.pow(2, 10)
print(ans)
ans = sol.pow(2, -10)
print(ans)
