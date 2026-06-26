from utils.linked_list import ListNode, build_ll, print_ll


def reverse_ll(head):
    prev = None
    curr = head
    while curr is not None:
        front = curr.next
        curr.next = prev
        prev = curr
        curr = front

    return prev


def add_2_numbers_in_ll(h1, h2):
    print_ll(h1)
    print_ll(h2)
    h1 = reverse_ll(h1)
    h2 = reverse_ll(h2)
    carry = 0
    dummy = ListNode(-1)
    result = dummy
    while h1 or h2 or carry:
        sum = carry
        if h1:
            sum += h1.val
            h1 = h1.next
        if h2:
            sum += h2.val
            h2 = h2.next

        value = sum % 10
        carry = sum // 10
        result.next = ListNode(value)
        result = result.next
    result = reverse_ll(dummy.next)
    return result


a1 = [1, 2, 3, 4]
a2 = [5, 6]
h1, h2 = build_ll(a1), build_ll(a2)
ans = add_2_numbers_in_ll(h1, h2)
print_ll(ans)
