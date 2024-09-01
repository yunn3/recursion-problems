#include <array>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class Battery7v {
 public:
  Battery7v(string manufacturer, string model, double amp_hour,
            double weight_kg, double wMm, double hMm, double dMm)
      : manufacturer_(manufacturer),
        model_(model),
        amp_hour_(amp_hour),
        weight_kg_(weight_kg),
        dimension_mm_{wMm, hMm, dMm} {
    manufacture_count_++;
  }

  string to_string() const;
  double get_power_capacity() const { return VOLTAGE_ * amp_hour_; }
  double get_volume() const {
    return dimension_mm_[0] * dimension_mm_[1] * dimension_mm_[2];
  }

  static int get_manufacture_count() { return manufacture_count_; }

 private:
  const static double VOLTAGE_;
  const static string TYPE_;
  static int manufacture_count_;

  string manufacturer_;
  string model_;
  double amp_hour_;
  double weight_kg_;
  array<double, 3> dimension_mm_;
};

const double Battery7v::VOLTAGE_ = 7.2;
const string Battery7v::TYPE_ = "Lithium-Ion";
int Battery7v::manufacture_count_ = 0;

string Battery7v::to_string() const {
  ostringstream oss;
  oss << fixed << setprecision(2);

  oss << manufacturer_ << " ";
  oss << model_ << ": ";
  oss << get_power_capacity() << "Wh (";
  oss << VOLTAGE_ << "V/";
  oss << amp_hour_ << "Ah) - ";
  oss << dimension_mm_[0] << "(W)x";
  oss << dimension_mm_[1] << "(H)x";
  oss << dimension_mm_[2] << "(D) ";
  oss << get_volume() << " volume ";
  oss << weight_kg_ << "kg";

  return oss.str();
}

int main() {
  Battery7v zlD72("MT-Dell Tech", "ZL-D72", 9.9, 1.18, 38, 80, 70);
  Battery7v zlD50("MT-Dell Tech", "ZL-D50", 6.6, 0.9, 28, 50, 65);
  Battery7v zlD40("MT-Dell Tech", "ZL-D40", 5.3, 1.18, 38, 80, 70);

  cout << zlD72.to_string() << endl;
  cout << zlD50.to_string() << endl;
  cout << zlD40.to_string() << endl;

  cout << endl;
  cout << "Accessing class member variables..." << endl;
  cout << Battery7v::get_manufacture_count() << endl;
  cout << zlD40.get_manufacture_count() << endl;
  cout << endl;

  cout << "Changing the internal structure of Battery7v!" << endl;

  Battery7v mdPL140("BowserPower", "MD-PL140", 9.9, 1.18, 89, 119, 85);

  cout << mdPL140.to_string() << endl;
  cout << zlD72.to_string() << endl;
  cout << zlD50.to_string() << endl;
  cout << zlD40.to_string() << endl;
  cout << endl;
  cout << "Total batteries manufactured: " << Battery7v::get_manufacture_count()
       << endl;

  return 0;
}
