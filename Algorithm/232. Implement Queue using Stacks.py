class MyQueue(object):

    def __init__(self):
        self.stPop = []
        self.stPush = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stPush.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.stPop.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stPop) == 0:
            while self.stPush:
                self.stPop.append(self.stPush.pop())
        return self.stPop[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stPush) + len(self.stPop) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()