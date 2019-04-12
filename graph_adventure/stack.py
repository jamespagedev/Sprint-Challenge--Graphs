class Stack:
    def __init__(self):
        self.size = 0
        self.storage = list()

    def push(self, item):
        if item not in self.storage:
            self.storage.append(item)
            self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        return None

    def remove(self, room_id):
        if self.size > 0:
            self.size -= 1
            del self.storage[self.storage.index(room_id)]

    def len(self):
        return self.size
