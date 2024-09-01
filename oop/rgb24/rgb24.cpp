#include <bitset>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

class RGB24 {
 public:
  RGB24(int red, int green, int blue) : red_(red), green_(green), blue_(blue) {}
  string get_hex() {
    ostringstream oss;
    oss << setfill('0') << setw(2) << hex << red_;
    oss << setfill('0') << setw(2) << hex << green_;
    oss << setfill('0') << setw(2) << hex << blue_;
    return oss.str();
  }

  string get_bits() {
    ostringstream oss;
    oss << bitset<8>(red_);
    oss << bitset<8>(green_);
    oss << bitset<8>(blue_);
    return oss.str();
  }

  set_as_black() {}
  string get_color_shade() {
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

 private:
  int red_;
  int green_;
  int blue_;

  bool is_gray_scale_() { return red_ == green_ && green_ == blue_; }
};

int main() {
  RGB24 rgb_24(255, 255, 255);
  cout << rgb_24.get_hex() << endl;
  cout << rgb_24.get_bits() << endl;
  cout << rgb_24.get_color_shade() << endl;
  return 0;
}