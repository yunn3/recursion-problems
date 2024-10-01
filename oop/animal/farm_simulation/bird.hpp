#ifndef FARM_SIMULATION_BIRD_H_
#define FARM_SIMULATION_BIRD_H_

#include "animal.hpp"
class Bird : public Animal {
 public:
  Bird(const string& species, double height_m, double weight_kg,
       double life_span_days, const string& sex)
      : Animal(species, height_m, weight_kg, life_span_days, sex) {}
  virtual ~Bird() {}
  void move() override;
  string to_string() const override;
};

#endif
