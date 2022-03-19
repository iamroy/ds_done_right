#203. Remove Linked List Elements
#234. Palindrome Linked List
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

#234. Palindrome Linked List
def is_palindrome(linked_list):
    head_node = linked_list.head

    vals = []
    current_node = head_node
    while current_node is not None:
        vals.append(current_node.data)
        current_node = current_node.next
    return vals == vals[::-1]

def remove_duplicates_sorted_list(head_node):
    pass

def linked_list_cycle(head_node):
    pass