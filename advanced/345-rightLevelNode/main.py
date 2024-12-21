from typing import List, Optional
from collections import deque


class BinaryTree:
    def __init__(
        self,
        data: int,
        left: Optional["BinaryTree"] = None,
        right: Optional["BinaryTree"] = None,
    ):
        self.data = data
        self.left = left
        self.right = right


def rightLevelNode(root: Optional[BinaryTree]) -> Optional[List[int]]:
    if root is None:
        return []

    result: List[int] = []
    queue: deque[BinaryTree] = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()

            # 最後のノード（右端のノード）を保持
            if i == level_size - 1:
                result.append(node.data)

            # 子ノードをキューに追加
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
