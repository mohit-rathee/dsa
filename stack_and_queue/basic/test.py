from stack_and_queue.basic.queue_with_stack import Queue_with_statck
from stack_and_queue.basic.queue_with_ll import Queue_with_ll
from stack_and_queue.basic.stack_with_ll import Stack_with_ll
from stack_and_queue.basic.stack_with_queue import Stack_with_queue
from utils.queue import Queue
from utils.stack import Stack


class Solution:
    def __init__(self) -> None:
        self.stack_with_arr = Stack()
        self.stack_with_ll = Stack_with_ll()
        self.stack_with_queue = Stack_with_queue()

        self.queue_with_arr = Queue()
        self.queue_with_ll = Queue_with_ll()
        self.queue_with_stack = Queue_with_statck()

    def push(self, el):
        self.stack_with_arr.push(el)
        self.stack_with_ll.push(el)
        self.stack_with_queue.push(el)
        self.queue_with_arr.push(el)
        self.queue_with_ll.push(el)
        self.queue_with_stack.push(el)

    def pop(self):
        a = self.stack_with_arr.pop()
        b = self.stack_with_ll.pop()
        c = self.stack_with_queue.pop()
        d = self.queue_with_arr.pop()
        e = self.queue_with_ll.pop()
        f = self.queue_with_stack.pop()
        if a == b == c and d == e == f:
            print("Pass:", a, d)
        else:
            print("Fail")

    def top(self):
        a = self.stack_with_arr.top()
        b = self.stack_with_ll.top()
        c = self.stack_with_queue.top()
        d = self.queue_with_arr.top()
        e = self.queue_with_ll.top()
        f = self.queue_with_stack.top()
        if a == b == c and d == e == f:
            print("Pass:", a, d)
        else:
            print("Fail")

    def is_empty(self):
        a = self.stack_with_arr.is_empty()
        b = self.stack_with_ll.is_empty()
        c = self.stack_with_queue.is_empty()
        d = self.queue_with_arr.is_empty()
        e = self.queue_with_ll.is_empty()
        f = self.queue_with_stack.is_empty()
        if a == b == c and d == e == f:
            print("Pass:", a, d)
        else:
            print("Fail")

    def size(self):
        a = len(self.stack_with_arr)
        b = len(self.stack_with_ll)
        c = len(self.stack_with_queue)
        d = len(self.queue_with_arr)
        e = len(self.queue_with_ll)
        f = len(self.queue_with_stack)
        if a == b == c and d == e == f:
            print("Pass:", a, d)
        else:
            print("Fail")


sol = Solution()
sol.push(1)
sol.push(2)
sol.push(3)
sol.push(4)
sol.push(5)
sol.pop()  # 5 1
sol.pop()  # 4 2
sol.is_empty()  # False False
sol.push(100)
sol.pop()  # 100 3
sol.pop()  # 3 4
sol.pop()  # 2 5
sol.size()  # 1 1
sol.pop()  # 1 100
sol.pop()  # None None
sol.is_empty()  # True True
