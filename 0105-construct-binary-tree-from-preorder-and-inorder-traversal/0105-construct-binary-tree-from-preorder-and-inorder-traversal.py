# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        index_map = {value: i for i, value in enumerate(inorder)}
        self.pre_index = 0

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(root_val)

            mid = index_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)