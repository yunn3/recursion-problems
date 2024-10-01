#ifndef FARM_SIMULATION_BMI_H_
#define FARM_SIMULATION_BMI_H_
#include <string>

using std::string;

class BMI {
 public:
  BMI(double height_m, double weight_kg);
  double get_weight_kg() const;
  double get_value() const;
  string to_string() const;

 protected:
  double height_m_;
  double weight_kg_;
  mutable double cached_bmi_ = -1;
};

#endif
