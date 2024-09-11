class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def searchKey(node,key):
    if node  is None :
        return False
    if node.data == key:
        return True
    if node.data < key:
        return searchKey(node.right,key)
    else:
        return searchKey(node.left,key)
if __name__ == '__main__':
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    print(searchKey(node,5))
    