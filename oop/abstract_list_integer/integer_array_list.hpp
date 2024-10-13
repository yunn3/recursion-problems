#ifndef INTEGER_ARRAY_LIST_HPP
#define INTEGER_ARRAY_LIST_HPP

#include "abstract_list_integer.hpp"

class IntegerArrayList : public AbstractListInteger {
 public:
  IntegerArrayList();
  IntegerArrayList(const std::vector<int>& arr);

  int get(int position) const override;
  void add(int element) override;
  void add(const std::vector<int>& elements) override;
  int pop() override;
  void add_at(int position, int element) override;
  void add_at(int position, const std::vector<int>& elements) override;
  int remove_at(int position) override;
  void remove_all_at(int start) override;
  void remove_all_at(int start, int end) override;
  std::unique_ptr<AbstractListInteger> sub_list(int start) const override;
  std::unique_ptr<AbstractListInteger> sub_list(int start,
                                                int end) const override;
  std::vector<int> to_vector() const override;
  int size() const override;

  void add_at(int index, const AbstractListInteger& elements);

 private:
  std::vector<int> data;
};

#endif
