#ifndef DEQUE_HPP
#define DEQUE_HPP

#include "queue.hpp"
#include "stack.hpp"

template <typename T>
class Deque : public Stack<T>, public Queue<T> {
 public:
  virtual ~Deque() = default;

  virtual void add_first(T value) = 0;
};

#endif
