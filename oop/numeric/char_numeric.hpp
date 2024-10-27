#ifndef CHAR_NUMERIC_HPP
#define CHAR_NUMERIC_HPP

#include "numeric.hpp"

class CharNumeric : public Numeric {
 public:
  explicit CharNumeric(char c);
  explicit CharNumeric(int c);

  char get_byte() const override;
  short get_short() const override;
  long get_long() const override;
  char get_char() const override;

  int get_integer() const override;
  double get_double() const override;

 private:
  char c_;
};

#endif
