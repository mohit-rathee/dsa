def kth_missing_number(vec, K):
    # vec should start from 1 to inf
    print(vec, K)
    n = len(vec)
    # check for last value EDGE CASE
    low, high = 0, n
    while low < high:
        mid = (low + high) // 2
        # print(low, mid, high)

        # i think kth missing number lies before mid
        expected_val = mid + 1
        actual_val = vec[mid]
        missing_elements = actual_val - expected_val
        if missing_elements >= K:
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
    print("low", low)
    print("high", high)

    return low + K


vec = [4, 7, 9, 10]
K = 9
# vec = [4, 7, 9, 10]
# K = 4
# vec = [1, 2, 4, 6]
# K = 2
ans = kth_missing_number(vec, K)
print(ans)
