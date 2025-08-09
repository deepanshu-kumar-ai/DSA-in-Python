import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def push(self, ele):
        heapq.heappush(self.queue, ele)

    def pop(self):
        if self.queue:
            return heapq.heappop(self.queue)
        else:
            return None

    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return None
