#include <ctime>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

using namespace std;

class Wallet {
 public:
  int bill1;
  int bill5;
  int bill10;
  int bill20;
  int bill50;
  int bill100;

  Wallet() : bill1(0), bill5(0), bill10(0), bill20(0), bill50(0), bill100(0) {}

  int get_total_money() const {
    return (1 * bill1) + (5 * bill5) + (10 * bill10) + (20 * bill20) +
           (50 * bill50) + (100 * bill100);
  }

  int insert_bill(int bill, int amount) {
    switch (bill) {
      case 1:
        bill1 += amount;
        break;
      case 5:
        bill5 += amount;
        break;
      case 10:
        bill10 += amount;
        break;
      case 20:
        bill20 += amount;
        break;
      case 50:
        bill50 += amount;
        break;
      case 100:
        bill100 += amount;
        break;
      default:
        return 0;
    }
    return bill * amount;
  }

  int remove_bill(int bill, int amount) {
    switch (bill) {
      case 1:
        if (bill1 >= amount) {
          bill1 -= amount;
          return bill * amount;
        }
        break;
      case 5:
        if (bill5 >= amount) {
          bill5 -= amount;
          return bill * amount;
        }
        break;
      case 10:
        if (bill10 >= amount) {
          bill10 -= amount;
          return bill * amount;
        }
        break;
      case 20:
        if (bill20 >= amount) {
          bill20 -= amount;
          return bill * amount;
        }
        break;
      case 50:
        if (bill50 >= amount) {
          bill50 -= amount;
          return bill * amount;
        }
        break;
      case 100:
        if (bill100 >= amount) {
          bill100 -= amount;
          return bill * amount;
        }
        break;
      default:
        return 0;
    }
    return 0;
  }

  int get_bill1() const { return bill1; }
  int get_bill5() const { return bill5; }
  int get_bill10() const { return bill10; }
  int get_bill20() const { return bill20; }
  int get_bill50() const { return bill50; }
  int get_bill100() const { return bill100; }
};

class Person {
 public:
  enum DenominationPreference { highest_first, dollars, twenties };

  Person(string first_name, string last_name, double height_m, double weight_kg,
         int birth_year, int initial_money = 0)
      : first_name_(first_name),
        last_name_(last_name),
        height_m_(height_m),
        weight_kg_(weight_kg),
        birth_year_(birth_year),
        denom_pref_(highest_first) {
    if (initial_money > 0) {
      wallet_ = make_unique<Wallet>();
      get_paid(initial_money);
    }
  }

  string to_string() const {
    return get_full_name() + ", height_m: " + std::to_string(height_m_) +
           ", weight_kg: " + std::to_string(weight_kg_) +
           ", age: " + std::to_string(get_age());
  }

  void change_name(string first_name, string last_name) {
    first_name_ = first_name;
    last_name_ = last_name;
  }

  const string& get_first_name() const { return first_name_; }
  const string& get_last_name() const { return last_name_; }
  double get_height_m() const { return height_m_; }
  double get_weight_kg() const { return weight_kg_; }
  int get_birth_year() const { return birth_year_; }

  void set_first_name(const string& first_name) { first_name_ = first_name; }
  void set_last_name(const string& last_name) { last_name_ = last_name; }
  void set_height_m(const double height_m) { height_m_ = height_m; }
  void set_weight_kg(const double weight_kg) { weight_kg_ = weight_kg; }

  int get_age() const {
    time_t current_time = time(0);
    tm* now = localtime(&current_time);
    int current_year = now->tm_year + 1900;
    return current_year - birth_year_;
  }

  int get_cash() const {
    if (!wallet_) return 0;
    return wallet_->get_total_money();
  }

  void add_wallet(unique_ptr<Wallet> new_wallet) {
    wallet_ = std::move(new_wallet);
  }

  unique_ptr<Wallet> drop_wallet() { return std::move(wallet_); }

  void set_denomination_preference(DenominationPreference pref) {
    denom_pref_ = pref;
  }

  vector<int> get_paid(int amount) {
    vector<int> bills(6, 0);

    if (!wallet_) {
      return bills;
    }

    distribute_money(amount, bills);

    int denominations[6] = {1, 5, 10, 20, 50, 100};
    for (int i = 0; i < 6; ++i) {
      if (bills[i] > 0) {
        wallet_->insert_bill(denominations[i], bills[i]);
      }
    }
    return bills;
  }

