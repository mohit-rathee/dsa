class Stack:
    def __init__(self):
        self.cap = 4  # inspired from python lists
        self.arr = [None] * self.cap
        self.end = -1

    def resize_by(self, factor):
        new_size = self.cap * factor
        new_arr = [None] * new_size
        for idx, el in enumerate(self.arr):
            new_arr[idx] = el
        self.arr = new_arr
        self.cap = new_size

    def push(self, element):
        next_pos = self.end + 1
        if next_pos >= self.cap:
            # resize
            self.resize_by(2)

        self.arr[next_pos] = element
        self.end = next_pos

    def pop(self):
        if self.end >= 0:
            top_el = self.arr[self.end]
            self.end -= 1
            return top_el

    def top(self):
        if self.end >= 0:
            return self.arr[self.end]

    def is_empty(self):
        return self.end == -1

    def __len__(self):
        return self.end + 1
