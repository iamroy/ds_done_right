from linked_list.linked_list import Linked_List
import linked_list.ll_problems as ll_probs
import binary_tree.bt_problems as bt_probs
from binary_tree.bt_node import TreeNode
from binary_tree.binary_tree import Binary_Tree
from tree import drawTree


def stack_driver():
    pass

def queue_driver():
    pass

def linked_list_driver():

    new_ll_2 = Linked_List()
    new_ll_2.insert_at_end_ll(1)
    new_ll_2.insert_at_end_ll(2)
    new_ll_2.insert_at_end_ll(3)
    new_ll_2.insert_at_end_ll(4)
    #new_ll = ll_probs.remove_duplicates_unsorted_list(new_ll)
    #new_ll = ll_probs.reverse_list(new_ll)
    #new_ll = ll_probs.reverse_between_one_pass(new_ll, 2, 3)

    #new_ll = ll_probs.add_two_numbers(new_ll_1, new_ll_2)
    #new_ll.print_ll()
    #new_ll = ll_probs.add_two_numbers_reverse_list(new_ll_1, new_ll_2)
    #new_ll_2.print_ll()
    #print(ll_probs.next_larger_nodes(new_ll_2))
    #new_ll_2 = ll_probs.plus_one(new_ll_2)
    #new_ll_2 = ll_probs.merge_nodes_iterative(new_ll_2)
    #new_ll_2 = ll_probs.odd_even_list(new_ll_2)
    #new_ll_2 = ll_probs.reorder_list(new_ll_2)
    #new_ll_2 = ll_probs.partition_list_2(new_ll_2, 3)
    #new_ll_2 = ll_probs.swap_nodes(new_ll_2, 2)
    #new_ll_2 = ll_probs.remove_nth_from_end(new_ll_2, 4)
    #new_ll_2.print_ll()

    #print(ll_probs.linked_list_has_cycle(new_ll))
    #new_ll.create_cycle_ll(4)
    #print(ll_probs.linked_list_has_cycle2(new_ll))
    #new_ll.insert_at_index_ll(5, 2)
    #new_ll.sort_elements_ll()
    #new_ll = ll_probs.remove_duplicates_sorted_list(new_ll)
    #new_ll.delete_from_beginning_ll()
    #new_ll.delete_from_end_ll()
    #new_ll.delete_at_index_ll(2)
    #print(new_ll.search_in_ll(1))
    #new_ll = ll_probs.remove_elements(new_ll, 2)
    #print(ll_probs.is_palindrome(new_ll2))

def binary_tree_driver():

    root_node = TreeNode(1)
    root_node.left = TreeNode(2)
    root_node.right = TreeNode(3)
    root_node.left.left = TreeNode(4)
    root_node.left.right = TreeNode(5)
    root_node.right.left = TreeNode(6)
    root_node.right.right = TreeNode(7)

    new_tree = Binary_Tree(root_node)
    drawTree(new_tree.root)
    # print binary tree
    space = 0
    height = 10
    #bt.print_binary_tree(new_tree.root, space, height)
    print(new_tree.pre_order_traversal_recursive(new_tree.root))
    print(new_tree.pre_order_traversal_iterative(new_tree.root))
    print(new_tree.in_order_traversal_recursive(new_tree.root))
    print(new_tree.in_order_traversal_iterative(new_tree.root))
    print(new_tree.post_order_traversal_recursive(new_tree.root))
    print(new_tree.post_order_traversal_iterative(new_tree.root))
    print(new_tree.level_order_traversal_iterative(new_tree.root))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack_driver()
    queue_driver()
    #linked_list_driver()
    binary_tree_driver()