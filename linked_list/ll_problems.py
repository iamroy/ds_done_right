#206. Reverse Linked List
#92. Reverse Linked List II
#203. Remove Linked List Elements
#234. Palindrome Linked List
#83. Remove Duplicates from Sorted List
#1836. Remove Duplicates From an Unsorted Linked List
#141. Linked List Cycle
#1019. Next Greater Node In Linked List
#445. Add Two Numbers II


from linked_list.ll_node import Node
from linked_list.linked_list import Linked_List
from collections import defaultdict

#206. Reverse Linked List
#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]
def reverse_list(linked_list):

    head_node = linked_list.head
    if not head_node:
        return

    if head_node.next is None:
        return head_node

    curr_node = head_node
    prev_node = None

    while curr_node.next:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    curr_node.next = prev_node
    linked_list.head = curr_node
    return linked_list

#92. Reverse Linked List II
#Input: head = [1,2,3,4,5], left = 2, right = 4
#Output: [1,4,3,2,5]
#2 pass algorithm
def reverse_between(linked_list, left, right):

    head_node = linked_list.head
    curr_node = head_node
    counter = 0
    node_val = []

    while curr_node:
        counter += 1
        if counter >= left and counter <= right:
            node_val.append(curr_node.data)
        curr_node = curr_node.next

    curr_node = head_node
    counter = 0

    while curr_node:
        counter += 1
        if counter >= left and counter <= right:
            curr_node.data = node_val.pop()
        curr_node = curr_node.next

    return linked_list


#1 pass algorithm
def reverse_between_one_pass(linked_list, left, right):

    head_node = linked_list.head
    curr_node = head_node
    prev_node, rev_tail_node, rev_head_node = None, None, None
    no_rev_left_end_node = None
    counter = 0

    while curr_node:
        counter += 1
        if counter>=left and counter <=right:

            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node

            if counter == left:
                rev_tail_node = curr_node
            if counter == right:
                rev_head_node = curr_node

            curr_node = next_node
        else:
            if counter>right:
                break

            if counter<left:
                no_rev_left_end_node = curr_node

            prev_node = curr_node
            curr_node = curr_node.next

    if rev_tail_node:
        rev_tail_node.next = curr_node

    if no_rev_left_end_node:
        no_rev_left_end_node.next = rev_head_node
    else:
        linked_list.head = rev_head_node

    return linked_list


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


#1836. Remove Duplicates From an Unsorted Linked List
#Input: head = [1,2,3,2]
#Output: [1,3]
def remove_duplicates_unsorted_list(linked_list):
    head_node = linked_list.head

    if not head_node:
        return

    seen = defaultdict(int)
    curr_node = head_node

    while curr_node:
        seen[curr_node.data] += 1
        curr_node = curr_node.next

    curr_node = head_node
    newNode = Node(curr_node.data - 1)
    newNode.next = head_node
    prev = newNode

    while curr_node:

        if seen[curr_node.data]>1:
            prev.next = curr_node.next
        else:
            prev = curr_node
        curr_node = curr_node.next

    linked_list.head = newNode.next

    return linked_list

#141. Linked List Cycle
# hash map approach
def linked_list_has_cycle(linked_list):
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

#141. Linked List Cycle
# two pointer approach
def linked_list_has_cycle2(linked_list):
    head_node = linked_list.head

    if not head_node:
        return False

    slow_ptr = head_node
    fast_ptr = head_node.next

    while slow_ptr != fast_ptr:
        if fast_ptr is None or fast_ptr.next is None:
            return False
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return True

#1019. Next Greater Node In Linked List
#Input: head = [2,7,4,3,5]
#Output: [7,0,5,5,0]
#monotonic stack approach
def next_larger_nodes(linked_list):
    head_node = linked_list.head
    curr_node = head_node
    out_list = []
    stack_arr = []
    index = -1

    while curr_node:
        index += 1
        out_list += [0]
        while stack_arr and stack_arr[-1][0]<curr_node.data:
            val = stack_arr.pop()
            out_list[val[1]] = curr_node.data

        stack_arr.append([curr_node.data, index])
        curr_node = curr_node.next
    return out_list


