def count_no_of_rotation_in_sorted_arr1(arr):
    print(arr)
    low, high = 0, len(arr) - 1

    if arr[low] <= arr[high]:
        return 0  # not rotated

    while low <= high:
        mid = (low + high) // 2

        # found pivot
        if mid < high and arr[mid] > arr[mid + 1]:
            left_rotation = mid + 1
            _right_rotation = len(arr) - 1 - mid
            # return min(left_rotation, _right_rotation)
            return left_rotation

        # left half sorted
        if arr[low] <= arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def minimum_in_rotated_arr(arr):  # elements are distinct
    print(arr)
    n = len(arr)
    low = 0
    high = n - 1
    minimum = float("inf")
    min_idx = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[high]:
            if minimum > arr[low]:
                minimum = arr[low]
                min_idx = low
                break
        if arr[low] <= arr[mid]:
            # left part is sorted
            # update minimum with first of sorted part
            if minimum > arr[low]:
                minimum = arr[low]
                min_idx = low
            # discard left part
            low = mid + 1
        else:
            # righ part is sorted
            # update minimum with first of sorted part
            if minimum > arr[mid]:
                minimum = arr[mid]
                min_idx = mid
            # discard right part
            high = mid - 1
    return min_idx


def count_no_of_rotation_in_sorted_arr2(arr):
    min_idx = minimum_in_rotated_arr(arr)
    left_rotation = min_idx
    _right_rotation = len(arr)-min_idx
    return left_rotation
    # return min(left_rotation,_right_rotation)


# arr = [4, 0, 1, 2, 3]
arr = [2, 3, 4, 5, 1]
# arr = [1, 2, 3]
ans = count_no_of_rotation_in_sorted_arr1(arr)
print(ans)
ans = count_no_of_rotation_in_sorted_arr2(arr)
print(ans)
