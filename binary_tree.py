from dataclasses import dataclass
from typing import Optional, Self


@dataclass
class Node:
    value: int
    left: Optional[Self] = None
    right: Optional[Self] = None


@dataclass
class BinaryTree:
    root: Optional[Node] = None

    def create_node(self, value: int) -> Node:
        return Node(value)

    def print_tree(self, root: Node):
        if root is None:
            return

        print(root.value)
        self.print_tree(root.left)
        self.print_tree(root.right)


def main() -> None:
    tree = BinaryTree()
    root = tree.create_node(5)
    root.left = tree.create_node(3)
    root.left.left = tree.create_node(12)
    root.left.right = tree.create_node(4)
    root.right = tree.create_node(6)
    root.right.left = tree.create_node(8)
    tree.print_tree(root)


if __name__ == "__main__":
    main()
