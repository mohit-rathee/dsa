from utils import linked_list as ll


def middle_of_ll(head):
    fast = slow = head
    while fast.next is not None:
        fast = fast.next
        # if fast.next:
        fast = fast.next if fast.next is not None else fast
        slow = slow.next

    ll.print_ll(head)
    print(slow.val)


arr = [1, 2, 3, 4, 5, 6]
linked_list = ll.build_ll(arr)
middle_of_ll(linked_list)
