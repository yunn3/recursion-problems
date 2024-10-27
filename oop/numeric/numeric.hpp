#ifndef NUMERIC_HPP
#define NUMERIC_HPP

#include <string>

class Numeric {
 public:
  virtual ~Numeric() {}

  virtual char get_byte() const = 0;
  virtual short get_short() const = 0;
  virtual long get_long() const = 0;
  virtual char get_char() const = 0;

  virtual int get_integer() const = 0;
  virtual double get_double() const = 0;

  virtual std::string to_string() const;
};

#endif
