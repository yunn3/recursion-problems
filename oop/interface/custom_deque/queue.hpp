#ifndef QUEUE_HPP
#define QUEUE_HPP

class Queue {
 public:
  virtual ~Queue() = default;

  virtual int peek_first() const = 0;
  virtual int poll() = 0;
  virtual void push(int value) = 0;
};

#endif
