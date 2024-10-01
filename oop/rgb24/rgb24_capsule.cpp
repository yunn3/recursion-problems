#include <algorithm>
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
  void set_color_by_bin(string bin_code);
  friend ostream& operator<<(ostream& os, const RGB24& obj);

 private:
  string rgb_hex_;

  void parse_rgb_hex_();
  int get_red_() const;
  int get_green_() const;
  int get_blue_() const;
  bool is_gray_scale_() const;
};

RGB24::RGB24(int red, int green, int blue) {
  ostringstream stream;
  stream << setfill('0') << setw(2) << hex << red;
  stream << setfill('0') << setw(2) << hex << green;
  stream << setfill('0') << setw(2) << hex << blue;
  rgb_hex_ = stream.str();
}

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

string RGB24::get_hex() const { return rgb_hex_; }

string RGB24::get_bits() const {
  ostringstream stream;
  stream << bitset<8>(get_red_());
  stream << bitset<8>(get_green_());
  stream << bitset<8>(get_blue_());
  return stream.str();
}

string RGB24::get_color_shade() const {
  if (is_gray_scale_()) return "grayscale";

  array<string, 3> color_str_table = {"red", "green", "blue"};
  array<int, 3> color_values = {get_red_(), get_green_(), get_blue_()};
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

void RGB24::set_as_black() { rgb_hex_ = "000000"; }

void RGB24::set_color_by_hex(string hex_code) {
  if (hex_code.size() != 6) {
    set_as_black();
    return;
  }
  rgb_hex_ = hex_code;
  transform(rgb_hex_.begin(), rgb_hex_.end(), rgb_hex_.begin(), ::tolower);
}

void RGB24::set_color_by_bin(string bin_code) {
  if (bin_code.size() != 24) {
    set_as_black();
    return;
  }
  ostringstream stream;
  for (int i = 0; i < 3; i++) {
    int color_value = stoi(bin_code.substr(i * 8, 8), nullptr, 2);
    stream << setfill('0') << setw(2) << hex << color_value;
  }
  rgb_hex_ = stream.str();
}

ostream& operator<<(ostream& os, const RGB24& obj) {
  os << "The color is rgb(";
  os << obj.get_red_() << ", ";
  os << obj.get_green_() << ", ";
  os << obj.get_blue_() << "), ";
  os << "Hex: " << obj.get_hex() << ", ";
  os << "Binary: " << obj.get_bits() << " ";
  return os;
}

int RGB24::get_red_() const { return stoi(rgb_hex_.substr(0, 2), nullptr, 16); }

int RGB24::get_green_() const {
  return stoi(rgb_hex_.substr(2, 2), nullptr, 16);
}

int RGB24::get_blue_() const {
  return stoi(rgb_hex_.substr(4, 2), nullptr, 16);
}

bool RGB24::is_gray_scale_() const {
  return get_red_() == get_green_() && get_green_() == get_blue_();
}
int main() {
  RGB24 color_1(0, 153, 255);
  RGB24 color_2("ff99cc");
  RGB24 color_3("100110011111111100110011");
  RGB24 gray("7b7b7b");
  cout << color_1 << endl;
  cout << color_2 << endl;
  cout << color_3 << endl;
  cout << gray << endl;

  cout << endl << "Changin the state of colors." << endl;

  gray.set_as_black();
  cout << gray << endl;

  color_1.set_color_by_hex("2EB656");
  cout << color_1 << endl;
  return 0;
}
