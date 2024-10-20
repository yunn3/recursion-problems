#ifndef STACK_HPP
#define STACK_HPP

template <typename T>
class Stack {
 public:
  virtual ~Stack() = default;

  virtual T peek_last() const = 0;
  virtual T pop() = 0;
  virtual void push(T value) = 0;
};

#endif
