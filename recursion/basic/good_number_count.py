class Solution:
    def __init__(self):
        self.even_count = 5  # 0,2,4,6,8
        self.prime_count = 4  # 2,3,5,7
        self.mod = 10**9 + 7

    def no_of_possibilities_until(self, i, n):
        # base case
        if i >= n:
            return 1

        if i % 2 == 0:
            return (
                self.even_count * self.no_of_possibilities_until(i + 1, n)
            ) % self.mod
        else:
            return (
                self.prime_count * self.no_of_possibilities_until(i + 1, n)
            ) % self.mod

    def count_good_numbers_brute_force(self, n):
        return self.no_of_possibilities_until(0, n)

    def count_good_numbers_optimal(self, n):
        even_indices_count = (n + 1) // 2
        odd_indices_count = n // 2
        # optimise it by using binary exponentiation
        return (
            self.even_count**even_indices_count * self.prime_count**odd_indices_count
        ) % self.mod


sol = Solution()
ans = sol.count_good_numbers_brute_force(40)
print(ans)
ans = sol.count_good_numbers_optimal(40)
print(ans)
