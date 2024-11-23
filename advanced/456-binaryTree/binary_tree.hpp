#ifndef BINARY_TREE_HPP
#define BINARY_TREE_HPP

#include <memory>
#include <vector>

class BinaryTree {
public:
  int data;
  std::unique_ptr<BinaryTree> left;
  std::unique_ptr<BinaryTree> right;

  BinaryTree(int value);
  BinaryTree(int value, std::unique_ptr<BinaryTree> left,
             std::unique_ptr<BinaryTree> right);
};

class BinarySearchTree {
public:
  std::unique_ptr<BinaryTree> root;

  BinarySearchTree();
  BinarySearchTree(const std::vector<int> &values);

  void insert(int value);
  void print_inorder();

  const BinaryTree *search(int key);
  bool key_exists(int key);
  int height();

private:
  void insert_recursive(std::unique_ptr<BinaryTree> &node, int value);
  void print_inorder_recursive(const BinaryTree *node);

  std::unique_ptr<BinaryTree>
  build_balanced_bst(const std::vector<int> &sorted_values, int start, int end);
  const BinaryTree *search_recursive(const BinaryTree *node, int key);

  int height_recursive(const BinaryTree *node);
};

#endif
