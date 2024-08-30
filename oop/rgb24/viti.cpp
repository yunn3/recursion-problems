#include <bitset>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class RGB24 {
 public:
  RGB24(int red, int green, int blue);
  ~RGB24();

  string get_hex();
  string get_bits();
  string get_color_shade();

 private:
  int red_;
  int green_;
  int blue_;

  bool is_gray_scale_() { return red_ == green_ && green_ == blue_; }
};

RGB24::RGB24(int red, int green, int blue)
    : red_(red), green_(green), blue_(blue) {
  cout << "RGB24 constructor called" << endl;
}

RGB24::~RGB24() { cout << "RGB24 destructor called" << endl; }

string RGB24::get_hex() {
  ostringstream stream;
  stream << setfill('0') << setw(2) << hex << red_;
  stream << setfill('0') << setw(2) << hex << green_;
  stream << setfill('0') << setw(2) << hex << blue_;
  return stream.str();
}

string RGB24::get_bits() {
  ostringstream stream;
  stream << bitset<8>(red_);
  stream << bitset<8>(green_);
  stream << bitset<8>(blue_);
  return stream.str();
}

string RGB24::get_color_shade() {
  if (is_gray_scale_()) return "grayscale";

  string greatest_string = "red";
  int greatest = red_;

  if (green_ > greatest) {
    greatest_string = "green";
    greatest = green_;
  }

  if (blue_ > greatest) {
    greatest_string = "blue";
    greatest = blue_;
  }

  return greatest_string;
}

int main() {
  RGB24 rgb_24(100, 100, 100);
  cout << rgb_24.get_hex() << endl;
  cout << rgb_24.get_bits() << endl;
  cout << rgb_24.get_color_shade() << endl;
  return 0;
}