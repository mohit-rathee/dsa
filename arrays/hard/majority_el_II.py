# Return all the elements > n//3
def majority_el_II(arr):
    el_1 = el_2 = 0
    cnt_1 = cnt_2 = 0
    for i in arr:
        if cnt_1 == 0 and el_2 != i:
            el_1 = i
            cnt_1 = 1
        elif cnt_2 == 0 and el_1 != i:
            el_2 = i
            cnt_2 = 1
        elif el_1 == i:
            cnt_1 += 1
        elif el_2 == i:
            cnt_2 += 1
        else:
            cnt_1 -= 1
            cnt_2 -= 1

    print(arr)
    print(el_1, el_2)
    # print(cnt_1, cnt_2)


arr = [1, 2, 1, 1, 3, 2]
majority_el_II(arr)
