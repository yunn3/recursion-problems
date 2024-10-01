#ifndef FARM_SIMULATION_CHICKEN_H_
#define FARM_SIMULATION_CHICKEN_H_
#include "bird.hpp"

class Chicken : public Bird {
 public:
  Chicken(double height_m, double weight_kg, double life_span_days,
          const string& sex);
  int get_egg_production() const;
  void move() override;
};

#endif
