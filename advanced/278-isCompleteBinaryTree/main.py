from typing import Optional
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


def isCompleteBinaryTree(root: Optional[BinaryTree]) -> bool:
    if root is None:
        return True  # 空の木は完全二分木

    queue: deque[Optional[BinaryTree]] = deque([root])
    found_null = False

    while queue:
        node = queue.popleft()

        if node is None:
            found_null = True
        else:
            if found_null:
                # nullの後にノードがある場合は完全二分木ではない
                return False
            # 子ノードをキューに追加
            queue.append(node.left)
            queue.append(node.right)

    return True  # 全ノードをチェックして問題がなければ完全二分木
