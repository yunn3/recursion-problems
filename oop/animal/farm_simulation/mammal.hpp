#ifndef FARM_SIMULATION_MAMMAL_H_
#define FARM_SIMULATION_MAMMAL_H_
#include "animal.hpp"
class Mammal : public Animal {
 public:
  Mammal(const string& species, double height_m, double weight_kg,
         double life_span_days, const string& biological_sex,
         double fur_length_cm, const string& fur_type,
         double avg_body_temperature_c);
  void sweat();
  void produce_milk();
  void mate(Mammal& mammal);
  void bite();
  void replace_teeth();
  void increase_body_heat(double celcius);
  void decrease_body_heat(double celcius);
  void adjust_body_heat();
  void move() override;
  string to_string() const override;

 private:
  double fur_length_cm_;
  string fur_type_;
  int tooth_counter_ = 0;
  double body_temperature_c_;
  double avg_body_temperature_c_;
  bool mammary_gland_;
  bool is_pregnant_ = false;
};

#endif
