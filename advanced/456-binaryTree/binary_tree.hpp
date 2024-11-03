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

  BinarySearchTree(const std::vector<int> &values);

  const BinaryTree *search(int key);
  bool KeyExists(int key);

  int height();

private:
  std::unique_ptr<BinaryTree>
  buildBalancedBST(const std::vector<int> &sorted_values, int start, int end);
  const BinaryTree *searchRecursive(const BinaryTree *node, int key);

  int heightRecursive(const BinaryTree *node);
};

#endif
