class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    # O(1) time
    def get(self, i: int) -> int:
        # assuming i index is valid
        return self.arr[i]

    # O(1) time
    def set(self, i: int, n: int) -> None:
        # assuming i index is valid
        self.arr[i] = n

    # O(1) time (Amortized)
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    # O(1) time
    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

    # O(n) time
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        self.newArr = [0] * self.capacity
        for i in range(self.size):
            self.newArr[i] = self.arr[i]
        self.arr = self.newArr

    # O(1) time
    def getSize(self) -> int:
        return self.size
    
    # O(1) time
    def getCapacity(self) -> int:
        return self.capacity