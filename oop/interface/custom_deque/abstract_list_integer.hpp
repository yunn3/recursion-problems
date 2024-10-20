#ifndef ABSTRACT_LIST_INTEGER_HPP
#define ABSTRACT_LIST_INTEGER_HPP

#include <vector>
class AbstractListInteger {
 public:
  virtual ~AbstractListInteger() = default;
  virtual void add(int value) = 0;
  virtual int size() const = 0;
  virtual std::vector<int> to_vector() const = 0;
};

#endif
