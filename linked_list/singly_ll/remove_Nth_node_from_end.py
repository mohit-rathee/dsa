from utils.linked_list import build_ll, print_ll


def remove_Nth_node_from_end(head, N):
    print_ll(head)
    slow = fast = head
    for _ in range(N):
        if fast.next:
            fast = fast.next
            N = N - 1
        else:
            if N == 0:
                return head.next
            print("N cannot exceed the len of linked list")
            return head
    print(slow.val, fast.val)
    while fast.next:
        fast = fast.next
        slow = slow.next
    print(slow.val, fast.val)
    slow.next = slow.next.next
    return head


arr = [1, 2, 3, 4, 5]
N = 5
head = build_ll(arr)
newHead = remove_Nth_node_from_end(head, N)
print_ll(newHead)
