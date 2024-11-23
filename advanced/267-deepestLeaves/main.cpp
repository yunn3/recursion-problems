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

void dfs(BinaryTree *node, int depth, int &max_depth, int &sum) {
  if (node == nullptr)
    return;

  if (node->left == nullptr && node->right == nullptr) {
    if (depth > max_depth) {
      max_depth = depth;
      sum = node->data;
    } else if (depth == max_depth) {
      sum += node->data;
    }
  }
  dfs(node->left, depth + 1, max_depth, sum);
  dfs(node->right, depth + 1, max_depth, sum);
}
int deepestLeaves(BinaryTree *root) {
  int max_depth = -1;
  int sum = 0;

  dfs(root, 0, max_depth, sum);

  return sum;
}
