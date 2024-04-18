# Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.
# Note that the root node is at depth 1.

# The adding rule is:

# Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
# cur's original left subtree should be the left subtree of the new left subtree root.
# cur's original right subtree should be the right subtree of the new right subtree root.
# If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

# Example 1:

# Input: root = [4,2,6,3,1,5], val = 1, depth = 2
# Output: [4,1,1,2,null,null,6,3,1,5]

# Example 2:

# Input: root = [4,2,null,3,1], val = 1, depth = 3
# Output: [4,2,null,1,1,3,null,null,1]

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# The depth of the tree is in the range [1, 104].
# -100 <= Node.val <= 100
# -105 <= val <= 105
# 1 <= depth <= the depth of tree + 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Recursive definition. If we reach the specified depth, we want to insert a new node in between this level and the next level.
        # We want to traverse the tree DFS-style. Only process the tree when we are at the specified depth. Then, we insert the nodes and return.

        def dfs(node, val, curLevel):
            if not node:
                return

            elif curLevel + 1 == depth:
                leftSubtree = node.left
                rightSubtree = node.right
                node.left = TreeNode(val=val, left=leftSubtree)
                node.right = TreeNode(val=val, right=rightSubtree)

            else:
                dfs(node.left, val, curLevel + 1)
                dfs(node.right, val, curLevel + 1)

        if depth == 1:
            return TreeNode(val=val, left=root)
        else:
            dfs(root, val, 1)
            return root