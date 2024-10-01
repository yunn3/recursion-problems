#include <iostream>
#include <string>
#include <vector>

using namespace std;

void print_chars(const vector<char>& char_arr) {
  cout << "Printing character array: ";
  for (char character : char_arr) {
    cout << character;
  }
  cout << endl;
}

int main() {
  vector<char> str1Chars = {'h', 'e', 'l', 'l', 'o', ' ',
                            'w', 'o', 'r', 'l', 'd', '!'};
  print_chars(str1Chars);

  str1Chars[6] = 'E';
  str1Chars[7] = 'a';
  str1Chars[8] = 'r';
  str1Chars[9] = 't';
  str1Chars[10] = 'h';

  print_chars(str1Chars);

  string s1(str1Chars.begin(), str1Chars.end());

  cout << endl;
  cout << "Comparing strings...." << endl;
  string s2(str1Chars.begin(), str1Chars.end());
  string s3 = "Hello World!";
  string s4 = "Hello World!";
  string s5 = "Hello World!";

  cout << &s1 << endl;
  cout << &s2 << endl;
  cout << &s3 << endl;

  cout << (s1 == s2) << endl;
  cout << (s3 == s4) << endl;
  cout << (s4 == s5) << endl;

  cout << endl;
  cout << "Doing operations...." << endl;

  string reverseS = "";
  for (int i = s5.length() - 1; i >= 0; i--) {
    reverseS += s5[i];
  }
  cout << s5 << endl;
  cout << reverseS << endl;

  vector<char> reverse_char(s5.length());
  int length = s5.length() - 1;
  for (int i = length; i >= 0; i--) {
    reverse_char[length - i] = s5[i];
  }
  string reverseS2(reverse_char.begin(), reverse_char.end());
  cout << reverseS2 << endl;
  cout << (reverseS2 == reverseS) << endl;
  return 0;
}
