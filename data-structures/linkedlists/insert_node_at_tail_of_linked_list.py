class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

def Insert(head, data):
    newNode = Node(data)
    tail = head
    if head == None:
        return newNode
    
    while tail.next != None:
        tail = tail.next
    
    tail.next = newNode
    return head

def printLLInNormal(finalData, head):
    if head == None:
        return None
    
    finalData.append(head.data)
    # print(head.data)
    printLLInNormal(finalData, head.next)

def createLinkedList(array_data, llist):
    array_data = array_data
    if len(array_data) <= 0:
        pass
        # return llist
    
    llist.head = Node(array_data[0])
    new_list = llist.head
    for i in array_data[1:]:
        temp = Node(i)
        new_list.next = temp
        new_list = new_list.next

if __name__ == "__main__":
    inp = input()
    inp = inp.split(" ")
    print(inp)