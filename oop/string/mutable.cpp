#include <iostream>
#include <vector>

using namespace std;

class MutableString {
 public:
  MutableString(const char* init_string) {
    while (*init_string != '\0') {
      str_.push_back(*init_string++);
    }
  }
  MutableString() = default;

  void append(char character) { str_.push_back(character); }

  // startインデックスから最後まで
  MutableString substring(int start_index) const {
    if (start_index < 0 || start_index >= str_.size()) {
      return MutableString("");
    }
    MutableString result;
    for (int i = start_index; i < str_.size(); ++i) {
      result.append(str_[i]);
    }
    return result;
  }

  // startインデックスからendインデックスまで
  MutableString substring(int start_index, int end_index) const {
    if (start_index < 0 || start_index >= str_.size()) {
      return MutableString("");
    }
    MutableString result;
    for (int i = start_index; i < end_index; ++i) {
      result.append(str_[i]);
    }
    return result;
  }

  void concat(const char* char_arr) {
    while (*char_arr != '\0') {
      str_.push_back(*char_arr++);
    }
  }

  void concat(const MutableString& other) {
    for (char character : other.str_) {
      str_.push_back(character);
    }
  }

  int length() const { return str_.size(); }

  void print() const {
    for (char character : str_) {
      cout << character;
    }
    cout << endl;
  }

 private:
  vector<char> str_;
};

int main() {
  MutableString s("hello");
  s.append(' ');
  s.append('w');
  s.append('o');
  s.append('r');
  s.append('l');
  s.append('d');
  s.append('!');
  s.print();

  MutableString substring = s.substring(6);
  substring.print();

  MutableString substring2 = s.substring(0, 5);
  substring2.print();

  MutableString hay("How are you?");
  s.concat(hay);
  s.print();

  return 0;
}
