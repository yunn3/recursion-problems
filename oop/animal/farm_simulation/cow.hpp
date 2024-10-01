#ifndef FARM_SIMULATION_COW_H_
#define FARM_SIMULATION_COW_H_

#include "mammal.hpp"

class Cow : public Mammal {
 public:
  Cow(double height_m, double weight_kg, double life_span_days,
      const string& biological_sex)
      : Mammal("Cow", height_m, weight_kg, life_span_days, biological_sex, 1.0,
               "Cowhide", 38.6) {}
  double get_milk_production() const;
};

#endif
