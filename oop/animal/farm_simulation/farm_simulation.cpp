#include <ctime>
#include <iostream>
#include <memory>
#include <utility>

#include "animal.hpp"
#include "chicken.hpp"
#include "cow.hpp"
#include "horse.hpp"
#include "parrot.hpp"
#include "person.hpp"

using namespace std;

int main() {
  Person farmer("Farming_way");

  auto cow = make_unique<Cow>(1.5, 500, 1825, "female");
  auto bull = make_unique<Cow>(1.6, 600, 1825, "male");
  auto horse = make_unique<Horse>(1.8, 600, 1095, "male", 60.0);
  auto chicken = make_unique<Chicken>(0.5, 2.0, 365, "female");
  auto parrot = make_unique<Parrot>(0.4, 1.5, 1460, "male");

  Animal* horse_ptr = horse.get();

  farmer.buy_animal(move(cow));
  farmer.buy_animal(move(bull));
  farmer.buy_animal(move(horse));
  farmer.buy_animal(move(chicken));
  farmer.buy_animal(move(parrot));

  for (const auto& animal : farmer.get_farm()) {
    cout << animal->to_string() << endl;
    animal->move();
  }

  auto cow_ptr = dynamic_cast<Cow*>(farmer.get_farm()[0].get());
  auto bull_ptr = dynamic_cast<Cow*>(farmer.get_farm()[1].get());

  if (cow_ptr && bull_ptr) {
    cow_ptr->mate(*bull_ptr);
    cow_ptr->produce_milk();
  }

  cow_ptr->sweat();

  cow_ptr->increase_body_heat(1.0);
  cout << "After increasing body heat:\n" << cow_ptr->to_string() << endl;
  cow_ptr->adjust_body_heat();
  cout << "After adjusting body heat:\n" << cow_ptr->to_string() << endl;

  cow_ptr->bite();

  cow_ptr->replace_teeth();

  auto parrot_ptr = dynamic_cast<Parrot*>(farmer.get_farm()[4].get());
  if (parrot_ptr) {
    parrot_ptr->talk();
    parrot_ptr->move();
  }

  auto chicken_ptr = dynamic_cast<Chicken*>(farmer.get_farm()[3].get());
  if (chicken_ptr) {
    chicken_ptr->move();
  }

  farmer.collect_farm_production();
  cout << "After collecting produce, farmer has $" << farmer.get_money()
       << endl;

  farmer.sell_animal(horse_ptr);
  cout << "After selling the horse, farmer has $" << farmer.get_money() << endl;

  farmer.sell_all_animals();
  cout << "After selling all animals, farmer has $" << farmer.get_money()
       << endl;

  cow_ptr->die();
  cow_ptr->eat();
  cout << cow_ptr->status() << endl;

  return 0;
}
