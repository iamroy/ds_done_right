from linked_list.ll_node import Node

class Linked_List:
    def __init__(self):
        self.head = None
        self.length = 0


    def print_ll(self):
        temp = self.head

        #print(f'\nList length: {self.length}')
        print("List elements are -")
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
            self.length += 1
            return

        while temp:
            prev = temp
            temp = temp.next

        prev.next = newNode
        self.length += 1

    def insert_at_front_ll(self, val):
        newNode = Node(val)
        temp = self.head

        if temp:

            nextNode = self.head
            newNode.next = nextNode

        self.head = newNode
        self.length += 1

    def insert_at_index_ll(self, val, index):

        newNode = Node(val)
        temp = self.head
        node_counter = 0

        if not index:
            self.insert_at_front_ll(val)
            self.length += 1
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

        self.length += 1


    def create_cycle_ll(self, element_index):

        temp = self.head
        prev = temp
        node_counter = 0
        index_node = None

        while temp:
            node_counter += 1

            if node_counter == element_index:
                index_node = temp

            prev =  temp
            temp = temp.next

        if index_node:
            prev.next = index_node


    def delete_from_beginning_ll(self):

        if not self.head:

            print('Empty linked list')
            return

        if not self.head.next:
            self.head = None
            self.length -= 1
            return

        head_node = self.head
        next_node = self.head.next
        self.head = next_node
        head_node = None
        self.length -= 1


    def delete_from_end_ll(self):

        if self.head is None:
            return

        temp = self.head

        if temp.next is None:
            self.head = None
            self.length -= 1
            return

        while temp.next.next:
            temp = temp.next

        temp.next = None
        self.length -= 1

    def delete_at_index_ll(self, index):
        node_counter = 0
        temp = self.head

        if index == 0:
            if self.length:
                self.length -= 1
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
        self.length -= 1

    def search_in_ll(self, val):
        temp = self.head

        while temp:
            if temp.data == val:
                return True
            temp = temp.next

        return False

    # Simple bubble sort
    def sort_elements_ll(self):

        print('Sorting....')
        temp = self.head
        ll_length = self.length

        counter = ll_length

        while counter:
            temp = self.head
            i = 1
            while i<counter:
                i += 1
                next_node = temp.next
                if next_node and next_node.data<temp.data:
                    temp.data, next_node.data = next_node.data, temp.data
                temp = temp.next

            counter -= 1






