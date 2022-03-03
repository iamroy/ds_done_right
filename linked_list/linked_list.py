from linked_list.ll_node import Node

class Linked_List:
    def __init__(self):
        self.head = None


    def print_ll(self):
        temp = self.head

        print("\nList elements are -")
        while temp:
            print(f'{temp.data}-->', end='')
            temp = temp.next

        print('None')


    def insert_at_end_ll(self, val):
        newNode = Node(val)
        temp = self.head
        prev = self.head

        if not self.head:
            self.head = newNode
            return

        while temp:
            prev = temp
            temp = temp.next

        prev.next = newNode


    def insert_at_front_ll(self, val):
        newNode = Node(val)
        temp = self.head

        if temp:

            nextNode = self.head
            newNode.next = nextNode

        self.head = newNode


    def insert_at_index_ll(self, val, index):

        newNode = Node(val)
        temp = self.head
        node_counter = 0

        if not index:
            self.insert_at_front_ll(val)
            return

        while temp and node_counter<index:
            node_counter += 1
            prev = temp
            temp = temp.next

        if node_counter == index:
            newNode.next = temp
            prev.next = newNode

        if node_counter < index:
            print(f'Linked List element count ({node_counter}) less than insert index ({index})')


    def delete_from_beginning_ll(self):

        if not self.head:

            print('Empty linked list')
            return

        if not self.head.next:
            self.head = None
            return

        head_node = self.head
        next_node = self.head.next
        self.head = next_node
        head_node = None


    def delete_from_end_ll(self):

        if self.head is None:
            return

        temp = self.head

        if temp.next is None:
            self.head = None
            return

        while temp.next.next:
            temp = temp.next

        temp.next = None


    def delete_at_index_ll(self, index):
        node_counter = 0
        temp = self.head

        if index == 0:
            self.head = None
            return

        while node_counter<index:
            prev = temp

            if temp.next:
                temp = temp.next
                node_counter += 1
            else:
                return

        prev.next = temp.next

    def search_in_ll(self, val):
        pass
