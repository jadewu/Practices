# OrderedDict可以很简单地解决问题
# key-value查找可以想到dictionary也就是hashmap
# 最少用的会被invalid，而且不能用记录使用次数的方式增加O(n)的遍历复杂度，所以想到ordered list
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
