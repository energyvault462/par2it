
# taken mostly from Dallas Walker at https://www.youtube.com/watch?v=V1FIo9DCUdU
#  though changed his implementation so it's a queue (FiFO) instead of a stack
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print items,

