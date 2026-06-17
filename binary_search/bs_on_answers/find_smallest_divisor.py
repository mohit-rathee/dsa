import math


def find_smallest_divisor(arr, K):
    print(arr, K)
    if len(arr) > K:
        return -1

    low, high = 1, max(arr)
    while low < high:
        mid = (low + high) // 2
        # check this value
        res = 0
        for i in arr:
            res += math.ceil(i / mid)
            if res > K:
                break
        if res <= K:
            high = mid
        else:
            low = mid + 1
    return low


arr = [1, 2, 3, 4, 5]
K = 8
arr = [8, 4, 2, 3]
K = 10
ans = find_smallest_divisor(arr, K)
print(ans)
