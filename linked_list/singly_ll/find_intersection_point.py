from utils.linked_list import build_ll, print_ll


def get_len_of_2_ll(h1, h2):
    l1 = l2 = 0
    while h1 or h2:
        if h1:
            l1 += 1
            h1 = h1.next
        if h2:
            l2 += 1
            h2 = h2.next
    return l1 - l2


def find_intersection_by_optimal_1(h1, h2):
    diff = get_len_of_2_ll(h1, h2)
    if diff < 0:
        while diff != 0:
            h2 = h2.next
            diff += 1
    elif diff > 0:
        while diff != 0:
            h1 = h1.next
            diff -= 1
    while h1 and h1 != h2:
        h1 = h1.next
        h2 = h2.next
    if h1 == h2:
        return h1.val
    else:
        return -1


def find_intersection_by_optimal_2(h1, h2):
    d1, d2 = h1, h2
    while d1 != d2:
        d1 = h2 if d1 is None else d1.next
        d2 = h1 if d2 is None else d2.next
    return d1.val if d1 else -1


a1 = [1, 2, 3, 4, 5]
a2 = [6, 7, 8]
h1 = build_ll(a1)
h2 = build_ll(a2)
h2.next.next.next = h1.next.next
ans = find_intersection_by_optimal_1(h1, h2)
print(ans)
ans = find_intersection_by_optimal_2(h1, h2)
print(ans)
