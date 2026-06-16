def search_in_rotated_array_without_distinct_el(arr, k):
    print(arr, k)
    n = len(arr)
    low = 0
    high = n - 1
    count = 8
    while low <= high and count != 0:
        mid = (low + high) // 2
        if arr[mid] == k:
            return True
        if arr[low] == arr[mid] == arr[high]:
            print("low == mid == high")
            low += 1
            high -= 1
            continue
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
        count -= 1
    return False


arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6, 7]
num = 7
arr = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
num = 0
ans = search_in_rotated_array_without_distinct_el(arr, num)
print("ans", ans)
