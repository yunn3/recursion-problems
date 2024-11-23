#include "binary_tree.hpp"
#include <algorithm>
#include <iostream>

BinaryTree::BinaryTree(int value)
    : data(value), left(nullptr), right(nullptr) {}

BinaryTree::BinaryTree(int value, std::unique_ptr<BinaryTree> left,
                       std::unique_ptr<BinaryTree> right)
    : data(value), left(std::move(left)), right(std::move(right)) {}

BinarySearchTree::BinarySearchTree() : root(nullptr) {}

BinarySearchTree::BinarySearchTree(const std::vector<int> &values) {
  std::vector<int> sorted_values = values;
  std::sort(sorted_values.begin(), sorted_values.end());
  root = build_balanced_bst(sorted_values, 0, sorted_values.size() - 1);
}

void BinarySearchTree::insert(int value) { insert_recursive(root, value); }

void BinarySearchTree::insert_recursive(std::unique_ptr<BinaryTree> &node,
                                        int value) {
  if (!node) {
    node = std::make_unique<BinaryTree>(value);
  } else if (value < node->data) {
    insert_recursive(node->left, value);
  } else if (value > node->data) {
    insert_recursive(node->right, value);
  }
}

void BinarySearchTree::print_inorder() {
  print_inorder_recursive(root.get());
  std::cout << std::endl;
}

void BinarySearchTree::print_inorder_recursive(const BinaryTree *node) {
  if (node) {
    print_inorder_recursive(node->left.get());
    std::cout << node->data << " ";
    print_inorder_recursive(node->right.get());
  }
}

std::unique_ptr<BinaryTree>
BinarySearchTree::build_balanced_bst(const std::vector<int> &sorted_values,
                                     int start, int end) {
  if (start > end) {
    return nullptr;
  }
  int mid = start + (end - start) / 2;
  auto left_subtree = build_balanced_bst(sorted_values, start, mid - 1);
  auto right_subtree = build_balanced_bst(sorted_values, mid + 1, end);
  return std::make_unique<BinaryTree>(
      sorted_values[mid], std::move(left_subtree), std::move(right_subtree));
}

const BinaryTree *BinarySearchTree::search(int key) {
  return search_recursive(root.get(), key);
}

const BinaryTree *BinarySearchTree::search_recursive(const BinaryTree *node,
                                                     int key) {
  if (node == nullptr) {
    return nullptr;
  }
  if (node->data == key) {
    return node;
  } else if (key < node->data) {
    return search_recursive(node->left.get(), key);
  } else {
    return search_recursive(node->right.get(), key);
  }
}

bool BinarySearchTree::key_exists(int key) { return search(key) != nullptr; }

int BinarySearchTree::height() { return height_recursive(root.get()); }

int BinarySearchTree::height_recursive(const BinaryTree *node) {
  if (!node) {
    return -1;
  }
  int left_height = height_recursive(node->left.get());
  int right_height = height_recursive(node->right.get());
  return std::max(left_height, right_height) + 1;
}
