def kth_missing_number(vec, K):
    # vec should start from 1 to inf
    print(vec, K)
    n = len(vec) - 1
    # check for last value EDGE CASE
    expected_val = n + 1 + K
    actual_val = vec[n]
    if not expected_val <= actual_val:
        expected_num = n + 1
        # req_diff = K
        return expected_num + K

    low, high = 0, n
    while low < high:
        mid = (low + high) // 2
        # print(low, mid, high)

        # i think kth missing number lies before mid
        expected_val = mid + 1 + K
        actual_val = vec[mid]
        if expected_val <= actual_val:
            # Kth missing number is on left side
            # print("valid")
            # print(expected_val,actual_val)
            high = mid
        else:
            # kth missing element is not in left side
            # discard left side
            # print("invalid")
            # print(expected_val,actual_val)
            low = mid + 1
    # return low

    expected_num = low + 1
    # req_diff = K
    return expected_num + K - 1


# vec = [4, 7, 9, 10]
# K = 9
# vec = [4, 7, 9, 10]
# K = 4
vec = [1, 2, 3, 5]
K = 1
ans = kth_missing_number(vec, K)
print(ans)
