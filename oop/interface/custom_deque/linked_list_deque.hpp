#ifndef LINKED_LIST_DEQUE_HPP
#define LINKED_LIST_DEQUE_HPP

#include <memory>
#include <vector>

#include "abstract_list_integer.hpp"
#include "deque.hpp"

class LinkedListDeque : public Deque, public AbstractListInteger {
 public:
  LinkedListDeque();
  ~LinkedListDeque() override = default;

  int peek_last() const override;
  int pop() override;
  void push(int value) override;
  int peek_first() const override;
  int poll() override;
  void add_first(int value) override;
  void add(int value) override;
  int size() const override;
  std::vector<int> to_vector() const override;

 private:
  struct Node {
    int data;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;

    Node(int value) : data(value), next(nullptr), prev() {}
  };

  std::shared_ptr<Node> head_;
  std::shared_ptr<Node> tail_;
};

#endif
