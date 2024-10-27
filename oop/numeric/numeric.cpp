#include "numeric.hpp"

#include <sstream>
#include <typeinfo>
// static_cast
// URL:https://learn.microsoft.com/ja-jp/cpp/cpp/static-cast-operator?view=msvc-170
char Numeric::get_byte() const {
  return static_cast<char>(this->get_integer());
}

short Numeric::get_short() const {
  return static_cast<short>(this->get_integer());
}

long Numeric::get_long() const {
  return static_cast<long>(this->get_integer());
}

char Numeric::get_char() const {
  return static_cast<char>(this->get_integer());
}

std::string Numeric::to_string() const {
  std::ostringstream oss;
  oss << typeid(*this).name() << " of int value:" << this->get_integer();
  return oss.str();
}
