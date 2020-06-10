# 在push的时候，先把现有的queue倒过来变成stack，append(x)，然后再倒回去变成新的queue
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        r = collections.deque()
        s = collections.deque()
        n = len(self.q)
        for i in range(n):
            r.append(self.q.pop())
        r.append(x)
        for j in range(n+1):
            s.append(r.pop())
        self.q = s
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.q.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.q:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
