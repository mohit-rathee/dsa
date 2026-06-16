def find_squart(x):
    low = 0
    high = x
    while low < high:
        mid = (low + high) // 2
        # print(low, mid, high)
        mid_square = mid * mid
        # print("mid_square", mid_square)
        if mid_square == x:
            return mid
        elif mid_square > x:
            high = mid - 1
        else:
            low = mid + 1
    return low


ans = find_squart(28)
print(ans)
