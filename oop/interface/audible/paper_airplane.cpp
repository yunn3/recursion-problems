#include "paper_airplane.hpp"

#include <iostream>

PaperAirplane::PaperAirplane() {}

PaperAirplane::~PaperAirplane() {}

void PaperAirplane::fly() {
  std::cout << "紙飛行機が飛んでます。" << std::endl;
}

double PaperAirplane::flight_height() const { return 10.0; }

double PaperAirplane::fly_speed() const { return 5.0; }

std::string PaperAirplane::name() const { return "紙飛行機"; }
