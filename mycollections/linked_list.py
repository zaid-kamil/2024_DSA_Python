class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        # empty linked list
        self.head = None
        self.n = 0 # number of nodes
    
    def __len__(self):
        return self.n
    
    def insert_head(self, value):
        new_node = Node(value) # create new node
        new_node.next = self.head # connect        
        self.head = new_node # update head
        self.n += 1 # increase node count
    
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            current = self.head
            while current.next !=None: # stop before end
                current = current.next
            current.next = new_node
        self.n += 1
    
    def insert_after(self, after, value):
        new_node = Node(value)
        current = self.head
        while current!=None:
            if current.data == after:
                break
            current = current.next
        if current!=None:
            new_node.next = current.next
            current.next = new_node
            self.n += 1
        else:
            print("item not found")

    def clear(self):
        self.head = None
        self.n = 0
    
    def delete_head(self):
        if self.head == None:
            return "Empty Linked List"
        self.head = self.head.next
        self.n -= 1
    
    def pop(self):
        if self.head == None:
            return "Empty Linked List"
        current = self.head
        if current.next == None:
            return self.delete_head()
        while current.next.next != None:
            current = current.next
        current.next = None
        self.n -= 1

    def remove(self, value):
        if self.head == None:
            return "Empty Linked List"
        current = self.head
        if current.data == value:
            return self.delete_head()
        while current.next !=None:
            if current.next.data == value:
                break
            current = current.next
        # if we reached the tail and item not found
        if current.next == None:
            return "Item not found"
        else:
            current.next = current.next.next
            self.n -= 1
        

    def __str__(self):
        current = self.head
        result = ''
        while current!=None: # stop at end
            result += f"{current.data} ➡️ "
            current = current.next
        return f"[{result[:-4]}]" # leave last 4 chars
    
    def __repr__(self) -> str:
        return self.__str__()

