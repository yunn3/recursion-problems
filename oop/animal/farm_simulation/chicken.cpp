#include "chicken.hpp"

#include <iostream>

using std::cout, std::endl;
Chicken::Chicken(double height_m, double weight_kg, double life_span_days,
                 const string& sex)
    : Bird("Chicken", height_m, weight_kg, life_span_days, sex) {}

int Chicken::get_egg_production() const { return 5; }

void Chicken::move() {
  if (!is_alive()) return;
  cout << species_ << " is walking." << endl;
}
