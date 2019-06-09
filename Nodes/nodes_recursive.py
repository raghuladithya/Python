class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def reverseutil(self,current,previous):
        if current.next is None:
            self.head = current
            current.next = previous
            return
        next = current.next
        current.next = previous
        self.reverseutil(next,current)

    def reverse(self):
        if self.head is None:
            return
        self.reverseutil(self.head, None)

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

llist = Linkedlist()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print ("Given linked list")
llist.printList()

llist.reverse()

print ("\n Reverse linked list")
llist.printList()
