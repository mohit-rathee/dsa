def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += right - (mid + 1)
    return cnt


def divide_count_merge(arr, low, high):
    mid = (low + high) // 2
    if mid >= high:
        return 0
    count = 0
    # divided
    count += divide_count_merge(arr, low, mid)
    count += divide_count_merge(arr, mid + 1, high)
    count += countPairs(arr, low, mid, high)
    # count and merge
    temp = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        # i<j && arr[i] > 2*arr[j]
        if arr[i] > arr[j]:
            temp.append(arr[j])
            j += 1
        else:
            temp.append(arr[i])
            i += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1
    for idx in range(len(temp)):
        arr[low + idx] = temp[idx]
    return count


def count_reverse_pair(arr):
    # a reverse pair is
    # i<j && arr[i] > 2*arr[j]
    print(arr)
    print(divide_count_merge(arr, 0, len(arr) - 1))
    print(arr)


# arr = [1, 3, 2, 3, 1]
arr = [3, 2, 1, 4]

count_reverse_pair(arr)
