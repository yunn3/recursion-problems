#include <iostream>
#include <string>

#include "big_decimal_numeric.hpp"
#include "char_numeric.hpp"
#include "hexdecimal.hpp"
#include "integer_numeric.hpp"
#include "octaldecimal.hpp"

using std::cout;
using std::endl;

void numeric_printer(const Numeric& num) {
  cout << num.to_string() << endl;
  cout << "Byte: " << static_cast<int>(num.get_byte()) << endl;
  cout << "Short: " << num.get_short() << endl;
  cout << "Long: " << num.get_long() << endl;
  cout << "Char: " << num.get_char() << endl;
  cout << "Double: " << num.get_double() << endl;
  cout << endl;
}

int main() {
  IntegerNumeric num1(73);
  IntegerNumeric num2(23555461);
  CharNumeric num3(61);

  numeric_printer(num1);
  numeric_printer(num2);
  numeric_printer(num3);

  std::string hex_code = "1A";
  Hexdecimal hex_num(hex_code);
  numeric_printer(hex_num);

  Octaldecimal oct_num("25");
  numeric_printer(oct_num);

  BigDecimalNumeric big_num1("394.4555643321");
  BigDecimalNumeric big_num2("100.123456789");
  BigDecimalNumeric big_sum = big_num1.add(big_num2);

  numeric_printer(big_num1);
  numeric_printer(big_num2);
  numeric_printer(big_sum);

  return 0;
}
