class Queue:
    def __init__(self) -> None:
        self.cap = 4  # inspired from python
        self.arr = [None] * self.cap
        self.start = -1
        self.end = -1
        self.size = 0

    def resize_by(self, factor):
        new_cap = self.cap * factor
        new_arr = [None] * new_cap
        for offset in range(self.size):
            idx = (self.start + offset) % self.cap
            new_idx = 0 + offset  # new_start = 0
            new_arr[new_idx] = self.arr[idx]

        self.arr = new_arr
        self.cap = new_cap
        self.start = 0
        self.end = self.size - 1

    def push(self, el):
        if self.size >= self.cap:
            self.resize_by(2)

        if self.size == 0:
            self.start = self.end = 0
        else:
            self.end = (self.end + 1) % self.cap

        self.arr[self.end] = el
        self.size += 1

    def pop(self):
        if self.size > 0:
            first_el = self.arr[self.start]
            self.arr[self.start] = None
            self.start = (self.start + 1) % self.cap
            self.size -= 1
            if self.size == 0:
                self.start = self.end = -1
            return first_el

    def top(self):
        if self.size > 0:
            return self.arr[self.start]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
