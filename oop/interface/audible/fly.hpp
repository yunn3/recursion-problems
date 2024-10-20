#ifndef FLY_HPP
#define FLY_HPP

class Fly {
 public:
  virtual ~Fly() = 0;

  virtual void fly() = 0;
  virtual double flight_height() const = 0;
  virtual double fly_speed() const = 0;
};

#endif
