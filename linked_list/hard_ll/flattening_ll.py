from utils.linked_list import ListNode, print_ll


def print_child_ll(head):
    while head:
        print(head.val, end=" -> ")
        head = head.child


def build_flatten_ll():
    # Main list
    head = ListNode(5)
    head.next = ListNode(10)
    head.next.next = ListNode(19)
    head.next.next.next = ListNode(28)

    # 5 -> 7 -> 8 -> 30
    curr = head
    curr.child = ListNode(7)
    curr.child.child = ListNode(8)
    curr.child.child.child = ListNode(30)

    # 10 -> 20
    curr = head.next
    curr.child = ListNode(20)

    # 19 -> 22 -> 50
    curr = head.next.next
    curr.child = ListNode(22)
    curr.child.child = ListNode(50)

    # 28 -> 35 -> 40 -> 45
    curr = head.next.next.next
    curr.child = ListNode(35)
    curr.child.child = ListNode(40)
    curr.child.child.child = ListNode(45)

    return head


def print_flatten_ll(head):
    curr = head
    while curr:
        print(curr.val, end="")
        child = curr.child
        while child:
            print(f" -> {child.val}", end="")
            child = child.child
        print()
        curr = curr.next


def merge_2_arrays(h1, h2):
    # h1 is child_list, h2 is linked_list
    dummy = ListNode(-1)
    tail = dummy
    while h1 and h2:
        if h1.val <= h2.val:
            tail.next = h1
            h1 = h1.child
            tail = tail.next
        else:
            tail.next = h2
            h2 = h2.next
            tail = tail.next
    while h1:
        tail.next = h1
        h1 = h1.child
        tail = tail.next
    while h2:
        tail.next = h2
        h2 = h2.next
        tail = tail.next
    return dummy.next


def flatten_ll(head):
    if head is None or head.next is None:
        dummy = ListNode(-1)
        tail = dummy
        curr = head
        while curr:
            tail.next = curr
            curr = curr.child
            tail = tail.next
        return dummy.next
    merged_ll = flatten_ll(head.next)
    return merge_2_arrays(head, merged_ll)


head = build_flatten_ll()
print_flatten_ll(head)
print()
ans = flatten_ll(head)
print_ll(ans)
