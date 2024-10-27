#include "char_numeric.hpp"

CharNumeric::CharNumeric(char c) : c_(c) {}

CharNumeric::CharNumeric(int c) : c_(static_cast<char>(c)) {}

char CharNumeric::get_byte() const { return c_; }

short CharNumeric::get_short() const { return static_cast<short>(c_); }

long CharNumeric::get_long() const { return static_cast<long>(c_); }

char CharNumeric::get_char() const { return c_; }

int CharNumeric::get_integer() const { return static_cast<int>(c_); }

double CharNumeric::get_double() const {
  return static_cast<double>(get_integer());
}
