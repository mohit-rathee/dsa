from utils.linked_list import build_ll


def find_starting_point_and_loop_len(head):
    # curr = head
    # for i in range(6):
    #     print(curr.val, end=" -> ")
    #     curr = curr.next
    # print()
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # print(slow.val, fast.val)
        if slow == fast:
            break
    if fast is None:
        print("no loop found")
        return -1, -1
    # else:
    first = head
    second = slow
    meeting_point = slow
    loop_len = 0
    while first != second:
        first = first.next
        second = second.next
        loop_len += 1
    while second != meeting_point:
        second = second.next
        loop_len += 1

    return first.val, loop_len


arr = [1, 2, 3, 4, 5, 6, 7]
head = build_ll(arr)
head.next.next.next.next.next.next.next = head.next.next
starting_point, loop_len = find_starting_point_and_loop_len(head)
print(starting_point, loop_len)
