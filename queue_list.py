class Queue:
    """
    This is the Python list implementation of a queue
    """
    def __init__(self):
        """
        Creates an empty queue.
        """
        self._items = list()

    def is_empty(self):
        """
        Returns True if the queue is empty or False otherwise.
        """
        return len(self) == 0

    def __len__(self):
        """
        Returns the number of items in the queue.
        """
        return len(self._items)

    def enqueue(self, item):
        """
        Adds the given item to the queue in the back.
        """
        self._items.append(item)

    def dequeue(self):
        """
        Removes and returns the first item in the queue.
        """
        return self._items.pop(0)
