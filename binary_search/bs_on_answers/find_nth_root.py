def find_nth_root(N, M):
    low = 0
    high = M
    while low <= high:
        mid = (low + high) // 2
        # mid^
        res = 1
        for _ in range(N):
            res *= mid
            if res > M:
                break
        if res == M:
            return mid
        elif res > M:
            high = mid - 1
        else:
            low = mid + 1
    return -1

ans = find_nth_root(4, 81)
print(ans)
