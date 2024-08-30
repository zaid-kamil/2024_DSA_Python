class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
    
    def isEmpty(self):
        return self.top == None

    def pop(self):
        if self.isEmpty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def __str__(self):
        s = ""
        temp = self.top
        while temp!=None:
            s += f"{temp.data} "
            temp = temp.next
        return f"Stack: {s}"