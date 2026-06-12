def longest_subarray_sum_0(arr, k):
    print(arr, k)
    prefix_sum = {}
    longest_count = 0
    sum = 0
    for idx, num in enumerate(arr):
        sum += num
        if sum == k:
            longest_count = max(longest_count, idx + 1)

        desired_sum = sum - k

        if desired_sum in prefix_sum:
            subarray_count = idx - prefix_sum[sum]
            longest_count = max(longest_count, subarray_count)
        else:
            prefix_sum[sum] = idx
    print(longest_count)


# arr = [9, -3, 3, -1, 6, -5]
arr = [6, -2, 2, -8, 1, 7, 4, -10]
sum = 0
longest_subarray_sum_0(arr, sum)
