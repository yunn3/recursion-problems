#include <cmath>
#include <deque>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

class BinaryTree {
public:
  int data;
  BinaryTree *left;
  BinaryTree *right;
  BinaryTree(int value) {
    this->data = value;
    this->left = nullptr;
    this->right = nullptr;
  };

  BinaryTree(int value, BinaryTree *left, BinaryTree *right) {
    this->data = value;
    this->left = left;
    this->right = right;
  };
};

bool is_unival_tree(BinaryTree *node, int value) {
  if (node == nullptr)
    return true;
  if (node->data != value)
    return false;
  return is_unival_tree(node->left, value) &&
         is_unival_tree(node->right, value);
}

bool treeWithTheSameValue(BinaryTree *root) {
  if (root == nullptr)
    return true;
  return is_unival_tree(root, root->data);
}
