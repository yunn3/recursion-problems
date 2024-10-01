#ifndef FARM_SIMULATION_HORSE_H_
#define FARM_SIMULATION_HORSE_H_

#include "mammal.hpp"

class Horse : public Mammal {
 public:
  Horse(double height_m, double weight_kg, double life_span_days,
        const string& biological_sex, double speed)
      : Mammal("Horse", height_m, weight_kg, life_span_days, biological_sex,
               1.5, "Horsehair", 37.5),
        speed_(speed) {}
  double get_speed() const;

 private:
  double speed_;
};

#endif
