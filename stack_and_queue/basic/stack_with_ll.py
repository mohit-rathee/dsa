from utils.linked_list import ListNode


class Stack_with_ll:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, el):
        next_node = ListNode(el)
        next_node.next = self.head
        self.head = next_node
        self.size += 1

    def pop(self):
        if self.head and self.size:
            top_el = self.head.val
            self.head = self.head.next
            self.size -= 1
            return top_el

    def top(self):
        if self.head:
            return self.head.val

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
