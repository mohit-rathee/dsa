def expand(s, left, right):
    n = len(s)
    has_entered_loop = False
    while left > -1 and right < n and s[left] == s[right]:
        has_entered_loop = True
        left -= 1
        right += 1
    # print(right - left + 1, [left, right])
    if has_entered_loop:
        left += 1
        right -= 1
        return right - left + 1, [left, right]
    else:
        return 0, [left, right]


def longest_palindrom(s):
    n = len(s)
    m_len = 0
    m_idx = [0, 0]
    for i in range(n):
        e_len, e_idx = expand(s, i - 1, i + 1)
        o_len, o_idx = expand(s, i, i + 1)

        if e_len > m_len:
            m_len = e_len
            m_idx = e_idx
        if o_len > m_len:
            m_len = o_len
            m_idx = o_idx

        left, right = m_idx
    return s[left : right + 1]


string = "abcdcbeeeebcdcba"
ans = longest_palindrom(string)
print(ans)
