def divide_count_merge(arr, low, high):
    mid = (high + low) // 2
    if mid >= high:
        return 0
    count = 0
    count += divide_count_merge(arr, low, mid)
    count += divide_count_merge(arr, mid + 1, high)

    # low to mid & mid+1 to high is sorted
    temp = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        # inversion count should increment here
        if arr[i] > arr[j]:
            temp.append(arr[j])
            j += 1
            print(high, j)
            count += mid - i + 1
        else:
            temp.append(arr[i])
            i += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1
    for idx in range(low, high + 1):
        arr[idx] = temp[idx - low]
    return count


def count_inversion(arr):
    low = 0
    high = len(arr) - 1
    print(arr)
    count = divide_count_merge(arr, low, high)

    print(count)
    print(arr)


arr = [5, 4, 3, 2, 1]
count_inversion(arr)
