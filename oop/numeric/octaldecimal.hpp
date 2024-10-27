#ifndef OCTALDECIMAL_HPP
#define OCTALDECIMAL_HPP

#include <string>

#include "numeric.hpp"

class Octaldecimal : public Numeric {
 public:
  explicit Octaldecimal(const std::string& oct_value);

  char get_byte() const override;
  short get_short() const override;
  long get_long() const override;
  char get_char() const override;

  int get_integer() const override;
  double get_double() const override;

  std::string to_string() const override;

 private:
  std::string oct_value_;
};

#endif
