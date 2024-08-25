"""
Node: holds a unit of the linked list
prev: pointer to previous Node
next: pointer to next Node
data: holds information
"""

class Node:
    #constructor
    def __init__(self, data =None):
        self.data = data
        self.prev = None
        self.next = None

"""
DList: Doubly linked lists data structure
head: pointer to front of the list
tail: pointer to end of the list
count: keeps track of the number of nodes in the lists
"""

class Dlist:
    #constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    #adds to end of list
    def append(self,data):
        newNode = Node(data)
    
        #if list is empty
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.count +=1
        else:
            # if list is not empty 
            currentNode = self.tail
            currentNode.next = newNode
            newNode.prev = currentNode
            self.tail = newNode
            self.count += 1

    #prints out the list
    def printList(self):
        currentNode = self.head
        print("head <==> ", end = "")
        
        while(currentNode):
            print(f"{currentNode.data} <==> ", end ="")
            currentNode = currentNode.next
        print("tail")

    # genrator function
    def gen(self):
        currentNode = self.head
        while(currentNode != None):
            yield currentNode
            currentNode = currentNode.next

    # search function
    def search(self,target):
        for i in self.gen():
            if i.data == target:
                return True
        return False
    # adds an item to front
    def addToFront(self,data):
        newNode = Node(data)
        #if list is empty
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.count += 1
        else:
            # if list is not empty
            newNode.next = self.head
            self.head = newNode
            self.count += 1

    # add at given index
    def addAtIndex(self, data, index: int):
        # index checks
        assert index >= 0, "index can not be negative"
        assert index <= self.count, "index out of bounds"
        newNode = Node(data)
        #if index == 0
        if index == 0:
            self.addToFront(data)
            self.count += 1
    
        #if index = tail
        elif index == (self.count):
            self.append(data)
            self.count += 1
        else:
            #if index > 0
            currentNode = self.head
            for i in range(0, (index-1)):
                currentNode = currentNode.next
            
            currentNode.next.prev = newNode
            newNode.next = currentNode.next
            newNode.prev = currentNode
            currentNode.next = newNode
            
            self.count += 1 



def main():
    #create new list

    myList = Dlist()

    # adding to end of list
    for i in range(0, 6):
        myList.append(i)

    # add to front
    myList.addToFront(400)
    #test add at index
    myList.addAtIndex(45,7)
    myList.addAtIndex(800,2)
    #test print list 
    myList.printList()
    #test count attribute
    print(f"count = {myList.count}")
    #print head tail
    print(f"head = {myList.head.data}")
    print(f"tail = {myList.tail.data}")

    #test generator
    print("Generator test")
    for i in myList.gen():
        print(str(i.data) +" ", end = "")

    print()
    #search test
    print("search test")
    print(myList.search(3))
    print(myList.search(90))
    


if __name__ == "__main__":
    main()


