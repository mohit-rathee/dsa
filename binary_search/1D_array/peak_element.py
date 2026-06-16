def peak_element(arr):
    print(arr)
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[mid + 1]:
            # a peak is on left side,including mid
            high = mid
        else:
            # a peak is on right side
            low = mid + 1
    return low


arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = peak_element(arr)
print(ans)
