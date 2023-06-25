from typing import Optional


def main():
    tree = RedBlackTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(5)
    tree.insert(15)
    tree.insert(30)
    print("Элементы дерева:")
    tree.traverse(tree.root)


class RedBlackTree:
    class Node:
        def __init__(self, value: int, color: str = "RED"):
            self.value = value
            self.left: Optional[RedBlackTree.Node] = None
            self.right: Optional[RedBlackTree.Node] = None
            self.color = color
        
        def _color_change(self) -> None:
            self.color = "RED"
            self.left.color = "BLACK"
            self.right.color = "BLACK"
        
        def _rotate_left(self) -> 'RedBlackTree.Node':
            x = self.right
            self.right = x.left
            x.left = self
            x.color = self.color
            self.color = "RED"
            return x

        def _rotate_right(self) -> 'RedBlackTree.Node':
            x = self.left
            self.left = x.right
            x.right = self
            x.color = self.color
            self.color = "RED"
            return x

    def __init__(self):
        self.root: Optional[RedBlackTree.Node] = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = self.Node(value)
            self.root.color = "BLACK"
            return

        self.root = self._insert(self.root, value)
        self.root.color = "BLACK"
    
    def _insert(self, node: 'RedBlackTree.Node', value: int) -> 'RedBlackTree.Node':
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        if self._is_red(node.right) and not self._is_red(node.left):
            node = node._rotate_left()
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = node._rotate_right()
        if self._is_red(node.left) and self._is_red(node.right):
            node._color_change()

        return node
    
    def _is_red(self, node: 'RedBlackTree.Node') -> bool:
        if node is None:
            return False
        return node.color == "RED"

    def traverse(self, node) -> None:
        if node is not None:
            self.traverse(node.left)
            print(f"{node.value} – {node.color}")
            self.traverse(node.right)

if __name__ == "__main__":
    main()