def check_configuration(arr, M, K, days):
    bouquet_count = 0
    flower_count = 0
    for blooming_days in arr:
        is_bloomed = True if blooming_days <= days else False
        if is_bloomed:
            flower_count += 1
            if flower_count == K:
                bouquet_count += 1
                flower_count = 0
                if bouquet_count >= M:
                    return True
        else:
            flower_count = 0

    return False


def min_days_to_make_bouquets(arr, M, K):
    # edge case
    if len(arr) < M * K:
        return -1
    elif len(arr) == M * K:
        return max(arr)

    print(arr, M, K)
    low = min(arr)
    high = max(arr)
    while low < high:
        mid = (low + high) // 2
        res = check_configuration(arr, M, K, mid)
        if res:
            high = mid
        else:
            low = mid + 1
    return low


# arr = [7, 7, 7, 7, 13, 11, 12, 7]
# M,K = 2,3
# arr = [1, 10, 3, 10, 2]
# M,K = 3,2
arr = [7, 7, 7, 7, 7, 7, 11]
M, K = 3, 2
ans = min_days_to_make_bouquets(arr, M, K)
print(ans)
