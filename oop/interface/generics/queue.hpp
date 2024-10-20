#ifndef QUEUE_HPP
#define QUEUE_HPP

template <typename T>
class Queue {
 public:
  virtual ~Queue() = default;

  virtual T peek_first() const = 0;
  virtual T poll() = 0;
  virtual void push(T value) = 0;
};

#endif
