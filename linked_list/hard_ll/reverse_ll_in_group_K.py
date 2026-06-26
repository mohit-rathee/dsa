from utils.linked_list import ListNode, build_ll, print_ll


def get_Kth_node(head, K):
    if head is None:
        return None
    curr = head
    for _ in range(K - 1):
        if curr:
            curr = curr.next
        else:
            break
    return curr


def reverse_ll_in_group_size_K(head, K):
    print_ll(head)
    dummy_node = ListNode(-1)
    tail = dummy_node
    curr = head
    group_start = head
    kth_node = get_Kth_node(curr, K)
    while True:
        if kth_node:
            prev = None
            for _ in range(K):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            tail.next = prev
            tail = group_start
        else:
            tail.next = curr
            return dummy_node.next
        kth_node = get_Kth_node(curr, K)
        group_start = curr


arr = [1, 2, 3, 4, 5, 6]
head = build_ll(arr)
K = 2
head = reverse_ll_in_group_size_K(head, K)
print_ll(head)
