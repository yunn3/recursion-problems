#ifndef FARM_SIMULATION_PARROT_H_
#define FARM_SIMULATION_PARROT_H_

#include "bird.hpp"

class Parrot : public Bird {
 public:
  Parrot(double height_m, double weight_kg, double life_span_days,
         const string& sex);
  void talk();
};

#endif
