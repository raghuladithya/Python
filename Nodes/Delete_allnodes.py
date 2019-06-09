class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def deletelist(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

if __name__ == '__main__':
    llist = Linkedlist()
    llist.push(1)
    llist.push(2)
    llist.push(12)
    llist.push(3)
    print("Deleting Linkedlist")
    llist.deletelist()
    print('Linked list is deleted')
    
