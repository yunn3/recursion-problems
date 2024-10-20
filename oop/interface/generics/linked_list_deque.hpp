#ifndef LINKED_LIST_DEQUE_HPP
#define LINKED_LIST_DEQUE_HPP

#include <memory>
#include <stdexcept>
#include <vector>

#include "deque.hpp"

template <typename T>
class LinkedListDeque : public Deque<T> {
 public:
  LinkedListDeque();
  virtual ~LinkedListDeque() override = default;
  virtual T peek_last() const override;
  virtual T pop() override;
  virtual void push(T value) override;
  virtual T peek_first() const override;
  virtual T poll() override;
  virtual void add_first(T value) override;
  void add(T value);
  int size() const;
  std::vector<T> to_vector() const;

 private:
  struct Node {
    T data;
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;

    Node(T value) : data(value), next(nullptr), prev() {}
  };

  std::shared_ptr<Node> head_;
  std::shared_ptr<Node> tail_;
};

template <typename T>
LinkedListDeque<T>::LinkedListDeque() : head_(nullptr), tail_(nullptr) {}

template <typename T>
T LinkedListDeque<T>::peek_last() const {
  if (!tail_) {
    throw std::out_of_range("Deque is empty");
  }
  return tail_->data;
}

template <typename T>
T LinkedListDeque<T>::pop() {
  if (!tail_) {
    throw std::out_of_range("Deque is empty");
  }
  T value = tail_->data;
  auto prev_node = tail_->prev.lock();

  if (prev_node) {
    prev_node->next.reset();
    tail_ = prev_node;
  } else {
    head_.reset();
    tail_.reset();
  }
  return value;
}

template <typename T>
void LinkedListDeque<T>::push(T value) {
  auto new_node = std::make_shared<Node>(value);
  new_node->prev = tail_;
  if (tail_) {
    tail_->next = new_node;
  } else {
    head_ = new_node;
  }
  tail_ = new_node;
}

template <typename T>
T LinkedListDeque<T>::peek_first() const {
  if (!head_) {
    throw std::out_of_range("Deque is empty");
  }
  return head_->data;
}

template <typename T>
T LinkedListDeque<T>::poll() {
  if (!head_) {
    throw std::out_of_range("Deque is empty");
  }
  T value = head_->data;
  auto next_node = head_->next;

  if (next_node) {
    next_node->prev.reset();
    head_ = next_node;
  } else {
    head_.reset();
    tail_.reset();
  }
  return value;
}

template <typename T>
void LinkedListDeque<T>::add_first(T value) {
  auto new_node = std::make_shared<Node>(value);
  new_node->next = head_;
  if (head_) {
    head_->prev = new_node;
  } else {
    tail_ = new_node;
  }
  head_ = new_node;
}

template <typename T>
void LinkedListDeque<T>::add(T value) {
  push(value);
}

template <typename T>
int LinkedListDeque<T>::size() const {
  int count = 0;
  auto current = head_;
  while (current) {
    count++;
    current = current->next;
  }
  return count;
}

template <typename T>
std::vector<T> LinkedListDeque<T>::to_vector() const {
  std::vector<T> result;
  auto current = head_;
  while (current) {
    result.push_back(current->data);
    current = current->next;
  }
  return result;
}

#endif
