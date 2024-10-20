#include <iostream>

#include "linked_list_deque.hpp"

int main() {
  LinkedListDeque deque;

  deque.push(1);
  deque.push(2);
  deque.add_first(0);

  std::cout << "First element: " << deque.peek_first() << std::endl;
  std::cout << "Last element: " << deque.peek_last() << std::endl;

  std::cout << "Poll: " << deque.poll() << std::endl;
  std::cout << "Pop: " << deque.pop() << std::endl;

  std::cout << "First element: " << deque.peek_first() << std::endl;

  return 0;
}
