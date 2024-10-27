#include "integer_linked_list.hpp"

#include <memory>
#include <stdexcept>
IntegerLinkedList::IntegerLinkedList() : AbstractListInteger() {
  data.insert(data.end(), get_initial_list().begin(), get_initial_list().end());
}

IntegerLinkedList::IntegerLinkedList(const std::vector<int>& arr)
    : AbstractListInteger(arr) {
  data.insert(data.end(), get_initial_list().begin(), get_initial_list().end());
}

int IntegerLinkedList::get(int position) const {
  if (position < 0 || position >= data.size()) {
    throw std::out_of_range("Index out of bounds");
  }
  auto it = data.begin();
  std::advance(it, position);
  return *it;
}

void IntegerLinkedList::add(int element) { data.push_back(element); }

void IntegerLinkedList::add(const std::vector<int>& elements) {
  data.insert(data.end(), elements.begin(), elements.end());
}

int IntegerLinkedList::pop() {
  if (data.empty()) {
    throw std::out_of_range("No elements to pop");
  }
  int value = data.back();
  data.pop_back();
  return value;
}

void IntegerLinkedList::add_at(int position, int element) {
  if (position < 0 || position > data.size()) {
    throw std::out_of_range("Index out of bounds");
  }
  auto it = data.begin();
  std::advance(it, position);
  data.insert(it, element);
}

void IntegerLinkedList::add_at(int position, const std::vector<int>& elements) {
  if (position < 0 || position > data.size()) {
    throw std::out_of_range("Index out of bounds");
  }
  auto it = data.begin();
  std::advance(it, position);
  data.insert(it, elements.begin(), elements.end());
}

int IntegerLinkedList::remove_at(int position) {
  if (position < 0 || position >= data.size()) {
    throw std::out_of_range("Index out of bounds");
  }
  auto it = data.begin();
  std::advance(it, position);
  int value = *it;
  data.erase(it);
  return value;
}

void IntegerLinkedList::remove_all_at(int start) {
  if (start < 0 || start > data.size()) {
    throw std::out_of_range("Index out of bounds");
  }
  auto it = data.begin();
  std::advance(it, start);
  data.erase(it, data.end());
}

void IntegerLinkedList::remove_all_at(int start, int end) {
  if (start < 0 || end > data.size() || start > end) {
    throw std::out_of_range("Invalid range");
  }
  auto it_start = data.begin();
  auto it_end = data.begin();
  std::advance(it_start, start);
  std::advance(it_end, end);
  data.erase(it_start, it_end);
}

std::unique_ptr<AbstractListInteger> IntegerLinkedList::sub_list(
    int start) const {
  if (start < 0 || start > data.size()) {
    throw std::out_of_range("Index out of bounds");
  }
  auto it = data.begin();
  std::advance(it, start);
  std::vector<int> sub(it, data.end());
  return std::make_unique<IntegerLinkedList>(sub);
}

std::unique_ptr<AbstractListInteger> IntegerLinkedList::sub_list(
    int start, int end) const {
  if (start < 0 || end > data.size() || start > end) {
    throw std::out_of_range("Invalid range");
  }
  auto it_start = data.begin();
  auto it_end = data.begin();
  std::advance(it_start, start);
  std::advance(it_end, end);
  std::vector<int> sub(it_start, it_end);
  return std::make_unique<IntegerLinkedList>(sub);
}

std::vector<int> IntegerLinkedList::to_vector() const {
  return std::vector<int>(data.begin(), data.end());
}

int IntegerLinkedList::size() const { return data.size(); }

void IntegerLinkedList::add_at(int index, const AbstractListInteger& elements) {
  std::vector<int> vec_elements = elements.to_vector();
  add_at(index, vec_elements);
}
