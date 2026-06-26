from utils.linked_list import ListNode, build_ll, print_ll


def split_from_middle(head):
    # find a middle, (hare & tortoise)
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    right = slow.next
    slow.next = None
    left = head
    return left, right


def join_sorted_lists(left, right):
    dummy_node = ListNode(-1)
    tail = dummy_node
    while left and right:
        if left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
        tail = tail.next

    if left:
        tail.next = left
    else:
        tail.next = right

    return dummy_node.next


def sort_linked_list(head):
    if head is None or head.next is None:
        return head
    left, right = split_from_middle(head)
    left = sort_linked_list(left)
    right = sort_linked_list(right)
    new_head = join_sorted_lists(left, right)
    return new_head


arr = [4, 5, 6, 4, 5, 1]
head = build_ll(arr)
print_ll(head)
ans = sort_linked_list(head)
print_ll(ans)
