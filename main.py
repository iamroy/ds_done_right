from linked_list.linked_list import Linked_List

def stack_driver():
    pass

def queue_driver():
    pass

def linked_list_driver():
    new_ll = Linked_List()
    new_ll.insert_at_end_ll(1)
    new_ll.insert_at_end_ll(2)
    new_ll.insert_at_end_ll(4)
    new_ll.insert_at_end_ll(12)
    new_ll.print_ll()
    new_ll.insert_at_end_ll(7)
    new_ll.print_ll()
    new_ll.insert_at_front_ll(11)
    new_ll.print_ll()
    new_ll.insert_at_index_ll(5, 2)
    new_ll.print_ll()
    #new_ll.delete_from_beginning_ll()
    #new_ll.print_ll()
    #new_ll.delete_from_end_ll()
    #new_ll.print_ll()
    #new_ll.delete_at_index_ll(2)
    #new_ll.print_ll()
    #print(new_ll.search_in_ll(1))

    new_ll.sort_elements_ll()
    new_ll.print_ll()


def binary_tree_driver():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack_driver()
    queue_driver()
    linked_list_driver()
    binary_tree_driver()
