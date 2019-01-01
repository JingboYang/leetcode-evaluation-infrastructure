import heapq

class Item:

    def __init__(self, value, level):
        self.value = value
        self.popped = False
        self.level = level
    def __repr__(self):
        return '(val={}, lvl={}, pop={})'.format(self.value, self.level, self.popped)
    def __str__(self):
        return self.__repr__()
    def __eq__(self, other):
        return self.value == other.value and self.level == other.level
    def __lt__(self, other):
        
        if self.value == other.value:
            return self.level > other.level
        else:
            return self.value > other.value
            

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_heap = []
        self.level = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        temp = Item(x, self.level)
        self.stack.append(temp)
        heapq.heappush(self.max_heap, temp)
        self.level += 1

        print(self.stack)

    def pop(self):
        """
        :rtype: int
        """
        done = False
        while done is False:
            temp = self.stack.pop()
            if temp.popped is not True:
                temp.popped = True
                print(self.stack)
                return temp.value


    def top(self):
        """
        :rtype: int
        """
        while self.stack[-1].popped is True:
            self.stack.pop()

        return self.stack[-1].value


    def peekMax(self):
        """
        :rtype: int
        """
        print(self.max_heap)
        while self.max_heap[0].popped is True:
            heapq.heappop(self.max_heap)
        return self.max_heap[0].value
        

    def popMax(self):
        """
        :rtype: int
        """
        done = False
        while done is False:
            temp = heapq.heappop(self.max_heap)
            if temp.popped is not True:
                temp.popped = True
                print(self.stack)
                print(self.max_heap)
                return temp.value

modifier = ''
signature = 'class MaxStack:'
test_cases = None
input_string = """["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]
[[],[5],[1],[5],[],[],[],[],[],[]]
"""    
        