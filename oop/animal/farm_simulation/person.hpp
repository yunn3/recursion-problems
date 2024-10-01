#ifndef FARMING_SIMULATION_PERSON_H_
#define FARMING_SIMULATION_PERSON_H_

#include <memory>
#include <vector>

#include "animal.hpp"
using std::unique_ptr;
using std::vector;

class Person {
 public:
  Person(const string& name);
  void buy_animal(unique_ptr<Animal> animal);
  void sell_animal(Animal* animal);
  void collect_farm_production();

  void sell_all_animals();
  double get_money() const;
  const vector<unique_ptr<Animal>>& get_farm() const;

 private:
  void calculate_sale_profit(const Animal* animal);
  string name_;
  double money_;
  vector<unique_ptr<Animal>> farm_;
};

#endif
