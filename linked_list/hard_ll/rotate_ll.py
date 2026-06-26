from utils.linked_list import build_ll, print_ll


def reverse_ll(head, K=None):
    length = 0
    if K is None:
        K = float("inf")
    prev = None
    next_block = head
    while length < K and next_block:
        next = next_block.next
        next_block.next = prev
        prev = next_block
        next_block = next
        length += 1
    new_tail = head
    new_head = prev
    return new_head, new_tail, next_block, length


def rotate_ll_1(head, K):
    new_head, _, _, n = reverse_ll(head)
    K = K % n
    # right rotate
    # h1, t1, nxt_blk, _ = reverse_ll(new_head, K)
    # left rotate
    h1, t1, nxt_blk, _ = reverse_ll(new_head, n - K)
    h2, t2, _, _ = reverse_ll(nxt_blk)
    t1.next = h2
    return h1


def rotate_ll_2(head, K):
    n = 0
    curr = head
    tail = None
    while curr:
        n += 1
        tail = curr
        curr = curr.next
    K = K % n
    if K == 0:
        return head
    tail.next = head
    curr = head
    # rotate left
    for _ in range(K - 1):
        # rotate right
        # for _ in range(n - K - 1):
        curr = curr.next
    next = curr.next
    curr.next = None
    return next


arr = [1, 2, 3, 4, 5]
head = build_ll(arr)
K = 8
print_ll(head)
ans = rotate_ll_1(head, K)
print_ll(ans)
head = build_ll(arr)
ans = rotate_ll_2(head, K)
print_ll(ans)
