class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def createNode(self, newValue):
        newNode = Node(newValue)
        newNode.left = None
        newNode.right = None

        return newNode

    def printTree(self, root):
        if root is None:
            return

        print(root.value)
        self.printTree(root.left)
        self.printTree(root.right)

    def countLeaveNodes(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        leftNodes = self.countLeaveNodes(root.left)
        rightNodes = self.countLeaveNodes(root.right)

        return leftNodes + rightNodes

if __name__ == "__main__":
    tree1 = BinaryTree()
    root1 = tree1.createNode(5)
    root1.left = tree1.createNode(3)
    root1.left.left = tree1.createNode(12)
    root1.left.right = tree1.createNode(4)
    root1.right = tree1.createNode(6)
    root1.right.left = tree1.createNode(8)
    root1.right.right = tree1.createNode(4)

    #tree1.printTree(root1)
    res = tree1.countLeaveNodes(root1)
    print(res)



