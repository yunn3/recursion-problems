#include <cmath>
#include <deque>
#include <iostream>
#include <iterator>
#include <sstream>
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

void inorder_travarsal(BinaryTree *root, vector<int> &result) {
  if (root == nullptr)
    return;
  inorder_travarsal(root->left, result);
  result.push_back(root->data);
  inorder_travarsal(root->right, result);
}

vector<int> allElementsSorted(BinaryTree *root1, BinaryTree *root2) {
  vector<int> v1, v2;
  inorder_travarsal(root1, v1);
  inorder_travarsal(root2, v2);

  vector<int> merged;
  merged.reserve(v1.size() + v2.size());

  auto it1 = v1.begin(), end1 = v1.end();
  auto it2 = v2.begin(), end2 = v2.end();

  while (it1 != end1 && it2 != end2) {
    if (*it1 < *it2) {
      merged.push_back(*it1);
      it1++;
    } else {
      merged.push_back(*it2);
      it2++;
    }
  }

  merged.insert(merged.end(), it1, end1);
  merged.insert(merged.end(), it2, end2);

  return merged;
}
