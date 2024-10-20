#include <iostream>
#include <stdexcept>

#include "abstract_list_integer.hpp"
#include "deque.hpp"
#include "linked_list_deque.hpp"
#include "queue.hpp"
#include "stack.hpp"
void queue_print(Queue& queue) {
  while (true) {
    try {
      int value = queue.poll();
      std::cout << value << " -> ";
    } catch (const std::out_of_range& e) {
      std::cout << "NULL" << std::endl;
      break;
    }
  }
}

void stack_print(Stack& stack) {
  while (true) {
    try {
      int value = stack.pop();
      std::cout << value << " -> ";
    } catch (const std::out_of_range& e) {
      std::cout << "NULL" << std::endl;
      break;
    }
  }
}

void deque_print(Deque& deque) {
  try {
    int value = deque.poll();
    std::cout << value << std::endl;
    value = deque.pop();
    std::cout << value << std::endl;
  } catch (const std::out_of_range& e) {
    std::cout << e.what() << std::endl;
  }
}

void abstract_list_integer_print(AbstractListInteger& abs_list) {
  std::vector<int> elements = abs_list.to_vector();
  for (int value : elements) {
    std::cout << value << " -> ";
  }
  std::cout << std::endl;
}

int main() {
  std::vector<LinkedListDeque> deques;
  deques.push_back(LinkedListDeque());
  deques.push_back(LinkedListDeque());
  deques.push_back(LinkedListDeque());
  deques.push_back(LinkedListDeque());
  auto deque1 = LinkedListDeque();
  deque1.push(7);
  for (auto& deque : deques) {
    for (int i = 0; i < 10; i++) {
      deque.push(i);
    }
  }

  queue_print(deques[0]);
  stack_print(deques[1]);
  deque_print(deques[2]);
  deque_print(deque1);
  abstract_list_integer_print(deques[3]);

  return 0;
}
