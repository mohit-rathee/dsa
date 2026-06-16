def unique_in_sorted_arr(arr):
    print(arr)
    n = len(arr) - 1
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n] != arr[n - 1]:
        return arr[n]
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        # checking the pair
        if mid % 2 == 0:
            pair_idx = mid + 1
        else:
            pair_idx = mid - 1
        if arr[mid] == arr[pair_idx]:
            print("mid pair is in correct order")
            # unique element is not on left side
            low = mid + 1
        else:
            # checking for mid
            print("mid pair is not in correct order")
            # unique is on left side, discard right
            high = mid - 1


arr = [1, 1, 3, 4, 4]
ans = unique_in_sorted_arr(arr)
print(ans)
