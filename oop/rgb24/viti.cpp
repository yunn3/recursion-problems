#include <array>
#include <bitset>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class RGB24 {
 public:
  RGB24(int red, int green, int blue);
  RGB24(string color_str);

  string get_hex() const;
  string get_bits() const;
  string get_color_shade() const;
  void set_as_black();
  void set_color_by_hex(string hex_code);
  void set_color_by_bin(string int_code);
  friend ostream& operator<<(ostream& os, const RGB24& obj);

 private:
  int red_;
  int green_;
  int blue_;

  bool is_gray_scale_() const { return red_ == green_ && green_ == blue_; }
};

RGB24::RGB24(string color_code) {
  int length = color_code.size();

  if (length == 6) {
    set_color_by_hex(color_code);
  } else if (length == 24) {
    set_color_by_bin(color_code);
  } else {
    set_as_black();
  }
}

string RGB24::get_hex() const {
  ostringstream stream;
  stream << setfill('0') << setw(2) << hex << red_;
  stream << setfill('0') << setw(2) << hex << green_;
  stream << setfill('0') << setw(2) << hex << blue_;
  return stream.str();
}

string RGB24::get_bits() const {
  ostringstream stream;
  stream << bitset<8>(red_);
  stream << bitset<8>(green_);
  stream << bitset<8>(blue_);
  return stream.str();
}

string RGB24::get_color_shade() const {
  if (is_gray_scale_()) return "grayscale";

  array<string, 3> color_str_table = {"red", "green", "blue"};
  array<int, 3> color_values = {red_, green_, blue_};
  int max_value = color_values[0];
  int max_index = 0;

  for (int i = 1; i < color_values.size(); i++) {
    if (max_value <= color_values[i]) {
      max_value = color_values[i];
      max_index = i;
    }
  }
  return color_str_table[max_index];
}

void RGB24::set_as_black() {
  red_ = 0;
  green_ = 0;
  blue_ = 0;
}

void RGB24::set_color_by_hex(string hex_code) {
  if (hex_code.size() != 6) {
    set_as_black();
    return;
  }
  array<int*, 3> color_values = {&red_, &green_, &blue_};
  stringstream ss;
  for (int i = 0; i < color_values.size(); i++) {
    ss << hex << hex_code.substr(i * 2, 2);
    ss >> *color_values[i];
  }
}

void RGB24::set_color_by_bin(string bin_code) {
  if (bin_code.size() != 24) {
    set_as_black();
    return;
  }
  array<int*, 3> color_values = {&red_, &green_, &blue_};
  for (int i = 0; i < color_values.size(); i++) {
    *(color_values[i]) = stoi(bin_code.substr(i * 8, 8), nullptr, 2);
  }
}

ostream& operator<<(ostream& os, const RGB24& obj) {
  os << "The color is rgb(";
  os << obj.red_ << ",";
  os << obj.green_ << ",";
  os << obj.blue_ << ").";
  os << "Hex: " << obj.get_hex() << ", ";
  os << "Binary: " << obj.get_bits() << " ";
  return os;
}

int main() {
  RGB24 color_1(0, 153, 255);
  RGB24 color_2("ff99cc");
  cout << color_1.get_color_shade() << endl;
  return 0;
}