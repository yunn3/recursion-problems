#include <iostream>
using namespace std;

// 財布を表現するクラス
class Wallet {
 public:
  int bill1 = 1;    // 1ドル札
  int bill5 = 3;    // 5ドル札
  int bill10 = 5;   // 10ドル札
  int bill20 = 7;   // 20ドル札
  int bill50 = 9;   // 50ドル札
  int bill100 = 0;  // 100ドル札

  // コンストラクタ（新たにWalletオブジェクトを生成する際に呼び出されるメソッド）
  Wallet() {
    cout << "this function is automatically ran!!" << endl;  // メッセージ表示
  }

  // 財布内の全額を計算するメソッド
  int getTotalMoney() {
    // 各紙幣の価値と枚数を掛け合わせて合計します。
    return (1 * this->bill1) + (5 * this->bill5) + (10 * this->bill10) +
           (20 * this->bill20) + (50 * this->bill50) + (100 * this->bill100);
  }
};

// 人を表現するクラス
class Person {
 public:
  string firstName;  // 名前
  string lastName;   // 姓
  int age;           // 年齢
  double heightM;    // 身長（メートル）
  double weightKg;   // 体重（キログラム）
  Wallet wallet;     // 財布（Walletオブジェクト）

  // コンストラクタ（新たにPersonオブジェクトを生成する際に呼び出されるメソッド）
  // 引数には名前が入ります。
  Person(string firstName) { this->firstName = firstName; }

  // 所持金を取得するメソッド
  int getCash() { return this->wallet.getTotalMoney(); }
};

int main() {
  // Personオブジェクトを新しく作成し、名前を"Ryu"とします。
  Person p = Person("Ryu");
  // Ryuの情報を出力
  cout << "firstname - " << p.firstName << endl;
  cout << "lastname - " << p.lastName
       << endl;  // lastNameは初期値が空文字（未設定）
  cout << "age - " << p.age << endl;  // ageは初期化されていないため、値は不定
  cout << "height - " << p.heightM
       << endl;  // heightMも初期化されていないため、値は不定
  cout << "weight - " << p.weightKg
       << endl;  // weightKgも初期化されていないため、値は不定
  cout << "current money - " << p.getCash() << endl
       << endl;  // 所持金を表示（財布が空の場合は0）

  // Ryuの情報を更新
  p.lastName = "Poolhopper";  // 姓を"Poolhopper"に設定
  p.age = 40;                 // 年齢を40に設定
  p.heightM = 180;            // 身長を180メートルに設定
  p.weightKg = 140;           // 体重を140キログラムに設定

  // 更新後のRyuの情報を出力
  cout << "firstname - " << p.firstName << endl;
  cout << "lastname - " << p.lastName << endl;
  cout << "age - " << p.age << endl;
  cout << "height - " << p.heightM << endl;
  cout << "weight - " << p.weightKg << endl;
}
