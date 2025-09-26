class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

        
a_list = LinkedList()
a_list.insert_at_beginning(10)
a_list.insert_at_beginning(11)
a_list.insert_at_beginning(12)
a_list.insert_at_beginning(13)
a_list.print_list()








