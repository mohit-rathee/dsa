def at_most_k_distinct(s, k):
    left, res = 0, 0
    freq = {}

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        # substrings in current window
        res += right - left + 1
    return res


def count_substrings(s, k):
    return at_most_k_distinct(s, k) - at_most_k_distinct(s, k - 1)


s = "pqpqs"
k = 2

print(s)
print("Count:", count_substrings(s, k))  # Output: 7
