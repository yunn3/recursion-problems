#include "big_decimal_numeric.hpp"

#include <algorithm>
#include <cctype>
#include <cstddef>
#include <regex>
#include <stdexcept>

BigDecimalNumeric::BigDecimalNumeric(const std::string& value_str) {
  if (!is_valid_number(value_str)) {
    throw std::invalid_argument("Invalid numeric format: " + value_str);
  }
  value_ = value_str;
}

bool BigDecimalNumeric::is_valid_number(const std::string& str) const {
  static const std::regex number_regex(R"(^-?\d+(\.\d+)?$)");
  return std::regex_match(str, number_regex);
}

int BigDecimalNumeric::get_integer() const {
  double num = std::stod(value_);
  return static_cast<int>(num);
}

double BigDecimalNumeric::get_double() const { return std::stod(value_); }

char Big std::string BigDecimalNumeric::add_strings(
    const std::string& num1, const std::string& num2) const {
  //整数部分と小数部分に分割したい
  auto split_num =
      [](const std::string& num) -> std::pair<std::string, std::string> {
    size_t dot_position = num.find(".");
    if (dot_position == std::string::npos) {
      return {num, ""};
    } else {
      return {num.substr(0, dot_position), num.substr(dot_position + 1)};
    }
  };

  auto [int_part1, frac_part1] = split_num(num1);
  auto [int_part2, frac_part2] = split_num(num2);

  //小数部分の桁数を揃えたい
  size_t max_frac_len = std::max(frac_part1.length(), frac_part2.length());
  frac_part1.append(max_frac_len - frac_part1.length(), '0');
  frac_part2.append(max_frac_len - frac_part2.length(), '0');

  //小数部分の加算をする
  std::string frac_sum;
  int carry = 0;
  for (int i = static_cast<int>(max_frac_len) - 1; i >= 0; i--) {
    int digit_sum = (frac_part1[i] - '0') + frac_part2[i] - '0' + carry;
    carry = digit_sum / 10;
    frac_sum.insert(frac_sum.begin(), (digit_sum % 10) + '0');
  }

  //整数部分の桁数を揃えたい
  size_t max_int_len = std::max(int_part1.length(), int_part2.length());
  int_part1.insert(0, max_int_len - int_part1.length(), '0');
  int_part2.insert(0, max_int_len - int_part2.length(), '0');

  //整数部分の加算をする
  std::string int_sum;
  for (int i = static_cast<int>(max_int_len) - 1; i >= 0; i--) {
    int digit_sum = (int_part1[i] - '0') + (int_part2[i] - '0') + carry;
    carry = digit_sum / 10;
    int_sum.insert(int_sum.begin(), (digit_sum % 10) + '0');
  }
  if (carry > 0) {
    int_sum.insert(int_sum.begin(), carry + '0');
  }

  std::string result = int_sum;
  if (!frac_sum.empty()) {
    result += "." + frac_sum;
  }

  while (result.size() > 1 && result[0] == '0' && result[1] != '.') {
    result.erase(0, 1);
  }

  if (result.find('.') != std::string::npos) {
    while (result.back() == '0') {
      result.pop_back();
    }
    if (result.back() == '.') {
      result.pop_back();
    }
  }
  return result;
}

std::string BigDecimalNumeric::to_string() const {
  return "BigDecimalNumeric of value: " + value_;
}
