#include "abstract_list_integer.hpp"

AbstractListInteger::AbstractListInteger() : initial_list() {}

AbstractListInteger::AbstractListInteger(const std::vector<int>& arr)
    : initial_list(arr) {}

std::vector<int> AbstractListInteger::get_original_list() const {
  return initial_list;
}

const std::vector<int>& AbstractListInteger::get_initial_list() const {
  return initial_list;
}
