from typing import List

class LinkedListNode:
    # a node is an object that has the val and pointer to the next node
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        # keep track of the head and tail node
        self.head = None
        self.tail = None

    # O(n) time | O(1) space
    def get(self, index: int) -> int:
        if index < 0:
            raise IndexError("Index must be non-negative")
        # iterate through the list
        # till ith indexed element
        currNode = self.head

        while index > 0 and currNode is not None:
            currNode = currNode.next
            index -= 1

        if currNode is None:
            raise IndexError("Index out of bounds")
        return currNode.val

    # O(1) time | O(1) space
    def insertHead(self, val: int) -> None:
        # insert a node with val at the head of the list
        node = LinkedListNode(val)
        # scenario 1 : list is empty 
        if self.head is None:
            self.head = node
            self.tail = node
            return
        # scenario 2 : list has elements        
        node.next = self.head
        self.head = node

    # O(1) time | O(1) space
    def insertTail(self, val: int) -> None:
        if self.tail is None: # list is empty
            self.insertHead(val)
            return
        
        node = LinkedListNode(val)
        # if list has elements
        self.tail.next = node
        self.tail = node
        
    # O(n) time | O(1) space
    def remove(self, index: int) -> bool:
        if index < 0:
            raise IndexError("Index must be non-negative")
        # iterate through till the ith node
        if self.head is None:
            return False
            
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True

        currNode = self.head
        prevNode = None
        while index > 0 and currNode is not None:
            prevNode = currNode
            currNode = currNode.next
            index -= 1

        if currNode is None:
            return False
        
        prevNode.next = currNode.next
        if currNode == self.tail:
            self.tail = prevNode
        
        return True
    
    # O(n) time | O(1) space
    def getValues(self) -> List[int]:
        # iterate through the list and store the values in the list
        # then just return the list
        values = [] # container to store the list values
        currNode = self.head
        while currNode is not None:
            values.append(currNode.val)
            currNode = currNode.next
        
        return values
