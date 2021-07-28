# 直接在push的时候把整个queue倒过来，变成stack的顺序，这样top就好写了，注意要用deque做
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        q = self.s
        q.append(x)
        for _ in range(len(q)-1):
            q.append(q.popleft())
            
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.s.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.s[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.s:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
