from utils.linked_list import build_ll, print_ll


def reverse_ll(head):
    prev = None
    curr = head
    while curr is not None:
        front = curr.next
        curr.next = prev
        prev = curr
        curr = front

    return prev


def check_palindrome(head):
    fast = slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    second = reverse_ll(slow.next)
    slow.next = None
    first = head

    prev = None
    is_palindrome = True
    while second is not None:
        if first.val != second.val:
            is_palindrome = False
        # inc first
        first = first.next
        # inc second and reverse
        front = second.next
        second.next = prev
        prev = second
        second = front
    slow.next = prev
    print_ll(head)
    return is_palindrome


arr = [1, 2, 3, 3, 2, 1]
head = build_ll(arr)

ans = check_palindrome(head)
print(ans)
