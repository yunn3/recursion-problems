#include "parrot.hpp"

#include <iostream>

using std::cout, std::endl;

Parrot::Parrot(double height_m, double weight_kg, double life_span_days,
               const string& sex)
    : Bird("Parrot", height_m, weight_kg, life_span_days, sex) {}
void Parrot::talk() { cout << "Parrot is talking!" << endl; }
