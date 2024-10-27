#ifndef BIG_DECIMAL_NUMERIC_HPP
#define BIG_DECIMAL_NUMERIC_HPP

#include <string>

#include "numeric.hpp"

class BigDecimalNumeric : public Numeric {
 public:
  explicit BigDecimalNumeric(const std::string& value_str);

  int get_integer() const override;
  double get_double() const override;
  BigDecimalNumeric add(const BigDecimalNumeric& other) const;
  std::string to_string() const override;

 private:
  std::string value_;
  std::string add_strings(const std::string& num1,
                          const std::string& num2) const;
  bool is_valid_number(const std::string& str) const;
};
#endif
