def count_painters(boards, max_load):
    painter_count = 1
    painter_load = 0
    for board in boards:
        if painter_load + board <= max_load:
            painter_load += board
        else:
            painter_count += 1
            painter_load = board
    return painter_count


def painters_partition(boards, K):
    print(boards, K)
    low, high = max(boards), sum(boards)
    while low < high:
        mid = (low + high) // 2
        # check configuration
        req_painters = count_painters(boards, mid)
        if req_painters > K:
            # invalid
            low = mid + 1
        else:
            # valid
            high = mid
    return low


boards = [5, 5, 5, 5]
K = 2
# boards = [10, 20, 30, 40]
# K = 2
ans = painters_partition(boards, K)
print(ans)
