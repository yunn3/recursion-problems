#ifndef DEQUE_HPP
#define DEQUE_HPP

#include "queue.hpp"
#include "stack.hpp"

class Deque : public Stack, public Queue {
 public:
  virtual ~Deque() = default;

  virtual void add_first(int value) = 0;
};

#endif
