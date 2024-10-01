#include "bmi.hpp"

#include <sstream>

using std::ostringstream;

BMI::BMI(double height_m, double weight_kg)
    : height_m_(height_m), weight_kg_(weight_kg) {}

double BMI::get_weight_kg() const { return weight_kg_; }

double BMI::get_value() const {
  if (cached_bmi_ < 0) {
    cached_bmi_ = weight_kg_ / (height_m_ * height_m_);
  }
  return cached_bmi_;
}

string BMI::to_string() const {
  ostringstream oss;
  oss << height_m_ << " meters, " << weight_kg_ << " kg, BMI: " << get_value();
  return oss.str();
}
