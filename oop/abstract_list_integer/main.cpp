#include <iostream>
#include <memory>

#include "abstract_list_integer.hpp"
#include "integer_array_list.hpp"
#include "integer_linked_list.hpp"

void test_list_integer(AbstractListInteger& int_list) {
  int_list.add(1);
  int_list.add(2);
  int_list.add(3);
  std::vector<int> elements = {4, 5, 6};
  int_list.add(elements);
  int_list.add_at(2, 10);

  std::cout << "IntegerArrayList elements: ";
  for (int i = 0; i < int_list.size(); i++) {
    std::cout << int_list.get(i) << " ";
  }
  std::cout << std::endl;

  std::unique_ptr<AbstractListInteger> sub_array_list = int_list.sub_list(2, 5);
  std::cout << "Sublist of IntegerArrayList: ";
  for (int i = 0; i < sub_array_list->size(); i++) {
    std::cout << sub_array_list->get(i) << " ";
  }
  std::cout << std::endl;

  IntegerArrayList array_list;
  array_list.add(100);
  array_list.add(200);
  array_list.add(300);
  int index = 2;
  array_list.add_at(index, int_list);

  std::cout << "IntegerArrayList after adding array_list at index" << index
            << ": ";
  for (int i = 0; i < array_list.size(); i++) {
    std::cout << array_list.get(i) << " ";
  }
  std::cout << std::endl;
}

int main() {
  IntegerArrayList array_list;
  IntegerLinkedList linked_list;
  std::cout << "test array_list" << std::endl;
  test_list_integer(array_list);

  std::cout << "test linked_list" << std::endl;
  test_list_integer(linked_list);
  return 0;
}
