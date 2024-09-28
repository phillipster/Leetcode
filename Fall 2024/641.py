import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()

class MyCircularDeque:  # Implementation for static-array-double-ended queue
    def __init__(self, k: int):
        self.max = k
        self.data = make_array(k)
        self.num_of_elems = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.num_of_elems

    def isEmpty(self):
        return len(self) == 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.data[0] = value
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.front_ind = (self.front_ind - 1) % len(self.data)
            self.data[self.front_ind] = value
            self.num_of_elems += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.data[0] = value
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.back_ind = (self.back_ind + 1) % len(self.data)
            self.data[self.back_ind] = value
            self.num_of_elems += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.isEmpty():
            self.front_ind = None
            self.back_ind = None
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        value = self.data[self.back_ind]
        self.data[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % len(self.data)
        self.num_of_elems -= 1
        if self.isEmpty():
            self.front_ind = None
            self.back_ind = None
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front_ind]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.back_ind]

    def isFull(self) -> bool:
        return self.num_of_elems == self.max


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(10)
param_1 = obj.insertFront(2)
param_2 = obj.insertLast(3)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()