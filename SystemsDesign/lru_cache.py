class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.d: return -1
        self.d[key] = self.d.pop(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d: self.d.pop(key)
        self.d[key] = value
        if len(self.d) > self.size:
            self.d.pop(next(iter(self.d)))