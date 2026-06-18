def capacity_to_ship_in_d_days(weights, days):
    print(weights, days)
    # edge case
    if days == 1:
        return sum(weights)
    if days >= len(weights):
        print("optimised")
        return max(weights)

    # min cap possible is max(weights)
    # max cap possible is sum(weights)
    low, high = max(weights), sum(weights)
    while low < high:
        mid = (low + high) // 2
        # check for mid capacity
        req_days = 1
        current_load = 0
        for weight in weights:
            if current_load + weight <= mid:
                current_load += weight
            else:
                req_days += 1
                current_load = weight
                if req_days > days:
                    break

        if req_days <= days:
            # mid in valid, and a potential ans
            high = mid
        else:
            # mid is not the ans, discard left
            low = mid + 1
    return low


weights = [5, 4, 5, 2, 3, 4, 5, 6]
day = 5
# weights = [1, 2, 3, 4, 5]
# day = 2
ans = capacity_to_ship_in_d_days(weights, day)
print(ans)
