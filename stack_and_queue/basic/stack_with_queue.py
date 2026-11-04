from utils.queue import Queue

# We need to maintain the internal queue like a stack for every push,
#   1. two_queues : Push all el from q1 into q2. Push x into q1. Move all el back back into q1.
#   2. one_queue, rotating at every push


# 2. Using 1 queue
class Stack_with_queue:
    def __init__(self) -> None:
        self.queue = Queue()

    def push(self, el):
        self.queue.push(el)
        for _ in range(len(self.queue) - 1):
            self.queue.push(self.queue.pop())

    def pop(self):
        return self.queue.pop()

    def top(self):
        return self.queue.top()

    def is_empty(self):
        return self.queue.is_empty()

    def __len__(self):
        return len(self.queue)
