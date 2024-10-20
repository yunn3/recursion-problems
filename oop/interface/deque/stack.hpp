#ifndef STACK_HPP
#define STACK_HPP

class Stack {
 public:
  virtual ~Stack() = default;

  virtual int peek_last() const = 0;
  virtual int pop() = 0;
  virtual void push(int value) = 0;
};

#endif
