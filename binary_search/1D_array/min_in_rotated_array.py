def minimum_in_rotated_arr(arr):  # elements are distinct
    print(arr)
    n = len(arr)
    low = 0
    high = n - 1
    minimum = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[high]:
            minimum = min(minimum, arr[low])
            break
        if arr[low] <= arr[mid]:
            # left part is sorted
            # update minimum with first of sorted part
            minimum = min(minimum, arr[low])
            # discard left part
            low = mid + 1
        else:
            # righ part is sorted
            # update minimum with first of sorted part
            minimum = min(minimum, arr[mid])
            # discard right part
            high = mid - 1
    return minimum


# arr = [4, 5, 6, 7, -26, 0, 1, 2, 3]
# arr = [1, 2, 3, 4, 5]
arr = [2, 3, 4, 5, 1]
ans = minimum_in_rotated_arr(arr)
print(ans)
