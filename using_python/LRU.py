class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dic:
            VAL = self.dic[key]
            del self.dic[key]
            self.dic[key] = val
            return val

        else：
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.dic:
            del self.dic[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
