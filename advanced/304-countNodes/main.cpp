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
  BinaryTree(int value) { this->data = value; };
  BinaryTree(int value, BinaryTree *left, BinaryTree *right) {
    this->data = value;
    this->left = left;
    this->right = right;
  };
};

int count_nodes(BinaryTree *root) {
  if (!root)
    return 0;

  BinaryTree *left = root;
  BinaryTree *right = left;
  int left_height = 0;
  int right_height = 0;

  while (left) {
    left_height++;
    left = left->left;
  }

  while (right) {
    right_height++;
    right = right->right;
  }

  if (left_height == right_height) {
    return (1 << left_height) - 1;
  } else {
    return 1 + count_nodes(root->left) + count_nodes(root->right);
  }
}
