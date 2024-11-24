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
  }

  BinaryTree(int value, BinaryTree *left, BinaryTree *right) {
    this->data = value;
    this->left = left;
    this->right = right;
  }

  ~BinaryTree() {
    delete left;
    delete right;
  }
};
BinaryTree *clone_tree(BinaryTree *root) {
  if (root == nullptr)
    return nullptr;
  BinaryTree *new_node = new BinaryTree(root->data);
  new_node->left = clone_tree(root->left);
  new_node->right = clone_tree(root->right);
  return new_node;
}

BinaryTree *mergeBST(BinaryTree *root1, BinaryTree *root2) {
  if (root1 == nullptr)
    return clone_tree(root2);
  if (root2 == nullptr)
    return clone_tree(root1);

  BinaryTree *merged_node = new BinaryTree(root1->data + root2->data);

  merged_node->left = mergeBST(root1->left, root2->left);
  merged_node->right = mergeBST(root1->right, root2->right);

  return merged_node;
}
