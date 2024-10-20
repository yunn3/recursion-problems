#include "rocket.hpp"

#include <iostream>

Rocket::Rocket() {}
Rocket::~Rocket() {}

void Rocket::fly() { std::cout << "ロケットが飛んでます。" << std::endl; }

double Rocket::flight_height() const { return 225000000000.0; }

double Rocket::fly_speed() const { return 7222.0; }

std::string Rocket::name() const { return "ロケット"; }
