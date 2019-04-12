class Queue:
    def __init__(self):
        self.size = 0
        self.storage = list()

    def enqueue(self, item):
        if item not in self.storage:
            self.storage.append(item)
            self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(0)
        return None

    def len(self):
        return self.size
