#include "animal.hpp"

#include <sstream>
using std::ostringstream;
Animal::Animal(const string& species, double height_m, double weight_kg,
               double life_span_days, const string& biological_sex)
    : species_(species),
      bmi_(height_m, weight_kg),
      life_span_days_(life_span_days),
      biological_sex_(biological_sex) {
  birth_time_ = time(nullptr);
}

Animal::~Animal() {}

bool Animal::is_hungry() const { return hunger_level_ >= 70; }

bool Animal::is_sleepy() const { return sleepiness_level_ >= 70; }

bool Animal::is_alive() const { return death_time_ == 0; }

void Animal::eat() {
  if (!is_alive()) return;
  hunger_level_ = 0;
}

void Animal::set_hungry() {
  if (!is_alive()) return;
  hunger_level_ = 100;
}

void Animal::sleep() {
  if (!is_alive()) return;
  sleepiness_level_ = 0;
}

void Animal::set_sleepy() {
  if (!is_alive()) return;
  sleepiness_level_ = 100;
}

void Animal::die() {
  if (!is_alive()) return;
  hunger_level_ = 0;
  sleepiness_level_ = 0;
  death_time_ = time(nullptr);
}

string Animal::to_string() const {
  ostringstream oss;
  oss << species_ << ", " << bmi_.to_string() << " lives " << life_span_days_
      << " days, gender: " << biological_sex_ << ".\n"
      << status();
  return oss.str();
}

string Animal::status() const {
  ostringstream oss;
  oss << species_ << " status: Hunger - " << hunger_level_
      << "%, sleepiness: " << sleepiness_level_ << "%, Alive - "
      << (is_alive() ? "Yes" : "No") << ", Born in the " << get_birth_date();
  return oss.str();
}

string Animal::get_birth_date() const {
  char buffer[20];
  struct tm* timeinfo;
  timeinfo = localtime(&birth_time_);
  strftime(buffer, sizeof(buffer), "%Y/%m/%d %H:%M:%S", timeinfo);
  return string(buffer);
}

double Animal::get_weight_kg() const { return bmi_.get_weight_kg(); }

double Animal::get_bmi_value() const { return bmi_.get_value(); }
