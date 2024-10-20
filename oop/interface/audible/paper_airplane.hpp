#ifndef PAPER_AIRPLANE_HPP
#define PAPER_AIRPLANE_HPP

#include "fly.hpp"
#include "named.hpp"

class PaperAirplane : public Fly, public Named {
 public:
  PaperAirplane();
  virtual ~PaperAirplane();
  void fly() override;
  double flight_height() const override;
  double fly_speed() const override;
  std::string name() const override;
};

#endif
