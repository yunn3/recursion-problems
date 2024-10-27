#include "octaldecimal.hpp"

#include <sstream>
#include <string>

Octaldecimal::Octaldecimal(const std::string& oct_value)
    : oct_value_(oct_value) {}

int Octaldecimal::get_integer() const {
  int value = 0;
  std::istringstream iss(oct_value_);
  iss >> std::oct >> value;
  return value;
}

double Octaldecimal::get_double() const {
  return static_cast<double>(get_integer());
}

char Octaldecimal::get_byte() const {
  return static_cast<char>(get_integer() & 0xFF);
}

short Octaldecimal::get_short() const {
  return static_cast<short>(get_integer() & 0xFFFF);
}

long Octaldecimal::get_long() const { return static_cast<long>(get_integer()); }

char Octaldecimal::get_char() const {
  return static_cast<char>(get_integer() & 0x7F);
}

std::string Octaldecimal::to_string() const {
  return "Octaldecimal of int value: " + std::to_string(get_integer());
}
