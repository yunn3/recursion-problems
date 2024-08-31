#include <array>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class Battery {
 public:
  Battery(string manufacturer, string model, double voltage, double amp_hour,
          double weight_kg, double wMm, double hMm, double dMm)
      : manufacturer_(manufacturer),
        model_(model),
        voltage_(voltage),
        amp_hour_(amp_hour),
        weight_kg_(weight_kg),
        dimension_mm_{wMm, hMm, dMm} {}

  string to_string() const;

  double get_power_capacity() const { return voltage_ * amp_hour_; }
  friend bool operator==(const Battery& obj, const Battery& other);
  friend bool operator!=(const Battery& obj, const Battery& other);

 private:
  string manufacturer_;
  string model_;
  double voltage_;
  double amp_hour_;
  double weight_kg_;
  array<double, 3> dimension_mm_;
};

string Battery::to_string() const {
  ostringstream oss;
  oss << fixed << setprecision(2);

  oss << manufacturer_ << " ";
  oss << model_ << ": ";
  oss << get_power_capacity() << "Wh (";
  oss << voltage_ << "V/";
  oss << amp_hour_ << "Ah) - ";
  oss << dimension_mm_[0] << "(W)x";
  oss << dimension_mm_[1] << "(H)x";
  oss << dimension_mm_[2] << "(D) ";
  oss << weight_kg_ << "kg";

  return oss.str();
}

bool operator==(const Battery& obj, const Battery& other) {
  for (int i = 0; i < obj.dimension_mm_.size(); i++) {
    if (obj.dimension_mm_[i] != other.dimension_mm_[i]) {
      return false;
    }
  }
  return true;
}

bool operator!=(const Battery& obj, const Battery& other) {
  for (int i = 0; i < obj.dimension_mm_.size(); i++) {
    if (obj.dimension_mm_[i] != other.dimension_mm_[i]) {
      return true;
    }
  }
  return false;
}

int main() {
  Battery mc96("VTec", "MC96", 14.4, 6.6, 0.55, 72, 97, 51.5);
  Battery mc60("VTec", "MC60", 14.4, 4.2, 0.35, 52, 77, 40.5);
  Battery md_pl140("BowserPower", "MD-PL140", 14.4, 9.9, 1.18, 89, 119, 85);
  Battery zl_d72("MT-Dell Tech", "ZL-D72", 7.2, 9.9, 1.18, 38, 80, 70);
  Battery original("VTec", "MC96", 14.4, 6.6, 0.55, 72, 97, 51.5);
  cout << mc96.to_string() << endl;
  cout << mc60.to_string() << endl;
  cout << md_pl140.to_string() << endl;
  cout << zl_d72.to_string() << endl;

  if (mc96 == original) {
    cout << "same size battery" << endl;
  }

  if (mc60 != original) {
    cout << "differnt size battery" << endl;
  }
  return 0;
}