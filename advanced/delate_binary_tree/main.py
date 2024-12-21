import math


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printInOrder(self):
        self.inOrderWalk(self)
        print("")

    def inOrderWalk(self, tRoot):
        if tRoot is not None:
            self.inOrderWalk(tRoot.left)
            print(tRoot.data, end=" ")
            self.inOrderWalk(tRoot.right)


class BinarySearchTree:
    def __init__(self, arrList):
        sortedList = sorted(arrList)
        self.root = BinarySearchTree.sortedArrayToBST(sortedList)

    @staticmethod
    def sortedArrayToBST(array):
        if not array:
            return None
        return BinarySearchTree.sortedArrayToBSTHelper(array, 0, len(array) - 1)

    @staticmethod
    def sortedArrayToBSTHelper(arr, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        left = BinarySearchTree.sortedArrayToBSTHelper(arr, start, mid - 1)
        right = BinarySearchTree.sortedArrayToBSTHelper(arr, mid + 1, end)
        return BinaryTree(arr[mid], left, right)

    def keyExist(self, key):
        current = self.root
        while current:
            if current.data == key:
                return True
            current = current.left if key < current.data else current.right
        return False

    def search(self, key):
        current = self.root
        while current:
            if current.data == key:
                return current
            current = current.left if key < current.data else current.right
        return None

    def insert(self, value):
        current = self.root
        while current:
            if value < current.data:
                if not current.left:
                    current.left = BinaryTree(value)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = BinaryTree(value)
                    return
                current = current.right

    def findParent(self, root, node):
        parent = None
        current = root
        while current and current != node:
            parent = current
            current = current.left if node.data < current.data else current.right
        return parent

    def findMin(self, node):
        while node.left:
            node = node.left
        return node

    def transplant(self, nodeParent, node, target):
        if not nodeParent:
            self.root = target
        elif nodeParent.left == node:
            nodeParent.left = target
        else:
            nodeParent.right = target

    def deleteNode(self, node):
        if not node.left and not node.right:
            parent = self.findParent(self.root, node)
            self.transplant(parent, node, None)
        elif not node.left:
            parent = self.findParent(self.root, node)
            self.transplant(parent, node, node.right)
        elif not node.right:
            parent = self.findParent(self.root, node)
            self.transplant(parent, node, node.left)
        else:
            successor = self.findMin(node.right)
            if successor != node.right:
                successorParent = self.findParent(self.root, successor)
                self.transplant(successorParent, successor, successor.right)
                successor.right = node.right
            parent = self.findParent(self.root, node)
            self.transplant(parent, node, successor)
            successor.left = node.left

    def delete(self, key):
        if self.keyExist(key):
            node = self.search(key)
            self.deleteNode(node)

    def printSorted(self):
        self.root.printInOrder()


balancedBST = BinarySearchTree(
    [4, 43, 36, 46, 32, 7, 97, 95, 34, 8, 96, 35, 85, 1010, 232]
)
balancedBST.printSorted()
balancedBST.delete(46)
balancedBST.printSorted()
balancedBST.delete(7)
balancedBST.printSorted()
balancedBST.delete(4)
balancedBST.printSorted()
balancedBST.delete(1010)
balancedBST.printSorted()
balancedBST.delete(0)
balancedBST.printSorted()
