# skip duplicate elements
def update_var(arr, idx, val, inc=True):
    while 0 <= idx < len(arr) and arr[idx] == val:
        if inc:
            idx += 1
        else:
            idx -= 1
    return idx


def four_sum(arr, sum):
    print(arr)
    result = []
    arr = sorted(arr)
    i_val = None
    for i in range(len(arr) - 3):
        # skip duplicate elements
        if arr[i] == i_val:
            continue
        # update new i value
        i_val = arr[i]
        j_val = None

        for j in range(i + 1, len(arr)):
            # skip duplicate elements
            if arr[j] == j_val:
                continue
            j_val = arr[j]
            desired_num = sum - i_val - j_val

            p = False
            if i_val == -2 and j_val == -1:
                p = True
            # 2 pointer approach
            k = j + 1
            l = len(arr) - 1
            while k < l:
                k_val = arr[k]
                l_val = arr[l]
                s = k_val + l_val

                # print('for', i_val, j_val, 'desired_num', desired_num)

                if s < desired_num:
                    # increase k
                    k = update_var(arr, k + 1, k_val, True)
                elif s > desired_num:
                    # decrease k
                    l = update_var(arr, l - 1, l_val, False)
                else:
                    # append to result
                    result.append([i_val, j_val, k_val, l_val])
                    k = update_var(arr, k + 1, k_val, True)
                    l = update_var(arr, l - 1, l_val, False)

    print(result)


def four_sum_hashmap(arr, sum):
    result = set()
    for i in range(len(arr) - 2):
        i_val = arr[i]

        for j in range(i + 1, len(arr)):
            j_val = arr[j]
            hashset = set()

            for k in range(j + 1, len(arr)):
                k_val = arr[k]

                l_val = sum - i_val - j_val - k_val
                # print(i_val, j_val, k_val, 'needs ', desired_num)
                if l_val in hashset:
                    res = sorted([i_val, j_val, k_val, l_val])
                    result.add(tuple(res))
                hashset.add(k_val)
    print(list(result))


arr = [-1, -1, 0, 1, -4, 2, -1, -4, 2, 2, 2, 3, 5]
# arr = [-1, -1, 1, 0, 2, 1, -3]
# arr = [1, 0, -1, 0, -2, 2]
# arr = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]

sum = 9
four_sum(arr, sum)
four_sum_hashmap(arr, sum)
