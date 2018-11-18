import threadsafe

class Stack(threadsafe.Lockable):

    def __init__(self):
        super(Stack, self).__init__()
        self._data = list()

    @threadsafe.locked
    def push(self, obj):
        current_largest = max(obj, self.get_largest())
        self._data.append((obj, current_largest))

    @threadsafe.locked
    def pop(self):
        obj, _last_largest = self._data.pop(-1)
        return obj

    def _peek_head(self):
        if self._data:
            return self._data[-1]

    def peek(self):
        head = self._peek_head()
        if head:
            obj = head[0]
            return obj

    def get_largest(self):
        head = self._peek_head()
        if head:
            current_largest = head[1]
            return current_largest