#2181. Merge Nodes in Between Zeros
#Input: head = [0,3,1,0,4,5,2,0]
#Output: [4,11]
# recursive solution
def merge_nodes(linked_list):

    head_node = linked_list.head
    curr_node = head_node.next

    if not curr_node:
        return Linked_List()

    node_data = 0

    while curr_node.data:
        node_data += curr_node.data
        curr_node = curr_node.next

    head_node.data = node_data
    new_linked_list = Linked_List()
    new_linked_list.head = curr_node
    new_linked_list = merge_nodes(new_linked_list)
    head_node.next = new_linked_list.head
    linked_list.head = head_node

    return linked_list

def merge_nodes_iterative(linked_list):
    head_node = linked_list.head
    curr_node = head_node.next
    out_node  = head_node
    node_data = 0
    prev = None

    while curr_node:
        if not curr_node.data:
            if not prev:
                out_node = head_node
            else:
                out_node = out_node.next
            out_node.data = node_data
            prev = out_node
            node_data = 0
        node_data += curr_node.data
        curr_node = curr_node.next

    out_node.next = None

    return linked_list

#445. Add Two Numbers II
#Input: l1 = [7,2,4,3], l2 = [5,6,4]
#Output: [7,8,0,7]
# Without reversing but using extra space to store the inputs
def add_two_numbers(linked_list1, linked_list2):

    head_node = linked_list1.head
    curr_node = head_node
    num_list1 = ''

    while curr_node:
        num_list1 += str(curr_node.data)
        curr_node = curr_node.next

    head_node = linked_list2.head
    curr_node = head_node
    num_list2 = ''

    while curr_node:
        num_list2 += str(curr_node.data)
        curr_node = curr_node.next

    final_sum_str = str(int(num_list1) + int(num_list2))
    out_linked_list = Linked_List()

    for c in final_sum_str:
        out_linked_list.insert_at_end_ll(int(c))

    return out_linked_list

# With reversing but without using extra space to store the inputs
def add_two_numbers_reverse_list(linked_list1, linked_list2):
    linked_list1 = reverse_list(linked_list1)
    linked_list2 = reverse_list(linked_list2)

    head_node1 = linked_list1.head
    curr_node1 = head_node1
    head_node2 = linked_list2.head
    curr_node2 = head_node2
    out_linked_list = Linked_List()

    carry = 0
    while curr_node1 and curr_node2:

        value = (curr_node1.data+curr_node2.data)%10
        out_linked_list.insert_at_end_ll(value+carry)
        carry = (curr_node1.data + curr_node2.data) // 10
        curr_node1 = curr_node1.next
        curr_node2 = curr_node2.next

    if curr_node2:
        while curr_node2:
            out_linked_list.insert_at_end_ll(curr_node2.data)
            curr_node2 = curr_node2.next

    if curr_node1:
        while curr_node1:
            out_linked_list.insert_at_end_ll(curr_node1.data)
            curr_node1 = curr_node1.next

    return reverse_list(out_linked_list)


#142. Linked List Cycle II
#Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
def detect_cycle(linked_list):
    pass

#369. Plus One Linked List
#Input: head = [1,2,3]
#Output: [1,2,4]
def plus_one(linked_list):

    head_node = linked_list.head
    # sentinel head
    sentinel = Node(0)
    sentinel.next = head_node
    curr = head_node
    not_nine = sentinel

    # find the rightmost not-nine digit
    while curr:
        if curr.data != 9:
            not_nine = curr
        curr = curr.next

    # increase this rightmost not-nine digit by 1
    not_nine.data += 1
    not_nine = not_nine.next

    # set all the following nines to zeros
    while not_nine:
        not_nine.data = 0
        not_nine = not_nine.next

    if sentinel.data:
        linked_list.head = sentinel
    return linked_list