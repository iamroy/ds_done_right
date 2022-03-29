from linked_list.linked_list import Linked_List
import linked_list.ll_problems as ll_probs

def stack_driver():
    pass

def queue_driver():
    pass

def linked_list_driver():
    new_ll = Linked_List()
    #new_ll.insert_at_end_ll(0)
    #new_ll.insert_at_end_ll(1)
    #new_ll.insert_at_end_ll(2)
    #new_ll.insert_at_end_ll(3)
    #new_ll.insert_at_end_ll(4)
    #new_ll.insert_at_end_ll(12)
    #new_ll.insert_at_end_ll(7)
    #new_ll.insert_at_front_ll(11)
    #new_ll.insert_at_end_ll(8)
    #new_ll.insert_at_end_ll(7)
    #new_ll.print_ll()
    #new_ll = ll_probs.remove_duplicates_unsorted_list(new_ll)
    #new_ll = ll_probs.reverse_list(new_ll)
    #new_ll = ll_probs.reverse_between_one_pass(new_ll, 2, 3)

    new_ll_1 = Linked_List()
    new_ll_1.insert_at_end_ll(7)
    new_ll_1.insert_at_end_ll(2)
    new_ll_1.insert_at_end_ll(4)
    new_ll_1.insert_at_end_ll(3)

    new_ll_2 = Linked_List()
    new_ll_2.insert_at_end_ll(1)
    new_ll_2.insert_at_end_ll(4)
    new_ll_2.insert_at_end_ll(3)
    #new_ll_2.insert_at_end_ll(2)
    #new_ll_2.insert_at_end_ll(5)
    #new_ll_2.insert_at_end_ll(2)
    #new_ll_2.insert_at_end_ll(6)
    #new_ll_2.insert_at_end_ll(7)
    #new_ll_2.insert_at_end_ll(8)

    #new_ll = ll_probs.add_two_numbers(new_ll_1, new_ll_2)
    #new_ll.print_ll()
    #new_ll = ll_probs.add_two_numbers_reverse_list(new_ll_1, new_ll_2)
    new_ll_2.print_ll()
    #print(ll_probs.next_larger_nodes(new_ll_2))
    #new_ll_2 = ll_probs.plus_one(new_ll_2)
    #new_ll_2 = ll_probs.merge_nodes_iterative(new_ll_2)
    #new_ll_2 = ll_probs.odd_even_list(new_ll_2)
    #new_ll_2 = ll_probs.reorder_list(new_ll_2)
    new_ll_2 = ll_probs.partition_list_2(new_ll_2, 3)
    new_ll_2.print_ll()

    #print(ll_probs.linked_list_has_cycle(new_ll))
    #new_ll.create_cycle_ll(4)
    #print(ll_probs.linked_list_has_cycle2(new_ll))
    #new_ll.print_ll()
    #new_ll.insert_at_index_ll(5, 2)
    #new_ll.sort_elements_ll()
    #new_ll = ll_probs.remove_duplicates_sorted_list(new_ll)
    #new_ll.delete_from_beginning_ll()
    #new_ll.delete_from_end_ll()
    #new_ll.delete_at_index_ll(2)
    #print(new_ll.search_in_ll(1))

    #new_ll = ll_probs.remove_elements(new_ll, 2)
    #new_ll.print_ll()
    #new_ll2 = Linked_List()
    #new_ll2.insert_at_end_ll(1)
    #new_ll2.insert_at_end_ll(2)
    #new_ll2.insert_at_end_ll(4)
    #new_ll2.insert_at_end_ll(2)
    #new_ll2.insert_at_end_ll(1)
    #new_ll2.print_ll()
    #print(ll_probs.is_palindrome(new_ll2))

def binary_tree_driver():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack_driver()
    queue_driver()
    linked_list_driver()
    binary_tree_driver()
