from collections import deque

class double_ended_queue:
    def __init__(self):
        self.d = deque()

    def append(self, x):
        self.d.append(x)

    def appendleft(self, x):
        self.d.appendleft(x)

    def pop(self):
        if self.d:
            return self.d.pop()
        else:
            return "Deque is empty"

    def popleft(self):
        if self.d:
            return self.d.popleft()
        else:
            return "Deque is empty"

    def extend(self, iterable):
        self.d.extend(iterable)

    def extendleft(self, iterable):
        self.d.extendleft(iterable)

    def remove(self, value):
        try:
            self.d.remove(value)
        except ValueError:
            return "Value not found"

    def clear(self):
        self.d.clear()

    def display(self):
        print(list(self.d))