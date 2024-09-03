#include <algorithm>
#include <array>
#include <iostream>
#include <random>
#include <sstream>
#include <vector>

using namespace std;

class Card {
 private:
  string rank;
  string suit;

 public:
  Card(string rank, string suit) : rank(rank), suit(suit) {}

  const string to_string() const { return rank + suit; }
};

class Deck {
 private:
  static const array<const string, 4> SUITS_;
  static const array<const string, 13> RANKS_;
  vector<Card> cards_;

 public:
  Deck() { cards_ = create_deck(); }
  static const string cards_to_string(const vector<Card>& cards) {
    ostringstream oss;
    for (size_t i = 0; i < cards.size(); i++) {
      oss << cards[i].to_string();
      if (i % 13 == 12) oss << " ";
    }
    return oss.str();
  }

  static vector<Card> create_deck() {
    vector<Card> deck;

    for (const string suit : SUITS_) {
      for (const string rank : RANKS_) {
        deck.emplace_back(suit, rank);
      }
    }
    return deck;
  }

  void shuffle_deck() {
    random_device rd;
    default_random_engine random_num_gen(rd());
    shuffle(cards_.begin(), cards_.end(), random_num_gen);
  }

  static void shuffle_deck_in_place(vector<Card>& cards) {
    random_device rd;
    default_random_engine random_num_gen(rd());
    shuffle(cards.begin(), cards.end(), random_num_gen);
  }

  static vector<Card> shuffle_deck_out_of_place(const vector<Card>& cards) {
    vector<Card> shuffled_deck = cards;
    shuffle_deck_in_place(shuffled_deck);
    return shuffled_deck;
  }

  string to_string() const { return cards_to_string(cards_); }
};

const array<const string, 4> Deck::SUITS_ = {"♠", "♡", "♢", "♣"};
const array<const string, 13> Deck::RANKS_ = {
    "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};

int main() {
  Deck deck;

  cout << "Original Deck:" << endl;
  cout << deck.to_string() << endl;
  cout << endl;

  vector<Card> cards = Deck::create_deck();
  Deck::shuffle_deck_in_place(cards);
  cout << "Shuffled Deck (In Place):" << endl;
  cout << Deck::cards_to_string(cards) << endl;
  vector<Card> shuffled_cards = Deck::shuffle_deck_out_of_place(cards);
  cout << endl;

  cout << "Shuffled Deck (Out of Place):" << endl;
  cout << Deck::cards_to_string(cards) << endl;
  cout << Deck::cards_to_string(shuffled_cards) << endl;

  cout << endl;
}
