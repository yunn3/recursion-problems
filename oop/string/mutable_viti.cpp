#include <cstddef>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

class MutableString {
 public:
  MutableString(vector<char> char_array) : char_array_(char_array) {}
  template <typename Iterator>
  MutableString(Iterator begin, Iterator end) : char_array_(begin, end) {}

  auto begin() const;
  auto end() const;
  void append(char c);
  MutableString substring(uint64_t start) const;
  MutableString substring(uint64_t start_index, uint64_t end_index) const;
  void concat(const vector<char>& c_arr);
  void concat(const string& string_input);
  void concat(const MutableString& other);
  size_t length() const;
  string str() const;

 private:
  vector<char> char_array_;
};

auto MutableString::begin() const { return char_array_.begin(); }
auto MutableString::end() const { return char_array_.end(); }

void MutableString::append(char c) { char_array_.push_back(c); }

MutableString MutableString::substring(uint64_t start) const {
  start %= length();
  return MutableString(char_array_.begin() + start, char_array_.end());
}
MutableString MutableString::substring(uint64_t start_index,
                                       uint64_t end_index) const {
  start_index %= length();
  end_index %= length();

  if (start_index > end_index) {
    swap(start_index, end_index);
  }

  return MutableString(char_array_.begin() + start_index,
                       char_array_.begin() + end_index);
}
void MutableString::concat(const vector<char>& c_arr) {
  for (char c : c_arr) {
    char_array_.push_back(c);
  }
}
void MutableString::concat(const string& string_input) {
  for (char c : string_input) {
    char_array_.push_back(c);
  }
}
void MutableString::concat(const MutableString& other) {
  for (auto it = other.begin(); it != other.end(); it++) {
    char_array_.push_back(*it);
  }
}

size_t MutableString::length() const { return char_array_.size(); }

string MutableString::str() const {
  return string(char_array_.begin(), char_array_.end());
}

int main() {
  vector<char> vec_c = {'a', 'b', 'c', 'd', 'e', 'f'};
  MutableString mut_str(vec_c);

  cout << mut_str.str() << endl;
  cout << mut_str.length() << endl;

  cout << endl;
  cout << "Append:" << endl;
  mut_str.append('@');

  cout << mut_str.str() << endl;
  cout << mut_str.length() << endl;

  cout << endl;
  cout << "Substring:" << endl;
  MutableString sub_str = mut_str.substring(3);

  cout << sub_str.str() << endl;
  cout << sub_str.length() << endl;

  MutableString sub_str2 = mut_str.substring(3, 5);

  cout << sub_str2.str() << endl;
  cout << sub_str2.length() << endl;

  cout << endl;
  cout << "Concat:" << endl;

  mut_str.concat(vector<char>{'G', 'o', 'o', 'g', 'l', 'e'});
  cout << mut_str.str() << endl;

  mut_str.concat("Hello!!!");
  cout << mut_str.str() << endl;

  MutableString mut_str2({'W', 'h', 'a', 't', '\'', 's'});
  mut_str.concat(mut_str2);

  cout << mut_str.str() << endl;
}
