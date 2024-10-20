#ifndef NAMED_HPP
#define NAMED_HPP
#include <string>

class Named {
 public:
  virtual ~Named() = default;
  virtual std::string name() const = 0;
};

#endif
