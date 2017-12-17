class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def hasNext(self):
        return self.next != None

class singleLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def insertAtTheBeginning(self, data):
        """
        insertAtTheBeginning : Inserts New Node at the Beginning of Linked List
        """
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertAtTheEnd(self, data):
        """
        insertAtTheEnd : Inserts New Node at the End of Linked List
        """
        newNode = Node(data)
        current = self.head
    
        if current == None:
            self.head = newNode
        
        while current.next != None:
            current = current.next
        
        current.next = newNode
        self.length += 1

    def insertNodeInMiddle(self, pos, data):
        """
        insertNodeInMiddle : Inserts New Node in the Middle of Linked List
        """
        if pos > self.length or pos < 0:
            return None

        if pos == 0:
            self.insertAtTheBeginning(data)
        elif pos == self.length:
            self.insertAtTheEnd(data)
        else:
            newNode = Node(data)
            current = self.head
            count = 1
            while count < pos - 1:
                count += 1
                current = current.next
            newNode.next = current.next
            current.next = newNode
            self.length += 1    

    def deleteNodeAtBeginning(self):
        """
        deleteNodeAtBeginning : Deletes Node at the Beginning of Linked List
        """
        if self.length == 0:
            return None
        self.head = self.head.next
        self.length -= 1
    
    def deleteNodeAtEnd(self):
        """
        deleteNodeAtEnd : Deletes Node at the End of Linked List
        """
        current = self.head
        previous = self.head
        if current == None:
            return None
        
        while current.next != None:
            previous = current
            current = current.next

        previous.next = None
        self.length -= 1
    
    def deleteNodeInBetweenByPos(self, pos):
        """
        deleteNodeInBetweenByPos : Deletes Node at a given Possition in Linked List
        """
        if pos < 0 or pos > self.length:
            return None
        
        if pos == 1:
            self.head = self.head.next

        current = self.head
        previous = current
        count = 1
        while count < pos and current.next != None:
            count += 1
            previous = current
            current = current.next
        
        previous.next = current.next
        self.length -= 1

    def deleteNodeByValue(self, data):
        """
        deleteNodeByValue : Deletes Node with a given value in Linked List
        """
        if self.head == None:
            return 
        count = 1
        current = self.head
        previous = self.head
        
        while count < self.length and current.next != None:
            count += 1
            if current.data == data:
                previous.next = current.next
                self.length -= 1
                break
                return
            
            previous = current
            current = current.next
        
        return 
        
        return "Sorry!, Data Not Found "

    def getLength(self):
        current = self.head
        count = 0
        if current == None:
            return count
        
        while current != None:
            count += 1
            current = current.next

        return count
    
    def printList(self):
        current = self.head
        if current == None:
            return
        while current != None:
            print(current.data)
            current = current.next
        

if __name__ == "__main__":        
    sll = singleLinkedList()
    sll.insertAtTheBeginning(1)
    sll.insertAtTheBeginning(2)
    sll.insertAtTheBeginning(3)
    sll.insertAtTheBeginning(4)
    sll.insertAtTheEnd(1)
    sll.insertAtTheEnd(2)
    sll.insertAtTheEnd(3)
    sll.insertAtTheEnd(4)
    sll.insertAtTheEnd(5)
    sll.insertNodeInMiddle(2, 10)
    sll.insertNodeInMiddle(4, 20)
    sll.insertNodeInMiddle(50, 100)
    print(sll.printList())
    sll.deleteNodeAtBeginning()
    print(sll.printList())
    sll.deleteNodeInBetweenByPos(2)
    print(sll.printList())
    sll.deleteNodeByValue(3)
    print(sll.printList())