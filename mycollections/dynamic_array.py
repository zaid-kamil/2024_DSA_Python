import ctypes
import sys

class DArray:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array__(self.size)

    def __make_array__(self, capacity):
        # create a C type array with a fixed size (static, referential)
        return (capacity*ctypes.py_object)() 
    
    def __len__(self):
        return self.n
    
    def append(self, item):
        if self.n == self.size:
            self.__resize__(self.size * 2)
        self.A[self.n] = item
        self.n += 1
    
    def __resize__(self, new_capacity):
        temp_array = self.__make_array__(new_capacity)
        self.size = new_capacity
        # copy content from A to temp
        for i in range(self.n):
            temp_array[i] = self.A[i]
        # update A
        self.A = temp_array
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result += f"{self.A[i]},"
        return f"[{result[:-1]}]"    
    
    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        return "IndexError - Index out of bound"
    
    def pop(self):
        if self.n == 0:
            return "empty list"
        self.n -= 1
        return self.A[self.n]
    
    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "ValueError - value not is list"
    
    def insert(self, pos, item):
        if pos < 0:
            self.append(item)
            return
        if pos > self.n:
            self.append(item)
            return
        if self.size == self.n:
            self.__resize__(self.size*2)
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n += 1

    def __delitem__(self, pos):
        if 0 <=pos<self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1
    
    def remove(self, item):
        pos = self.find(item)
        if isinstance(pos, int):
            self.__delitem__(pos)
        else:
            print(pos)
    
    def extend(self, iter):
        pass

    def sort(self, reverse=False):
        pass

    def __repr__(self):
        pass

    def slice(self):
        pass

if __name__ == "__main__":
    a = DArray()
    a.append("hi")
    a.append(3)
    a.append(312)
    a.append(35)
    a.append(120)
    a.append(122)
    print(len(a))
    print(a)
    # print(a[1], a[0], a[2])
    # print(a.pop())
    # a.clear()
    print(a.find(312))
    a.insert(1, 1000)
    print(a)
    a.insert(3, 50)
    print(a)
    a.insert(15, 50)
    print(a)
    a.insert(15, 50)
    print(a)
    a.insert(15, 50)
    print(a)
    a.insert(-1, -1)
    print(a)
    del a[50]
    del a[50]
    print(a)
    del a[0]
    print(a)
    del a[1]
    print(a)
    a.remove('hi')
    print(a)
    a.remove(312)
    print(a)
    print(a.min())