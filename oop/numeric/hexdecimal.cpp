#include "hexdecimal.hpp"

#include <sstream>
#include <string>

Hexdecimal::Hexdecimal(const std::string& hex_value) : hex_value_(hex_value) {}

int Hexdecimal::get_integer() const {
  int value = 0;
  std::istringstream iss(hex_value_);
  iss >> std::hex >> value;
  return value;
}

double Hexdecimal::get_double() const {
  return static_cast<double>(get_integer());
}

char Hexdecimal::get_byte() const {
  return static_cast<char>(get_integer() & 0xFF);
}

short Hexdecimal::get_short() const {
  return static_cast<short>(get_integer() & 0xFFFF);
}

long Hexdecimal::get_long() const { return static_cast<long>(get_integer()); }

char Hexdecimal::get_char() const {
  return static_cast<char>(get_integer() & 0x7F);
}

std::string Hexdecimal::to_string() const {
  return "Hexdecimal of int value: " + std::to_string(get_integer());
}
