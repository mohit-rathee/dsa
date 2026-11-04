from utils.linked_list import ListNode


class Queue_with_ll:
    def __init__(self) -> None:
        self.start = None
        self.end = None
        self.size = 0

    def push(self, el):
        next_node = ListNode(el)
        if self.end:
            self.end.next = next_node
        else:
            self.start = next_node

        self.end = next_node
        self.size += 1

    def pop(self):
        if self.size and self.start:
            first_el = self.start.val
            self.start = self.start.next
            self.size -= 1
            if self.start is None:
                self.end = None
            return first_el

    def top(self):
        if self.size and self.start:
            return self.start.val

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
