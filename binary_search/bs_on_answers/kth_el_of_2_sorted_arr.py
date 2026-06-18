def kth_el_2_sorted_arr(a1, a2, K):
    n = len(a1)
    m = len(a2)

    print(a1, a2)
    sm, lg = [a1, a2] if n < m else [a2, a1]
    n, m = len(sm), len(lg)

    # split by median
    low, high = max(0, K - m), min(K, n)
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
            left_el = max(leftA, leftB)
            return left_el
        elif leftA > rightB:
            # K is too right
            high = mid - 1
        else:
            # K is too left
            low = mid + 1


arr1 = [1, 2, 3, 9]
arr2 = [4, 5, 6, 7, 18]
K = 8
ans = kth_el_2_sorted_arr(arr1, arr2, K)
print(ans)
