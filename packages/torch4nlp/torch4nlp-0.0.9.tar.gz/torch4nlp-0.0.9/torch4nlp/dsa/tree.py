class BinaryTreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def depth(self, node=None):
        """
            if node is None, return the depth of current subtree
            otherwise, return the depth of node in current subtree
        """

        max_depth = 1
        if node is None:
            queue = [(self, 1)]
            while queue:
                node, depth = queue.pop(0)
                max_depth = max(max_depth, depth)
                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))
            return max_depth
        else:
            if self is node:
                return max_depth
            queue = [(self, 1)]
            while queue:
                pnode, depth = queue.pop(0)
                if pnode is node:
                    return max_depth
                else:
                    if node.left:
                        queue.append((node.left, depth + 1))
                    if node.right:
                        queue.append((node.right, depth + 1))
            return -1


def build_binary_tree(arr):
    if len(arr) == 0:
        return None
    root = BinaryTreeNode(arr[0])