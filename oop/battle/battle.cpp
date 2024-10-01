#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class Monster {
 public:
  Monster(const string& name, int health, int attack, int defense);

  string to_string() const;
  string get_name() const;
  double get_height_in_meters() const;
  int get_attack() const;
  int get_defense() const;
  void attacked(int damage);

 private:
  string name_;
  int health_;
  int attack_;
  int defense_;
  int gold_;
  double height_cm_ = 300.0;
};

class Player {
 public:
  Player(const string& username, int health, int attack, int defense, int gold);

  string to_string() const;
  double get_height_in_meters() const;
  void attack_monster(Monster& monster);

 private:
  string username_;
  int health_;
  int attack_;
  int defense_;
  int gold_;
  double height_m_ = 1.8;
};
Monster::Monster(const string& name, int health, int attack, int defense)
    : name_(name), health_(health), attack_(attack), defense_(defense) {}

string Monster::get_name() const { return name_; }

string Monster::to_string() const {
  ostringstream oss;
  oss << name_ << " - HP:" << health_ << "/Atk:" << attack_
      << "/Def:" << defense_ << "/height:" << height_cm_ << "centimeters";
  return oss.str();
}
int Monster::get_attack() const { return attack_; }
int Monster::get_defense() const { return defense_; }

double Monster::get_height_in_meters() const { return height_cm_ / 100.0; }

void Monster::attacked(int damage) {
  health_ -= damage;
  if (health_ < 0) health_ = 0;
}

Player::Player(const string& usernamem, int health, int attack, int defense,
               int gold)
    : username_(usernamem),
      health_(health),
      attack_(attack),
      defense_(defense),
      gold_(gold) {}

double Player::get_height_in_meters() const { return height_m_; }

void Player::attack_monster(Monster& monster) {
  cout << username_ << " ATTACKS " << monster.get_name() << endl;

  if (monster.get_height_in_meters() >= height_m_ * 3 ||
      attack_ <= monster.get_defense())
    return;

  monster.attacked(attack_ - monster.get_defense());
}

string Player::to_string() const {
  ostringstream oss;
  oss << "Player " << username_ << " - HP:" << health_ << "/Atk:" << attack_
      << "/Def:" << defense_ << "/Gold:" << gold_ << "/height:" << height_m_
      << "meters";
  return oss.str();
}

int main() {
  Player p1("Batrunner", 2000, 200, 60, 1000);
  Monster gorilla("Gorilla", 4000, 40, 100);
  Monster vampier("Vampier", 6000, 160, 20);

  cout << p1.to_string() << endl;
  cout << gorilla.to_string() << endl;
  cout << vampier.to_string() << endl;

  p1.attack_monster(gorilla);

  cout << gorilla.to_string() << endl;

  return 0;
}
