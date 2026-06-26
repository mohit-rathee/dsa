from utils.linked_list import build_ll


def detect_loop_in_ll(head):
    fast = slow = head
    while fast.next:
        fast = fast.next
        if fast.next is not None:
            fast = fast.next
        else:
            return False
        slow = slow.next
        if slow == fast:
            return True


arr = [1, 2, 3, 4, 5, 6]
head = build_ll(arr)
curr = head
for i in range(4):
    curr = curr.next
curr.next = head

ans = detect_loop_in_ll(head)
print(ans)
