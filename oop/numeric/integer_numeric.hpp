#ifndef INTEGER_NUMERIC_HPP
#define INTEGER_NUMERIC_HPP

#include "numeric.hpp"

class IntegerNumeric : public Numeric {
 public:
  // explicitを使うことで、明示的な型変換しか受け付けないので、暗示的な型変換をしようとするとコンパイルエラーになる
  // URL: https://qiita.com/Suda00/items/11f57ce0d5e33ccb0fad
  explicit IntegerNumeric(int value);

  char get_byte() const override;
  short get_short() const override;
  long get_long() const override;
  char get_char() const override;

  int get_integer() const override;
  double get_double() const override;

  std::string to_string() const override;

 private:
  int value_;
};

#endif
