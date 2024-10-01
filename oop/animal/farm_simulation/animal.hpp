#ifndef FARM_SIMULATION_ANIMAL_H_
#define FARM_SIMULATION_ANIMAL_H_
#include <string>

#include "bmi.hpp"

using std::string;

class Animal {
 public:
  Animal(const string& species, double height_m, double weight_kg,
         double life_span_days, const string& biological_sex);
  virtual ~Animal();
  bool is_hungry() const;
  bool is_sleepy() const;
  bool is_alive() const;
  void set_hungry();
  void set_sleepy();
  void eat();
  void sleep();
  void die();
  virtual void move() = 0;
  virtual string to_string() const;
  string status() const;
  string get_birth_date() const;
  double get_weight_kg() const;
  double get_bmi_value() const;

 protected:
  string species_;
  string biological_sex_;
  int hunger_level_ = 100;
  int sleepiness_level_ = 100;
  double life_span_days_;
  time_t birth_time_;
  time_t death_time_ = 0;
  BMI bmi_;
  mutable bool alive_status_cached_ = true;
};

#endif
