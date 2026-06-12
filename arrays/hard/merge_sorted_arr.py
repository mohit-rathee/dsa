def merge_sorted_arr_without_space(a1, a2):
    [sm, lg] = [a1, a2] if len(a1) < len(a2) else [a2, a1]
    print(lg, sm)
    i = len(lg) - len(sm) - 1
    j = len(sm) - 1
    k = len(lg) - 1
    while j >= 0 and i >= 0:
        print(i, j)
        print(lg[i], sm[j])
        if lg[i] > sm[j]:
            # put lg[i] item in unused area
            lg[k] = lg[i]
            i -= 1
            k -= 1
        else:
            lg[k] = sm[j]
            j -= 1
            k -= 1
        print(lg, sm)
        print(i, j)
    if j >= 0:
        for i in range(j + 1):
            lg[i] = sm[i]
    print(lg, sm)
    print(i, j)


# arr1 = [-5, -2, 4, 5, 0, 0, 0]
# arr2 = [-3, 1, 8]

# arr1 = [0, 2, 0, 0]
# arr2 = [-1, 3]

arr1 = [0, 2, 7, 8, 0, 0, 0]
arr2 = [-7, -3, -1]
merge_sorted_arr_without_space(arr1, arr2)
