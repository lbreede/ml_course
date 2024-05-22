from dataclasses import dataclass
from typing import Optional, Self


@dataclass
class Node:
    value: int
    left: Optional[Self] = None
    right: Optional[Self] = None


@dataclass
class BST:
    root: Optional[Node] = None

    def insert(self, root: Node, value: int) -> Node:
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    def insert_node(self, value: int) -> None:
        self.root = self.insert(self.root, value)

    def print_tree(self, root: Node) -> None:
        if root is None:
            return
        print(root.value)
        self.print_tree(root.left)
        self.print_tree(root.right)


def main() -> None:
    bst = BST()
    bst.insert_node(50)
    bst.insert_node(30)
    bst.insert_node(20)
    bst.insert_node(40)
    bst.insert_node(70)
    bst.insert_node(60)
    bst.insert_node(80)
    bst.print_tree(bst.root)


if __name__ == "__main__":
    main()
