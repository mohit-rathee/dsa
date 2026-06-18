# arr1 = [1,2]          smaller
# arr2 = [3,4,5]        bigger
# merged_arr =  [first K elements]| [  rest of arr  ]
# merged_arr =  [part of smaller] | [rest of bigger ]
#               [part of bigger]  | [rest of smaller]
#
# merged_arr =     [x elements]   | [ n-x elements  ]
#                 [K-x elements]  | [ m-x elements  ]
# find x? (from low=0 to high=n)
# how to apply binary??
#
# merged_arr =      [*,*,*,leftA] | [rightA,*,*,*]
#                   [*,*,*,leftB] | [rightB,*,*,*]
#
# valid configuration will always satisfy:
#       leftA < rightB and leftB < rightA
# right side configuration will folow:
#       leftA > rightB
# left side configuration will folow:
#       rightA > leftB


def median_of_2_sorted_arr(a1, a2):
    n = len(a1)
    m = len(a2)

    print(a1, a2)
    sm, lg = [a1, a2] if n < m else [a2, a1]
    n, m = len(sm), len(lg)

    # if even then find el at median and (median+1)
    # if odd just find el at median
    median = (n + m) // 2
    K = median
    # split by median
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        # now config is
        #  {sm[:mid]}  |  {sm[mid:]}
        # {lg[:K-mid]} | {lg[K-mid:]}
        leftA = sm[mid - 1] if mid > 0 else float("-inf")
        rightA = sm[mid] if mid < n else float("inf")
        leftB = lg[K - mid - 1] if K - mid > 0 else float("-inf")
        rightB = lg[K - mid] if K - mid < m else float("inf")

        if leftB <= rightA and leftA <= rightB:
            if (n + m) % 2 == 0:
                left_el = max(leftA, leftB)
                right_el = min(rightA, rightB)
                median = (left_el + right_el) / 2
                return median
            else:
                right_el = min(rightA, rightB)
                return float(right_el)
        elif leftA > rightB:
            # K is too right
            high = mid - 1
        else:
            # K is too left
            low = mid + 1


arr1 = [1, 2]
arr2 = [3, 4]
ans = median_of_2_sorted_arr(arr1, arr2)
print(ans)
