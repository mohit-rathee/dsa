def merge_overlapping_subintervals(arr):
    print(arr)
    arr = sorted(arr, key=lambda x: x[0])
    print(arr)
    last_interval = arr[0]
    result = [last_interval]
    for i in range(1, len(arr)):
        interval = arr[i]
        s = interval[0]
        e = interval[1]
        le = last_interval[1]
        if le > s:
            last_interval[1] = max(e, le)
        else:
            result.append(arr[i])
            last_interval = arr[i]
    print(result)


arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_overlapping_subintervals(arr)
