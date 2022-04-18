#The maximum number of nodes at level ‘l’ of a binary tree is 2**l.

#The Maximum number of nodes in a binary tree of height ‘h’ is 2**h – 1.

#In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is Log2(N+1). If we
#consider the convention where the height of a root node is considered as 0, then above formula for minimum
#possible height becomes | Log2(N+1) | – 1

#A Binary Tree with L leaves has at least | Log2L |+ 1   levels.

#In Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more than nodes with two children.
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right