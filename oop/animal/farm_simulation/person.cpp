#include "person.hpp"

#include <algorithm>

#include "chicken.hpp"
#include "cow.hpp"
#include "horse.hpp"

Person::Person(const string& name) : name_(name), money_(0) {}
void Person::buy_animal(unique_ptr<Animal> animal) {
  farm_.push_back(move(animal));
}
void Person::sell_animal(Animal* animal) {
  auto it = std::find_if(
      farm_.begin(), farm_.end(),
      [animal](const unique_ptr<Animal>& ptr) { return ptr.get() == animal; });
  if (it != farm_.end()) {
    calculate_sale_profit(animal);
    farm_.erase(it);
  }
}
void Person::collect_farm_production() {
  for (const auto& animal : farm_) {
    if (const Cow* cow = dynamic_cast<const Cow*>(animal.get())) {
      money_ += cow->get_milk_production() * 2;
    } else if (const Chicken* chicken =
                   dynamic_cast<const Chicken*>(animal.get())) {
      money_ += chicken->get_egg_production() * 0.5;
    }
  }
}
void Person::sell_all_animals() {
  for (const auto& animal : farm_) {
    calculate_sale_profit(animal.get());
  }
  farm_.clear();
}
double Person::get_money() const { return money_; }
const vector<unique_ptr<Animal>>& Person::get_farm() const { return farm_; }

void Person::calculate_sale_profit(const Animal* animal) {
  if (const Cow* cow = dynamic_cast<const Cow*>(animal)) {
    money_ += cow->get_weight_kg() * 10;
  } else if (const Horse* horse = dynamic_cast<const Horse*>(animal)) {
    money_ += horse->get_speed() * 50;
  } else if (const Chicken* chicken = dynamic_cast<const Chicken*>(animal)) {
    money_ += chicken->get_weight_kg() * 5;
  }
}
