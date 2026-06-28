class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.child = None


class DoublyNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def build_ll(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next

    return head


def build_dll(arr):
    if not arr:
        return None

    head = DoublyNode(arr[0])
    curr = head

    for x in arr[1:]:
        node = DoublyNode(x)
        curr.next = node
        node.prev = curr
        curr = node

    return head


def to_list(head):
    ans = []

    while head:
        ans.append(head.val)
        head = head.next

    return ans


def print_ll(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next

    print("None")
