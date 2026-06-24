from utils.linked_list import build_ll, print_ll


def segregate_even_odd(head):
    even_head = odd_head = None
    even_tail = odd_tail = None
    curr = head
    while curr:
        next = curr.next
        curr.next = None
        if curr.val % 2 == 0:
            if even_head is None:
                even_head = curr
                even_tail = curr
            else:
                even_tail.next = curr
                even_tail = curr
            # print_ll(even_head)
        else:
            if odd_head is None:
                odd_head = curr
                odd_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = curr
            # print_ll(odd_head)
        curr = next
    if not even_head:
        return odd_head

    if not odd_head:
        return even_head

    even_tail.next = odd_head

    return even_head


arr = [1, 2, 3, 4, 5, 6]
head = build_ll(arr)

ans = segregate_even_odd(head)
print_ll(ans)
