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

 protected:
  double height_m_;
  double weight_kg_;
  mutable double cached_bmi_ = -1;
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
  virtual void move();
  virtual string to_string() const;

  string status() const;
  string get_birth_date() const;

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
  return Animal::to_string() +
         " Fur length: " + std::to_string(fur_length_cm_) +
         " cm, Fur type: " + fur_type_ +
         ", Body temperature: " + std::to_string(body_temperature_c_) + "C";
}

int main() {
  Mammal cow("Cattle", 1.8, 454.5, 730, "female", 1.4, "Cowhide", 32.4);
  cout << cow.to_string() << endl;

  Mammal bull("Cattle", 1.8, 454.5, 730, "male", 1.1, "Cowhide", 30.8);
  cout << bull.to_string() << endl;

  bull.move();
  cow.move();

  cow.eat();
  bull.eat();

  return 0;
}
