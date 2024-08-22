"""
Node: structure to hold data 
data: holds data 
next: pointer to next variable
"""
class Node:
    #constructor
    def __init__(self,data):
        self.data = data 
        self.next = None

"""
SList: structure to hold liked list
head: pointer to start of list
"""
class Slist:
#constructor
    def __init__(self):
        self.head = None
        self.count = 0

        #adds to list
    def addNode(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.count += 1
        else:
            currentNode = self.head
            #traverse linked list
            while currentNode.next != None:
                currentNode = currentNode.next

            currentNode.next = newNode
            self.count += 1
    #adds node at index
    def addNodeI(self,data,index:int):
        assert index >= 0, "index cannot be negative"
        assert index <= self.count, "index out of bounds"
        newNode = Node(data)
        
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            self.count += 1
        else:
            currentNode = self.head
            for i in range(0, (index-1)):
                currentNode = currentNode.next

            newNode.next = currentNode.next
            currentNode.next = newNode
            self.count += 1
    # generator function
    def gen(self):
        currentNode = self.head
        while(currentNode != None):
            yield currentNode
            currentNode = currentNode.next

    #search function
    def search(self,item):
        for i in self.gen():
            if i.data == item:
                return True
            
        return False

        



def main():
    myList = Slist()

    for i in range(0,11):
        myList.addNode(i)

    myList.addNodeI(23,4)
    myList.addNodeI(56,0)
    myList.addNodeI(90,13)

    currentNode = myList.head
    for i in range(0,myList.count):
        print(f" {currentNode.data} =>",end ='')
        currentNode = currentNode.next
    print(" None")
    print(myList.count)
    print(myList.search(5))
    print(myList.search(100))

if __name__ == "__main__":
    main()
