# 答案的做法，双向链表+hashmap/dictionary，O(1)复杂度
class ll():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    
    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def remove(self, node):
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv
    
    def move_to_head(self, node):
        self.remove(node)
        self.add(node)
        
    def pop_tail(self):
        ttail = self.tail.prev
        self.remove(ttail)
        return ttail

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = ll(0, 0), ll(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            nnode = ll(key, value)
            self.cache[key] = nnode
            self.add(nnode)
            self.size += 1
            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.val = value
            self.move_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 自己想的双向链表解法，不用dictionary，复杂度O(n)
# cache除了第一个节点，最左边是LRU，最右边是MRU
# cache是第一个节点为(0, 0)的双向链表，后面的节点是真正放入的有效节点，在进行放入、换位、判断是否超长的操作，需要时刻注意特殊情况
class ll():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = ll(0, 0)
        self.cap = capacity

    def get(self, key: int) -> int:
        pt = self.cache
        flg = 0
        while pt.next:
            if pt.key == key:
                pt.prev.next = pt.next
                pt.next.prev = pt.prev
                a = pt.val
                flg = 1
            pt = pt.next
        if pt.prev == None:
            return -1
        if pt.key == key:
            return pt.val
        if flg:
            pt.next = ll(key, a)
            pt.next.prev = pt
            return a
        return -1
    # def print(self):
    #     pt = self.cache
    #     res = []
    #     while pt:
    #         res.append((pt.key, pt.val))
    #         pt = pt.next
    #     print(res)
    def put(self, key: int, value: int) -> None:
        pt = self.cache
        n = 0
        while pt.next:
            n += 1
            if pt.key == key:
                pt.prev.next = pt.next
                pt.next.prev = pt.prev
                n -= 1
            pt = pt.next
        if self.cap == 1:
            self.cache.next = ll(key, value)
            self.cache.next.prev = self.cache
            return
        if pt.key == key:
            pt.prev.next = ll(key, value)
            pt.prev.next.prev = pt.prev
            return
        #n += 1
        if n == self.cap:
            self.cache.next = self.cache.next.next
            self.cache.next.prev = self.cache
        pt.next = ll(key, value)
        pt.next.prev = pt
        #self.print()
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

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
