#ifndef ROCKET_HPP
#define ROCKET_HPP

#include "fly.hpp"
#include "named.hpp"

class Rocket : public Fly, public Named {
 public:
  Rocket();
  virtual ~Rocket();
  void fly() override;
  double flight_height() const override;
  double fly_speed() const override;
  std::string name() const override;
};

#endif
