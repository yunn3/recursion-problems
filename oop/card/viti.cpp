#include <algorithm>
#include <array>
#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <memory>
#include <random>
#include <sstream>

using namespace std;

class Card {
 public:
  Card(string rank, string suit);
  const string to_string() const;

 private:
  string rank_;
  string suit_;
};

Card::Card(string rank, string suit) : rank_(rank), suit_(suit){};

const string Card::to_string() const {
  ostringstream oss;
  oss << "[" << suit_ << rank_ << "]";
  return oss.str();
}

class Deck {
 public:
  static const array<const string, 4> SUITS;
  static const array<const string, 13> RANKS;
  static constexpr size_t SIZE = SUITS.size() * RANKS.size();
  static array<unique_ptr<Card>, SIZE> create_deck();
  static const string cards_to_string(
      const array<unique_ptr<Card>, SIZE>& cards);

  Deck();
  void shuffle_deck();
  const string to_string() const;

 private:
  array<unique_ptr<Card>, SIZE> cards_;
};

const array<const string, 4> Deck::SUITS = {"♠", "♡", "♢", "♣"};
const array<const string, 13> Deck::RANKS = {
    "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
};

array<unique_ptr<Card>, Deck::SUITS.size() * Deck::RANKS.size()>
Deck::create_deck() {
  const int suits_size = SUITS.size();
  const int ranks_size = RANKS.size();
  array<unique_ptr<Card>, SIZE> cards;

  for (int suit_idx = 0; suit_idx < suits_size; suit_idx++) {
    for (int rank_idx = 0; rank_idx < ranks_size; rank_idx++) {
      cards[suit_idx * ranks_size + rank_idx] =
          make_unique<Card>(RANKS[rank_idx], SUITS[suit_idx]);
    }
  }

  return cards;
}

const string Deck::cards_to_string(const array<unique_ptr<Card>, SIZE>& cards) {
  ostringstream oss;
  for (int i = 0; i < cards.size(); i++) {
    oss << cards[i]->to_string();
    if ((i % 5) == 4) {
      oss << " ";
    }
  }
  return oss.str();
}

Deck::Deck() : cards_(create_deck()) {}

void Deck::shuffle_deck() {
  random_device seed_gen;
  mt19937 engine(seed_gen());
  shuffle(cards_.begin(), cards_.end(), engine);
}
const string Deck::to_string() const { return cards_to_string(cards_); }

int main() {
  Deck deck;
  cout << deck.to_string() << endl;
  deck.shuffle_deck();
  cout << deck.to_string() << endl;
  return 0;
}
