class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def maxDepth(node):
    if node is None:
        return 0
    lDepth = maxDepth(node.left)
    rDepth = maxDepth(node.right)
    return max(lDepth,rDepth)+1
# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(maxDepth(root))