class Node:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
#function for preorder traversal.
def preorderTraversal(node):
    if node is not None:
        preorderTraversal(node.leftchild)
        print(node.data,end='->')
        preorderTraversal(node.rightchild)
#Function for inorder traversal.
def inorderTraversal(node):
    if node is not None:
        print(node.data,end='->')
        inorderTraversal(node.leftchild)
        inorderTraversal(node.rightchild)
#Function for post order tracersal
def postorderTraversal(node):
    if node is not None:
        postorderTraversal(node.leftchild)
        postorderTraversal(node.rightchild)
        print(node.data,end='->')

def main():
    # Create the binary tree
    first = Node(5)
    first.leftchild = Node(3)
    first.rightchild = Node(8)
    first.leftchild.leftchild = Node(1)
    first.leftchild.rightchild = Node(4)
    first.rightchild.rightchild = Node(10)
    
    # Preoder Traversal of  the tree
    print('Preorder Traversal of the tree:')
    preorderTraversal(first)
    print("None")  
    # Inorder Traversal of the tree
    print('Inorder Traversal of the tree')
    inorderTraversal(first)
    print('None')
    #Postorder Traversal of the tree
    print('Postorder Traversal of the tree')
    postorderTraversal(first)
    print('None')


if __name__ == '__main__':
    main()
