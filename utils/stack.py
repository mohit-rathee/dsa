class Stack:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self) -> str:
        return str(self.arr)

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        return self.arr.pop()

    def top(self):
        if len(self.arr) > 0:
            return self.arr[-1]
        else:
            return None

    def is_empty(self):
        if len(self.arr) == 0:
            return True
        return False
