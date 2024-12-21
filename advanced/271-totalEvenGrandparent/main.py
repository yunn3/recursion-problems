class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def totalEvenGrandparent(root: BinaryTree) -> int:
    total = 0

    # 再帰的ヘルパー関数 (ノード、親、祖父母)
    def helper(node, parent, grandparent):
        nonlocal total  # 外部変数 total を参照

        if node is None:
            return

        # 祖父母ノードが偶数ならば、そのノードの値を合計に加算
        if grandparent and grandparent.data % 2 == 0:
            total += node.data

        # 左右の子ノードを再帰的に処理
        helper(node.left, node, parent)
        helper(node.right, node, parent)

    # 再帰的に探索を開始
    helper(root, None, None)

    return total


# 二分木をリストから生成する関数
def toBinaryTree(arr):
    if not arr:
        return None

    root = BinaryTree(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = BinaryTree(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = BinaryTree(arr[i])
            queue.append(node.right)
        i += 1

    return root
