def count_partition(arr, limit):
    subarr_count = 1
    subarr_total = 0
    for val in arr:
        if subarr_total + val <= limit:
            subarr_total += val
        else:
            subarr_count += 1
            subarr_total = val
    return subarr_count


def split_arr_largest_sum(arr, K):
    print(arr, K)
    low, high = max(arr), sum(arr)
    while low < high:
        mid = (low + high) // 2
        # print(low, mid, high)
        # check
        partition_count = count_partition(arr, mid)
        if partition_count <= K:
            # if we can have less partitions satisfing the conditions then splitting those partitions will still follow the max sum rule
            # print("valid")
            # valid ans
            high = mid
        else:  # res < K
            # print("invalid")
            low = mid + 1
    return low


arr = [1, 2, 3, 4, 5]
K = 3
arr = [3, 5, 1]
K = 3
ans = split_arr_largest_sum(arr, K)
print(ans)
