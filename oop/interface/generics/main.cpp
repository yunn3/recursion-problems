#include <iostream>
#include <stdexcept>

#include "linked_list_deque.hpp"

template <typename T>
void queue_print(Queue<T>& queue) {
  while (true) {
    try {
      T value = queue.poll();
      std::cout << value << " -> ";
    } catch (const std::out_of_range& e) {
      std::cout << "NULL" << std::endl;
      break;
    }
  }
}

template <typename T>
void stack_print(Stack<T>& stack) {
  while (true) {
    try {
      T value = stack.pop();
      std::cout << value << " -> ";
    } catch (const std::out_of_range& e) {
      std::cout << "NULL" << std::endl;
      break;
    }
  }
}

int main() {
  LinkedListDeque<int> stack_deque_int;
  stack_deque_int.push(10);
  stack_deque_int.push(20);
  stack_deque_int.push(30);

  std::cout << "Stack Output (int):" << std::endl;
  stack_print(stack_deque_int);

  LinkedListDeque<int> queue_deque_int;
  queue_deque_int.push(10);
  queue_deque_int.push(20);
  queue_deque_int.push(30);

  std::cout << "Queue Output (int):" << std::endl;
  queue_print(queue_deque_int);

  LinkedListDeque<double> stack_deque_double;
  stack_deque_double.push(5.5);
  stack_deque_double.push(10.1);
  stack_deque_double.push(15.2);

  std::cout << "Stack Output (double):" << std::endl;
  stack_print(stack_deque_double);

  LinkedListDeque<double> queue_deque_double;
  queue_deque_double.push(5.5);
  queue_deque_double.push(10.1);
  queue_deque_double.push(15.2);

  std::cout << "Queue Output (double):" << std::endl;
  queue_print(queue_deque_double);

  return 0;
}
