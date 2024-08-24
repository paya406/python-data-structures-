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
            self.count += 1

    #prints out the list
    def printList(self):
        currentNode = self.head
        print("head <==> ", end = "")
        
        while(currentNode):
            print(f"{currentNode.data} <==> ", end ="")
            currentNode = currentNode.next
        print("tail")


def main():
    #create new list

    myList = Dlist()

    #add to list
    for i in range(0, 6):
        myList.append(i)

    myList.printList()
    #test count attribute
    print(myList.count)
    


if __name__ == "__main__":
    main()


