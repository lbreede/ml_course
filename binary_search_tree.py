class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, newValue):
        if root is None:
            return Node(newValue)

        else:
            if newValue < root.value:
                root.left = self.insert(root.left, newValue)
            else:
                root.right = self.insert(root.right, newValue)

        return root

    def insert_node(self, value):
        self.root = self.insert(self.root, value)

    def printTree(self, root):
        if root is None:
            return
        self.printTree(root.left)
        print(root.value)
        self.printTree(root.right)


if __name__ == "__main__":
    bst = BST()
    bst.insert_node(50)
    bst.insert_node(30)
    bst.insert_node(20)
    bst.insert_node(40)
    bst.insert_node(70)
    bst.insert_node(60)
    bst.insert_node(80)

    bst.printTree(bst.root)
