#include "mammal.hpp"

#include <iostream>

using std::cout, std::endl;

Mammal::Mammal(const string& species, double height_m, double weight_kg,
               double life_span_days, const string& biological_sex,
               double fur_length_cm, const string& fur_type,
               double avg_body_temperature_c)
    : Animal(species, height_m, weight_kg, life_span_days, biological_sex),
      fur_length_cm_(fur_length_cm),
      fur_type_(fur_type),
      avg_body_temperature_c_(avg_body_temperature_c),
      body_temperature_c_(avg_body_temperature_c),
      mammary_gland_(biological_sex == "female") {}

void Mammal::sweat() {
  if (!is_alive()) return;
  cout << "Sweating.... Body temperature is now "
       << (body_temperature_c_ -= 0.3) << "C" << endl;
}

void Mammal::produce_milk() {
  if (!is_alive()) return;
  if (is_pregnant_ && mammary_gland_) {
    cout << "Producing milk..." << endl;
  } else {
    cout << "Cannot produce milk" << endl;
  }
}

void Mammal::mate(Mammal& mammal) {
  if (!is_alive()) return;
  if (species_ != mammal.species_) return;
  if (biological_sex_ == "female" && mammal.biological_sex_ == "male") {
    is_pregnant_ = true;
  } else if (biological_sex_ == "male" && mammal.biological_sex_ == "female") {
    mammal.is_pregnant_ = true;
  }
}

void Mammal::bite() {
  if (!is_alive()) return;
  cout << species_ << " bites with their single lower jaws." << endl;
}

void Mammal::replace_teeth() {
  if (!is_alive()) return;
  if (tooth_counter_ == 0) tooth_counter_++;
}

void Mammal::increase_body_heat(double celcius) {
  body_temperature_c_ += celcius;
}

void Mammal::decrease_body_heat(double celcius) {
  body_temperature_c_ -= celcius;
}

void Mammal::adjust_body_heat() {
  body_temperature_c_ = avg_body_temperature_c_;
}

void Mammal::move() {
  if (!is_alive()) return;
  cout << "This mammal is moving....." << endl;
}

string Mammal::to_string() const {
  return Animal::to_string() + "\n" +
         "Fur length: " + std::to_string(fur_length_cm_) +
         " cm, Fur type: " + fur_type_ +
         ", Body temperature: " + std::to_string(body_temperature_c_) + "C";
}
