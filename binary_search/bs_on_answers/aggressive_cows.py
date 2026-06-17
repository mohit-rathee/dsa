def canPlace(stalls, cows, d):
    # Place first cow at first stall
    count = 1
    lastPos = stalls[0]

    # Loop through stalls
    for i in range(1, len(stalls)):
        # If stall is at least d away from last placed cow
        if stalls[i] - lastPos >= d:
            # Place cow here
            count += 1
            # Update last position
            lastPos = stalls[i]
        # If all cows placed
        if count >= cows:
            return True
    # Could not place all cows
    return False


def aggressive_cows(stalls, K):
    stalls = sorted(stalls)
    print(stalls, K)
    ans = 0
    low = 1
    high = stalls[-1] - stalls[0]
    # last possible configuration
    while low <= high:
        mid = (low + high) // 2
        # print(low, mid, high)
        if canPlace(stalls, K, mid):
            ans = mid
            # print(mid, "is possible")
            low = mid + 1
        else:
            # print(mid, "is not possible")
            high = mid - 1
    return ans


stalls = [0, 3, 4, 7, 10, 9]
K = 4
ans = aggressive_cows(stalls, K)
print(ans)
