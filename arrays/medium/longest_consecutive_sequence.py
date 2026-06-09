def longest_consecutive_sequence(arr):
    s = set()
    for i in arr:
        s.add(i)
    print(s)
    longest = count = 0
    for num in s:
        if num-1 not in s:
            count = 1
            while num+1 in s:
                count += 1
                num += 1
            longest = max(longest, count)
    print(longest)
    return longest


arr = [100, 4, 200, 1, 3, 2]
longest_consecutive_sequence(arr)
