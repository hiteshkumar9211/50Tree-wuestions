
INT_MIN = -424967296
INT_MAX = 424967296

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def isBST(node):
    return isBSTUtil(node,INT_MIN,INT_MAX)
def isBSTUtil(node,mini,maxi):
    if node is None:
        return True
    if node.data < mini or node.data > maxi:
        return False
    return isBSTUtil(node.left,mini,node.data-1) and isBSTUtil(node.right,node.data+1,maxi)
# Driver code
if __name__ == "__main__":
  root = Node(4)
  root.left = Node(2)
  root.right = Node(5)
  root.left.left = Node(1)
  root.left.right = Node(0)

  # Function call
  if (isBST(root)):
      print(True)
  else:
      print(False)

