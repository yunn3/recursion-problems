#include <iostream>
#include <memory>

class BinaryTree {
public:
  int data;
  std::unique_ptr<BinaryTree> left;
  std::unique_ptr<BinaryTree> right;

  explicit BinaryTree(int value) : data(value) {}
};

int main() {
  auto binary_tree = std::make_unique<BinaryTree>(10);
  binary_tree->left = std::make_unique<BinaryTree>(6);
  binary_tree->right = std::make_unique<BinaryTree>(8);

  std::cout << binary_tree->data << std::endl;
  std::cout << binary_tree->left->data << std::endl;
  std::cout << binary_tree->right->data << std::endl;

  return 0;
}
