#include "binary_tree.hpp"
#include <algorithm>

BinaryTree::BinaryTree(int value)
    : data(value), left(nullptr), right(nullptr) {}

BinaryTree::BinaryTree(int value, std::unique_ptr<BinaryTree> left,
                       std::unique_ptr<BinaryTree> right)
    : data(value), left(std::move(left)), right(std::move(right)) {}

BinarySearchTree::BinarySearchTree(const std::vector<int> &values) {
  std::vector<int> sorted_values = values;
  std::sort(sorted_values.begin(), sorted_values.end());
  root = buildBalancedBST(sorted_values, 0, sorted_values.size() - 1);
}

std::unique_ptr<BinaryTree>
BinarySearchTree::buildBalancedBST(const std::vector<int> &sorted_values,
                                   int start, int end) {
  if (start > end) {
    return nullptr;
  }
  int mid = start + (end - start) / 2;
  auto left_subtree = buildBalancedBST(sorted_values, start, mid - 1);
  auto right_subtree = buildBalancedBST(sorted_values, mid + 1, end);
  return std::make_unique<BinaryTree>(
      sorted_values[mid], std::move(left_subtree), std::move(right_subtree));
}

const BinaryTree *BinarySearchTree::search(int key) {
  return searchRecursive(root.get(), key);
}

const BinaryTree *BinarySearchTree::searchRecursive(const BinaryTree *node,
                                                    int key) {
  if (node == nullptr) {
    return nullptr;
  }
  if (node->data == key) {
    return node;
  } else if (key < node->data) {
    return searchRecursive(node->left.get(), key);
  } else {
    return searchRecursive(node->right.get(), key);
  }
}

bool BinarySearchTree::KeyExists(int key) { return search(key) != nullptr; }

int BinarySearchTree::height() { return heightRecursive(root.get()); }

int BinarySearchTree::heightRecursive(const BinaryTree *node) {
  if (!node) {
    return -1;
  }
  int left_height = heightRecursive(node->left.get());
  int right_height = heightRecursive(node->right.get());
  return std::max(left_height, right_height) + 1;
}
