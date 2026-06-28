from utils.linked_list import ListNode, build_ll, print_ll


def deep_print(head):
    print_ll(head)
    curr = head
    while curr:
        print(curr.val, "->", curr.random.val if curr.random else "None")
        curr = curr.next
    print()


def clone_ll(head):
    # add clone next to respective places
    curr = head
    while curr:
        next = curr.next
        val = curr.val
        # new_val = str(val) + '"'  # just for now
        new_val = val
        new_node = ListNode(new_val)
        # new_node.random = curr # just for now
        curr.next = new_node
        new_node.next = next
        curr = next
    curr = head
    # add linking
    while curr:
        next = curr.next.next
        cloned_node = curr.next
        cloned_random = curr.random.next if curr.random else None
        cloned_node.random = cloned_random
        curr = next
    # extract clones
    dummy = ListNode(-1)
    tail = dummy
    curr = head
    while curr:
        next = curr.next.next
        cloned_node = curr.next
        tail.next = cloned_node
        tail = tail.next
        curr.next = next
        curr = next
    return dummy.next


arr = [1, 2, 3, 4, 5, 6]

head = build_ll(arr)
# 1 -> 2
head.random = None
# 2 -> 1
head.next.random = head
# 3 -> 5
head.next.next.random = head.next.next.next.next
# 4 -> 1
head.next.next.next.random = head
# 5 -> 6
head.next.next.next.next.random = head.next.next.next.next.next
# 6 -> 6
head.next.next.next.next.next.random = head.next.next.next.next.next

deep_print(head)
ans = clone_ll(head)
deep_print(ans)
