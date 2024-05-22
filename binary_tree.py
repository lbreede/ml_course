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

    @staticmethod
    def create_node(value: int) -> Node:
        return Node(value)

    def print_tree(self, root: Node):
        if root is None:
            return

        print(root.value)
        self.print_tree(root.left)
        self.print_tree(root.right)

    def count_leaves(self, root: Node) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        return self.count_leaves(root.left) + self.count_leaves(root.right)


def main() -> None:
    tree = BinaryTree()
    root = tree.create_node(5)
    root.left = tree.create_node(3)
    root.left.left = tree.create_node(12)
    root.left.right = tree.create_node(4)
    root.right = tree.create_node(6)
    root.right.left = tree.create_node(8)
    # root.right.right = tree.create_node(7)
    tree.print_tree(root)
    leaves = tree.count_leaves(root)
    print(f"Number of leaves: {leaves}")


if __name__ == "__main__":
    main()
