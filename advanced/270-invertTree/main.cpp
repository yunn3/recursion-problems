#include <cmath>
#include <cstddef>
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

BinaryTree *invertTree(BinaryTree *root) {
  if (root == nullptr)
    return nullptr;

  BinaryTree *temp = root->left;
  root->left = invertTree(root->right);
  root->right = invertTree(temp);

  return root;
}
