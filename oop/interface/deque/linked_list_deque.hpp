#ifndef LINKED_LIST_DEQUE_HPP
#define LINKED_LIST_DEQUE_HPP

#include <deque>

#include "deque.hpp"

class LinkedListDeque : public Deque {
 public:
  LinkedListDeque();
  ~LinkedListDeque() override;

  int peek_last() const override;
  int pop() override;
  void push(int value) override;

  int peek_first() const override;
  int pollll() override;

  void add_first(int value) override;

 private:
  std::deque<int> data_;
};

#endif
