from insert_node_at_tail_of_linked_list import Insert

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None

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
    n = input()
    finalData = []
    for i in range(int(n)):
        x = input()
        if int(x) > 0:
            inp = input()
            data = inp.split(" ")
            new_data = []
            if len(data) > 0:
                new_data = [x for x in data if x != ""]
            if len(new_data) > 0:
                llist = LinkedList()
                createLinkedList(new_data, llist)
                # printLLInNormal(finalData, llist.head)
                sh = Insert(llist.head, 100)
                printLLInNormal(finalData, sh)
    
    for i in finalData:
        print(i)