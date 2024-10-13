#include "integer_array_list.hpp"

#include <memory>
#include <stdexcept>

IntegerArrayList::IntegerArrayList() : AbstractListInteger() {
  data = get_initial_list();
}

IntegerArrayList::IntegerArrayList(const std::vector<int>& arr)
    : AbstractListInteger(arr) {
  data = get_initial_list();
}

int IntegerArrayList::get(int position) const {
  if (position < 0 || position >= static_cast<int>(data.size())) {
    throw std::out_of_range("Index out of bounds");
  }
  return data[position];
}

void IntegerArrayList::add(int element) { data.push_back(element); }

void IntegerArrayList::add(const std::vector<int>& elements) {
  data.insert(data.end(), elements.begin(), elements.end());
}

int IntegerArrayList::pop() {
  if (data.empty()) {
    throw std::out_of_range("No elements to pop");
  }
  int value = data.back();
  data.pop_back();
  return value;
}

void IntegerArrayList::add_at(int position, int element) {
  if (position < 0 || position > static_cast<int>(data.size())) {
    throw std::out_of_range("Index out of bounds");
  }
  data.insert(data.begin() + position, element);
}

void IntegerArrayList::add_at(int position, const std::vector<int>& elements) {
  if (position < 0 || position > static_cast<int>(data.size())) {
    throw std::out_of_range("Index out of bounds");
  }
  data.insert(data.begin() + position, elements.begin(), elements.end());
}

int IntegerArrayList::remove_at(int position) {
  if (position < 0 || position >= static_cast<int>(data.size())) {
    throw std::out_of_range("Index out of bounds");
  }
  int value = data[position];
  data.erase(data.begin() + position);
  return value;
}

void IntegerArrayList::remove_all_at(int start) {
  if (start < 0 || start > static_cast<int>(data.size())) {
    throw std::out_of_range("Index out of bounds");
  }
  data.erase(data.begin() + start, data.end());
}

void IntegerArrayList::remove_all_at(int start, int end) {
  if (start < 0 || end > static_cast<int>(data.size()) || start > end) {
    throw std::out_of_range("Invalid range");
  }
  data.erase(data.begin() + start, data.begin() + end);
}

std::unique_ptr<AbstractListInteger> IntegerArrayList::sub_list(
    int start) const {
  if (start < 0 || start > static_cast<int>(data.size())) {
    throw std::out_of_range("Index out of bounds");
  }
  std::vector<int> sub(data.begin() + start, data.end());
  return std::make_unique<IntegerArrayList>(sub);
}

std::unique_ptr<AbstractListInteger> IntegerArrayList::sub_list(int start,
                                                                int end) const {
  if (start < 0 || end > static_cast<int>(data.size()) || start > end) {
    throw std::out_of_range("Invalid range");
  }
  std::vector<int> sub(data.begin() + start, data.begin() + end);
  return std::make_unique<IntegerArrayList>(sub);
}

std::vector<int> IntegerArrayList::to_vector() const { return data; }

int IntegerArrayList::size() const { return static_cast<int>(data.size()); }

void IntegerArrayList::add_at(int index, const AbstractListInteger& elements) {
  std::vector<int> vecElements = elements.to_vector();
  add_at(index, vecElements);
}
