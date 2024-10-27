#include "integer_numeric.hpp"

#include <string>

IntegerNumeric::IntegerNumeric(int value) : value_(value) {}

char IntegerNumeric::get_byte() const { return static_cast<char>(value_); }

short IntegerNumeric::get_short() const {
  return static_cast<short>(value_ & 0xFFFF);
}

long IntegerNumeric::get_long() const { return static_cast<long>(value_); }

char IntegerNumeric::get_char() const {
  return static_cast<char>(value_ & 0x7F);
}

int IntegerNumeric::get_integer() const { return value_; }

double IntegerNumeric::get_double() const {
  return static_cast<double>(value_ & 0xFF);
}

std::string IntegerNumeric::to_string() const {
  return "IntegerNumeric of int value: " + std::to_string(value_);
}
