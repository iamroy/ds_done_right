from binary_tree.bt_node import TreeNode
from collections import deque


class Binary_Tree:

    def __init__(self, root_node=None):
        self.root = root_node

    def get_height(self, node):
        if not node:
            return 0

        return max(self.get_height(node.left), self.get_height(node.right)) + 1

    def pre_order_traversal_recursive(self, root_node):

        out_list = []
        if root_node:
            out_list.append(root_node.data)
            out_list += self.pre_order_traversal_recursive(root_node.left)
            out_list += self.pre_order_traversal_recursive(root_node.right)
        return out_list

    def pre_order_traversal_iterative(self, root_node):
        stack = []
        out_list = []
        root = root_node

        while root or stack:
            if root:
                out_list.append(root.data)
                stack.append(root)
                root = root.left
            else:
                stack_top = stack.pop()
                root = stack_top.right
        return out_list


    def in_order_traversal_recursive(self, root_node):

        out_list = []
        if root_node:
            out_list += self.in_order_traversal_recursive(root_node.left)
            out_list.append(root_node.data)
            out_list += self.in_order_traversal_recursive(root_node.right)
        return out_list


    def in_order_traversal_iterative(self, root_node):
        stack = []
        out_list = []
        root = root_node

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                stack_top = stack.pop()
                out_list.append(stack_top.data)
                root = stack_top.right

        return out_list

    def post_order_traversal_recursive(self, root_node):
        out_list = []
        if root_node:
            out_list += self.post_order_traversal_recursive(root_node.left)
            out_list += self.post_order_traversal_recursive(root_node.right)
            out_list.append(root_node.data)
        return out_list

    def post_order_traversal_iterative(self, root_node):
        stack = []
        out_list = []
        root = root_node
        prev = None

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if not root.right or root.right == prev:
                    out_list.append(root.data)
                    stack_top = stack.pop()
                    prev = stack_top
                    root = None
                else:
                    root = root.right
        return out_list

    def lever_order_traversal_recursive(self, root_node):
        out_list = []
        if root_node:
            out_list += self.post_order_traversal_recursive(root_node.left)
            out_list += self.post_order_traversal_recursive(root_node.right)
            out_list.append(root_node.data)
        return out_list

    #102. Binary Tree Level Order Traversal
    def level_order_traversal_iterative(self, root_node):
        out_list = []
        stack = []

        if not root_node:
            return out_list

        stack.append(root_node)

        while stack:

            top_node = stack.pop(0)
            out_list.append(top_node.data)

            if top_node.left:
                stack.append(top_node.left)

            if top_node.right:
                stack.append(top_node.right)
        return out_list


def print_binary_tree(root, space, height):
    # Base case
    if root is None:
        return

    # increase distance between levels
    space += height

    # print right child first
    print_binary_tree(root.right, space, height)
    print()

    # print the current node after padding with spaces
    for i in range(height, space):
        print(' ', end='')

    print(root.data, end='')

    # print left child
    print()
    print_binary_tree(root.left, space, height)