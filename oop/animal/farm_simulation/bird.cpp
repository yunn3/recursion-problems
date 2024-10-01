#include "bird.hpp"

#include <iostream>
#include <string>

using std::cout, std::endl;
using std::string;

void Bird::move() {
  if (!is_alive()) return;
  cout << species_ << " is flying." << endl;
}
string Bird::to_string() const { return Animal::to_string() + " (Bird)"; };
