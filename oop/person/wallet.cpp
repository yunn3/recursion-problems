#include <iostream>
using namespace std;

class Wallet {
 public:
  int bill1 = 0;
  int bill5 = 0;
  int bill10 = 0;
  int bill20 = 0;
  int bill50 = 0;
  int bill100 = 0;

  Wallet() {}

  int getTotalMoney() {
    return (1 * bill1) + (5 * bill5) + (10 * bill10) + (20 * bill20) +
           (50 * bill50) + (100 * bill100);
  }

  int insertBill(int bill, int amount) {
    switch (bill) {
      case (1):
        bill1 += amount;
        break;
      case (5):
        bill5 += amount;
        break;
      case (10):
        bill10 += amount;
        break;
      case (20):
        bill20 += amount;
        break;
      case (50):
        bill50 += amount;
        break;
      case (100):
        bill100 += amount;
        break;
      default:
        return 0;
    }

    return bill * amount;
  }
};

class Person {
 public:
  string firstName;
  string lastName;
  int age;
  double heightM;
  double weightKg;
  Wallet wallet;

  Person(string firstName, string lastName, int x, double y, double z) {
    this->firstName = firstName;
    this->lastName = lastName;
    age = x;  // age's state is updated to x.
    heightM = y;
    weightKg = z;
  }

  int getCash() { return wallet.getTotalMoney(); }

  void printState() {
    cout << "firstname - " << firstName << endl;
    cout << "lastname - " << lastName << endl;
    cout << "age - " << age << endl;
    cout << "height - " << heightM << endl;
    double weightKg = 495;
    cout << "weight - " << weightKg << ", joking it is:" << this->weightKg
         << endl;
    cout << "current money - " << getCash() << endl << endl;
  }
};

int main() {
  Person p = Person("Ryu", "Poolhopper", 40, 180, 140);
  p.printState();

  p.wallet.insertBill(5, 3);
  p.wallet.insertBill(100, 2);

  p.printState();
}
