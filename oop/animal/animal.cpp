#include <ctime>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class BMI {
 public:
  BMI(double height_m, double weight_kg);

  double get_weight_kg() const;
  double get_value() const;
  string to_string() const;

 private:
  double height_m_;
  double weight_kg_;
  mutable double cached_bmi_ = -1;
};

class Animal {
 public:
  Animal(const string& species, double height_m, double weight_kg,
         double life_span_days, const string& biological_sex);

  bool is_hungry() const;
  bool is_sleepy() const;
  bool is_alive() const;
  void set_hungry();
  void set_sleepy();
  void eat();
  void sleep();
  void die();
  void move();

  string status() const;
  string get_birth_date() const;
  string to_string() const;

 private:
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

BMI::BMI(double height_m, double weight_kg)
    : height_m_(height_m), weight_kg_(weight_kg) {}

double BMI::get_weight_kg() const { return weight_kg_; }

double BMI::get_value() const {
  if (cached_bmi_ < 0) {
    cached_bmi_ = weight_kg_ / (height_m_ * height_m_);
  }
  return cached_bmi_;
}

string BMI::to_string() const {
  ostringstream oss;
  oss << height_m_ << " meters, " << weight_kg_ << " kg, BMI: " << get_value();
  return oss.str();
}

Animal::Animal(const string& species, double height_m, double weight_kg,
               double life_span_days, const string& biological_sex)
    : species_(species),
      bmi_(height_m, weight_kg),
      life_span_days_(life_span_days),
      biological_sex_(biological_sex) {
  birth_time_ = time(nullptr);
}

bool Animal::is_hungry() const { return hunger_level_ >= 70; }

bool Animal::is_sleepy() const { return sleepiness_level_ >= 70; }

bool Animal::is_alive() const {
  if (!alive_status_cached_) {
    return death_time_ == 0;
  }
  return alive_status_cached_;
}

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
  alive_status_cached_ = false;
}

void Animal::move() {
  if (!is_alive()) return;
  cout << "This animal just moved..." << endl;
}

string Animal::to_string() const {
  ostringstream oss;
  oss << species_ << ", " << bmi_.to_string() << " lives " << life_span_days_
      << " days, gender: " << biological_sex_ << ". " << status();
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
  struct tm timeinfo;
  localtime_r(&birth_time_, &timeinfo);
  strftime(buffer, sizeof(buffer), "%Y/%m/%d %H:%M:%S", &timeinfo);
  return string(buffer);
}

int main() {
  Animal cow("Cow", 1.8, 454.5, 730, "female");
  cout << cow.to_string() << endl;

  cow.eat();
  cow.sleep();
  cout << cow.status() << endl;

  cow.set_hungry();
  cow.set_sleepy();
  cow.die();
  cout << cow.status() << endl;

  return 0;
}
