# You want to implement a queue that sorts items by a given priority and always returns
# the item with the highest priority on each pop operation.

import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1] # index refers to the item in the tuple


class Item:

    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return f'Item {self._name}'


if __name__ == '__main__':
    queue = PriorityQueue()

    queue.push(Item('foo'), 1)
    queue.push(Item('bar'), 5)
    queue.push(Item('buz'), 4)
    queue.push(Item('gro'), 1)

    print(queue.pop()) # bar expected
    print(queue.pop()) # buz expected
    print(queue.pop()) # foo expected
    print(queue.pop()) # gro expected
