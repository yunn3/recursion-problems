#include "linked_list_deque.hpp"

#include <memory>
#include <stdexcept>

LinkedListDeque::LinkedListDeque() : head_(nullptr), tail_(nullptr) {}

int LinkedListDeque::peek_last() const {
  if (!tail_) {
    throw std::out_of_range("Deque is empty");
  }
  return tail_->data;
}

int LinkedListDeque::pop() {
  if (!tail_) {
    throw std::out_of_range("Deque is empty");
  }
  int value = tail_->data;
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

void LinkedListDeque::push(int value) {
  auto new_node = std::make_shared<Node>(value);
  new_node->prev = tail_;
  if (tail_) {
    tail_->next = new_node;
  } else {
    head_ = new_node;
  }
  tail_ = new_node;
}

int LinkedListDeque::peek_first() const {
  if (!head_) {
    throw std::out_of_range("Deque is empty");
  }
  return head_->data;
}

int LinkedListDeque::poll() {
  if (!head_) {
    throw std::out_of_range("Deque is empty");
  }
  int value = head_->data;
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

void LinkedListDeque::add_first(int value) {
  auto new_node = std::make_shared<Node>(value);
  new_node->next = head_;
  if (head_) {
    head_->prev = new_node;
  } else {
    tail_ = new_node;
  }
  head_ = new_node;
}
void LinkedListDeque::add(int value) { push(value); }
int LinkedListDeque::size() const {
  int count = 0;
  auto current = head_;
  while (current) {
    count++;
    current = current->next;
  }
  return count;
}

std::vector<int> LinkedListDeque::to_vector() const {
  std::vector<int> result;
  auto current = head_;
  while (current) {
    result.push_back(current->data);
    current = current->next;
  }
  return result;
}
