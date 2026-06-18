def count_gas_station(positions, limit):
    gas_count = 0
    n = len(positions)
    for i in range(1, n):
        gap = positions[i] - positions[i - 1]
        req_gas_stations = int(gap / limit)
        if gap == limit * req_gas_stations:
            req_gas_stations -= 1
        gas_count += req_gas_stations

    return gas_count


def max_gap_btw_2_consecutive_gas_station(positions):
    max_dist = 0
    for i in range(1, len(positions)):
        gap = positions[i] - positions[i - 1]
        max_dist = max(max_dist, gap)
    return max_dist


def minimise_max_distance_btw_gas_stations(positions, K):
    print(positions, K)
    low = 0  # all gas stations are at same place
    high = max_gap_btw_2_consecutive_gas_station(positions)
    while high - low > 1e-6:
        mid = (low + high) / 2.0
        print(low, mid, high)
        # check for mid
        req_gas_stations = count_gas_station(positions, mid)
        if req_gas_stations > K:
            print("invalid")
            low = mid
        else:
            print("valid")
            high = mid
    return high


positions = [1, 2, 3, 4, 5]
K = 12
ans = minimise_max_distance_btw_gas_stations(positions, K)
print(ans)
