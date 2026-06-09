def leaders_in_arr(arr):
    leaders = [arr[len(arr)-1]]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > leaders[-1]:
            leaders.append(arr[i])

    print(leaders[::-1])
    return leaders[::-1]


arr = [4, 7, 1, 0]
arr = [10, 22, 12, 3, 0, 6]
leaders_in_arr(arr)
