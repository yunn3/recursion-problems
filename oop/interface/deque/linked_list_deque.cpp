#include "linked_list_deque.hpp"

#include <stdexcept>

LinkedListDeque::LinkedListDeque() = default;
LinkedListDeque::~LinkedListDeque() = default;

int LinkedListDeque::peek_last() const {
  if (data_.empty()) {
    throw std::out_of_range("Deque is empty");
  }
  return data_.back();
}

int LinkedListDeque::pop() {
  if (data_.empty()) {
    throw std::out_of_range("Deque is empty");
  }
  int value = data_.back();
  data_.pop_back();
  return value;
}

void LinkedListDeque::push(int value) { data_.push_back(value); }

int LinkedListDeque::peek_first() const {
  if (data_.empty()) {
    throw std::out_of_range("Deque is empty");
  }
  return data_.front();
}

int LinkedListDeque::poll() {
  if (data_.empty()) {
    throw std::out_of_range("Deque is empty");
  }
  int value = data_.front();
  data_.pop_front();
  return value;
}

void LinkedListDeque::add_first(int value) { data_.push_front(value); }
