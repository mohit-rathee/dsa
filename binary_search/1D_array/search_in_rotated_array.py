def search_in_rotated_sorted_array(arr, k):
    print(arr, k)
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            return mid
        print(low, mid, high)

        # figure out which part is sorted
        # left = low to mid
        # not putting >= coz el are distinct
        if arr[low] <= arr[mid]:
            print("# left part is sorted")
            if arr[low] <= k < arr[mid]:
                print("# discard right side")
                high = mid - 1
            else:
                print("# discard left side")
                low = mid + 1
        # right = mid to high
        else:
            print("# right part is sorted")
            if arr[mid] < k <= arr[high]:
                print("# discard left side")
                low = mid + 1
            else:
                print("# discard right side")
                high = mid - 1
    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
k = 0
# arr = [4, 5, 6, 7, 0, 1, 2]
# k=3
ans = search_in_rotated_sorted_array(arr, k)
print("ans", ans)
