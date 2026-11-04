from utils.stack import Stack


# Two methods:
#   1. Cheap pop and costly Push: transfer and rotate.
#   2. Push is cheap, pop is costly: it needs 2 stacks (input,output)


class Queue_with_statck:
    def __init__(self) -> None:
        self.input = Stack()
        self.output = Stack()

    def push(self, el):
        self.input.push(el)

    def pop(self):
        if self.output.is_empty():
            while not self.input.is_empty():
                self.output.push(self.input.pop())

        return self.output.pop()

    def top(self):
        if self.output.is_empty():
            while not self.input.is_empty():
                self.output.push(self.input.pop())

        return self.output.top()

    def is_empty(self):
        return self.input.is_empty() and self.output.is_empty()

    def __len__(self):
        return len(self.input) + len(self.output)
        pass
