def lower_bound(arr, x):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            high = mid
        else:
            low = mid + 1
    return low


def upper_bound(arr, x):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2

        if arr[mid] > x:
            high = mid
        else:
            low = mid + 1

    return low


def el_in_range(rang, el):  # (is_matched,is_bigger)
    # rang = (min,max)
    min, max = rang
    if el >= min and el <= max:
        return (True, True)
    elif el < min:
        return (False, True)
    else:
        return (False, False)


def findMedianSortedArrays(arr1, arr2):
    M = {}
    # print(arr1, arr2)
    n = len(arr1)
    m = len(arr2)
    total = m + n
    # print("total lenght is", total)
    median_pos = []
    if total % 2 == 0:
        median_pos.append((total // 2) - 1)
        median_pos.append(total // 2)
    else:
        median_pos.append(total // 2)
    # print("median at index", median_pos)

    median_sum = 0
    for pos in median_pos:
        # print("finding", pos)
        if pos in M:
            median_sum += M[pos]
            continue
        low, high = 0, n - 1
        is_found = False
        # BS on arr1
        # print("bs on arr1")
        while low <= high:
            mid = (low + high) // 2
            l_b = lower_bound(arr2, arr1[mid])
            u_b = upper_bound(arr2, arr1[mid])
            left_count = mid
            index_in_merged_arr = (l_b + left_count, u_b + left_count)
            # print("for", arr1[mid], mid)
            # print("lower_bound", l_b)
            # print("left_count", left_el_count)
            # print(
            #     "index",
            #     index_in_merged_arr,
            #     "(",
            #     l_b + left_count,
            #     u_b + left_count,
            #     ")",
            # )
            is_matched, is_bigger = el_in_range(index_in_merged_arr, pos)
            if is_matched:
                # print("==> found median ", arr1[mid])
                median_sum += arr1[mid]
                is_found = True
                break
            elif is_bigger:
                # print("valid")
                high = mid - 1
            else:
                # print("invalid")
                low = mid + 1

        if is_found:
            continue

        # print("not found in arr1")
        # print("bs on arr2")
        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            l_b = lower_bound(arr1, arr2[mid])
            u_b = upper_bound(arr1, arr2[mid])
            # print("for", arr2[mid])
            # print(low, mid, high)
            left_count = mid
            # print("lower_bound", l_b)
            # print("upper_bound", u_b)
            index_in_merged_arr = (l_b + left_count, u_b + left_count)
            # print("lower_bound", l_b)
            # print(
            #     "index",
            #     index_in_merged_arr,
            #     "(",
            #     l_b + left_count,
            #     u_b + left_count,
            #     ")",
            # )
            is_matched, is_bigger = el_in_range(index_in_merged_arr, pos)
            if is_matched:
                # print("==> found median ", arr2[mid])
                median_sum += arr2[mid]
                is_found = True
                break
            elif is_bigger:
                # print("valid")
                high = mid - 1
            else:
                # print("invalid")
                low = mid + 1
    median = median_sum / float(len(median_pos))
    return median


def brute_force(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        one = arr[n // 2]
        two = arr[(n // 2) - 1]
        return (one + two) / 2
    else:
        return float(arr[n // 2])


arr1 = [1, 2]
arr2 = [3, 4]
# arr1 = [1, 3]
# arr2 = [2, 4]
# arr1 = [2, 2, 4, 4]
# arr2 = [2, 2, 2, 4, 4]
ans = findMedianSortedArrays(arr1, arr2)
print(ans)
print(brute_force(arr1, arr2))
