# skip duplicate elements
def update_var(arr, idx, val, inc=True):
    while arr[idx] == val and idx < len(arr):
        if inc:
            idx += 1
        else:
            idx -= 1
    return idx


def three_sum(arr, sum):
    print(arr)
    result = []
    arr = sorted(arr)
    i = 0
    i_val = None
    for i in range(len(arr)-2):
        # skip duplicate elements
        if arr[i] == i_val:
            continue
        # update new i value
        i_val = arr[i]

        # 2 pointer approach
        j = i+1
        k = len(arr)-1

        desired_num = sum-i_val
        print('for', i_val, 'desired_num', desired_num)

        while j < k:
            j_val = arr[j]
            k_val = arr[k]
            print(i_val, j_val, k_val)

            s = j_val + k_val
            if s < desired_num:
                # increase j
                j = update_var(arr, j+1, j_val, True)
            elif s > desired_num:
                # decrease k
                k = update_var(arr, k-1, k_val, False)
            else:
                # append to result
                result.append([i_val, j_val, k_val])
                break

        # incrementing i
        i = update_var(arr, i+1, i_val, True)
    print(result)


arr = [-1, -1, 0, 1, -4, 2, -1, -4, 2, 2, 2, 3, 5]
# p = [-1, -1, 0, 2, 1, -3]
three_sum(arr, 1)
