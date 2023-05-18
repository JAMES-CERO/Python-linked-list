class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference

node1 = Node(5)
print(node1.data)

node2 = Node(11)
node1.reference = node2
print(node1.reference)

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def print_linked_list(self):
        if self.head is None:
            print( 'The linked list is empty')
        else:
            c_node = self.head 
            while c_node is not None:
                print(c_node.data)
                c_node = c_node.reference

    def add_to_start(self, data):
        n_node = Node(data)
        n_node.reference = self.head
        self.head = n_node

    def add_item(self, data):
        new_n = Node(data)
        if self.head is None:
            self.head = new_n
        else:
        
            last_n = self.head

            while last_n.reference:
                last_n = last_n.reference
            last_n.reference = new_n 


        # Accepts a value. Creates a node with that value, and adds the node to the end of the linked list.

# linked_list1 = LinkedList()


# linked_list1.add_to_start(82)
# linked_list1.add_to_start(55)

# linked_list1.print_linked_list()

mylist = LinkedList()

mylist.add_item(5)
mylist.add_item(10)
mylist.add_item(15)

mylist.print_linked_list()