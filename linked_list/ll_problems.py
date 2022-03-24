#203. Remove Linked List Elements
#234. Palindrome Linked List
#83. Remove Duplicates from Sorted List
#141. Linked List Cycle

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

#83. Remove Duplicates from Sorted List
def remove_duplicates_sorted_list(linked_list):
    head_node = linked_list.head

    if not head_node:
        return

    curr_node = head_node
    newNode = Node(curr_node.data-1)
    newNode.next = head_node
    prev = newNode

    while curr_node:

        if curr_node.data == prev.data:
            prev.next = curr_node.next
        else:
            prev = curr_node

        curr_node = curr_node.next

    linked_list.head = newNode.next

    return linked_list


# hash map approach
def linked_list_cycle(linked_list):
    head_node = linked_list.head
    curr_node = head_node
    seen = {}
    counter = 0
    while curr_node:
        counter += 1

        if curr_node not in seen:
            seen[curr_node] = counter
        else:
            return True

        curr_node = curr_node.next

    return False