class Solution:
    def generate_binary_str_without_consecutive_1_of_len_n(self, n):
        if n == 0:
            return []
        if n == 1:
            return ["0", "1"]
        else:
            binaries = self.generate_binary_str_without_consecutive_1_of_len_n(n - 1)
            result = []
            for binary in binaries:
                if binary[-1] == "0":
                    result.append(binary + "1")
                result.append(binary + "0")
            return result

    def helper(self, n):
        if n == 1:
            return (1, 1)
        else:
            prev_zeros, prev_ones = self.helper(n - 1)
            zeros = prev_zeros + prev_ones
            ones = prev_zeros
            return (zeros, ones)

    def count_binary_str_without_consecutive_1_of_len_n(self, n):
        if n == 0:
            return 0

        zeros, ones = self.helper(n)
        return zeros + ones


sol = Solution()
n = 6
ans = sol.generate_binary_str_without_consecutive_1_of_len_n(n)
print(ans)
print(len(ans))
ans = sol.count_binary_str_without_consecutive_1_of_len_n(n)
print(ans)
