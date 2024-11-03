#include "binary_tree.hpp"
#include <iostream>

int main() {
  BinarySearchTree balancedBST({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11});

  std::cout << std::boolalpha;
  std::cout << "Key 6 exists: " << balancedBST.KeyExists(6) << std::endl;
  std::cout << "Serach key 6: " << (balancedBST.search(6) != nullptr)
            << std::endl;

  std::cout << "Key 2 exists: " << balancedBST.KeyExists(2) << std::endl;
  std::cout << "Search Key 2: " << (balancedBST.search(2) != nullptr)
            << std::endl;

  std::cout << "Search key 34: " << (balancedBST.search(34) != nullptr)
            << std::endl;

  std::cout << "Tree height: " << balancedBST.height() << std::endl;
  return 0;
}
