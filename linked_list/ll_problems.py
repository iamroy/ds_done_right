#203. Remove Linked List Elements
from linked_list.ll_node import Node

#203. Remove Linked List Elements
def remove_elements(linked_list, val):

    head_node = linked_list.head
    temp = head_node
    newNode = Node(-1)
    newNode.next = head_node
    prev = newNode

    while temp:
        if temp.data == val:
            prev.next = temp.next
        else:
            prev = temp

        temp = temp.next

    linked_list.head = newNode.next
    return linked_list

def is_palindrome(linked_list):
    return False

def remove_duplicates_sorted_list(head_node):
    pass

def linked_list_cycle(head_node):
    pass