  vector<int> spend_money(int amount) {
    vector<int> bills(6, 0);

    if (!wallet_) {
      return bills;
    }

    distribute_money(amount, bills);

    int denominations[6] = {1, 5, 10, 20, 50, 100};
    bool can_spend = true;
    for (int i = 0; i < 6; ++i) {
      int wallet_bill_count = get_wallet_bill_count(denominations[i]);
      if (bills[i] > wallet_bill_count) {
        can_spend = false;
        break;
      }
    }

    if (!can_spend) {
      bills.assign(6, 0);
      return bills;
    }

    for (int i = 0; i < 6; ++i) {
      if (bills[i] > 0) {
        wallet_->remove_bill(denominations[i], bills[i]);
      }
    }
    return bills;
  }

 private:
  string first_name_;
  string last_name_;
  double height_m_;
  double weight_kg_;
  int birth_year_;
  unique_ptr<Wallet> wallet_;
  DenominationPreference denom_pref_;

  string get_full_name() const { return first_name_ + " " + last_name_; }

  void distribute_money(int amount, vector<int>& bills) const {
    int remaining = amount;

    if (denom_pref_ == highest_first) {
      int denominations[6] = {100, 50, 20, 10, 5, 1};
      for (int i = 0; i < 6; ++i) {
        int denom = denominations[i];
        int count = remaining / denom;
        bills[get_denomination_index(denom)] = count;
        remaining %= denom;
      }
    } else if (denom_pref_ == dollars) {
      bills[0] = remaining;
    } else if (denom_pref_ == twenties) {
      bills[3] = remaining / 20;
      remaining %= 20;
      int denominations[5] = {100, 50, 10, 5, 1};
      for (int i = 0; i < 5; ++i) {
        int denom = denominations[i];
        int count = remaining / denom;
        bills[get_denomination_index(denom)] = count;
        remaining %= denom;
      }
    }
  }

  int get_denomination_index(int denom) const {
    switch (denom) {
      case 1:
        return 0;
      case 5:
        return 1;
      case 10:
        return 2;
      case 20:
        return 3;
      case 50:
        return 4;
      case 100:
        return 5;
      default:
        return -1;
    }
  }

  int get_wallet_bill_count(int denom) const {
    switch (denom) {
      case 1:
        return wallet_->get_bill1();
      case 5:
        return wallet_->get_bill5();
      case 10:
        return wallet_->get_bill10();
      case 20:
        return wallet_->get_bill20();
      case 50:
        return wallet_->get_bill50();
      case 100:
        return wallet_->get_bill100();
      default:
        return 0;
    }
  }
};

int main() {
  Person carly("Carly", "Angelo", 1.72, 85.5, 1996, 500);

  cout << carly.to_string() << endl;
  cout << "Age: " << carly.get_age() << endl;
  cout << "Current Money: $" << carly.get_cash() << endl;

  carly.change_name("Carly", "Barderson");
  cout << carly.to_string() << endl;

  carly.set_first_name("New");
  carly.set_last_name("Name");
  carly.set_height_m(1.75);
  carly.set_weight_kg(80.0);

  cout << "Updated:" << endl;
  cout << "First Name: " << carly.get_first_name() << endl;
  cout << "Last Name: " << carly.get_last_name() << endl;
  cout << "Height: " << carly.get_height_m() << endl;
  cout << "Weight: " << carly.get_weight_kg() << endl;

  carly.set_denomination_preference(Person::highest_first);

  vector<int> received_bills = carly.get_paid(389);
  cout << "Received $389 with highest_first preference:" << endl;
  cout << "$1 bills: " << received_bills[0] << endl;
  cout << "$5 bills: " << received_bills[1] << endl;
  cout << "$10 bills: " << received_bills[2] << endl;
  cout << "$20 bills: " << received_bills[3] << endl;
  cout << "$50 bills: " << received_bills[4] << endl;
  cout << "$100 bills: " << received_bills[5] << endl;
  cout << "Current Money: $" << carly.get_cash() << endl;

  vector<int> spent_bills = carly.spend_money(150);
  cout << "Spent $150 with highest_first preference:" << endl;
  cout << "$1 bills: " << spent_bills[0] << endl;
  cout << "$5 bills: " << spent_bills[1] << endl;
  cout << "$10 bills: " << spent_bills[2] << endl;
  cout << "$20 bills: " << spent_bills[3] << endl;
  cout << "$50 bills: " << spent_bills[4] << endl;
  cout << "$100 bills: " << spent_bills[5] << endl;
  cout << "Current Money: $" << carly.get_cash() << endl;

  auto new_wallet = make_unique<Wallet>();
  new_wallet->insert_bill(10, 5);
  carly.add_wallet(std::move(new_wallet));
  cout << "Added new wallet with $50." << endl;
  cout << "Current Money: $" << carly.get_cash() << endl;

  auto old_wallet = carly.drop_wallet();
  cout << "Dropped wallet." << endl;
  cout << "Current Money: $" << carly.get_cash() << endl;

  return 0;
}
