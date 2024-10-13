#ifndef ABSTRACT_LIST_INTEGER_HPP
#define ABSTRACT_LIST_INTEGER_HPP

#include <memory>
#include <vector>

class AbstractListInteger {
 public:
  AbstractListInteger();
  AbstractListInteger(const std::vector<int>& arr);
  virtual ~AbstractListInteger() {}

  std::vector<int> get_original_list() const;

  virtual int get(int position) const = 0;
  virtual void add(int element) = 0;
  virtual void add(const std::vector<int>& elements) = 0;
  virtual int pop() = 0;
  virtual void add_at(int position, int elements) = 0;
  virtual void add_at(int position, const std::vector<int>& elements) = 0;
  virtual int remove_at(int position) = 0;
  virtual void remove_all_at(int start) = 0;
  virtual void remove_all_at(int start, int end) = 0;
  virtual std::unique_ptr<AbstractListInteger> sub_list(int start) const = 0;
  virtual std::unique_ptr<AbstractListInteger> sub_list(int start,
                                                        int end) const = 0;
  virtual std::vector<int> to_vector() const = 0;
  virtual int size() const = 0;

 protected:
  const std::vector<int>& get_initial_list() const;

 private:
  std::vector<int> initial_list;
};

#endif
