#include "LRUCache.hpp"

LRUCache::LRUCache(int capacity) : capacity_(capacity) {}

LRUCache::~LRUCache() {}

std::string LRUCache::get(int key) {
  auto iterator = cache_.find(key);
  if (iterator == cache_.end()) {
    return "";
  } else {
    keys_.splice(keys_.begin(), keys_, iterator->second.second);
    return iterator->second.first;
  }
}

void LRUCache::put(int key, const std::string& value) {
  auto iterator = cache_.find(key);
  if (iterator != cache_.end()) {
    iterator->second.first = value;
    keys_.splice(keys_.begin(), keys_, iterator->second.second);
    return;
  }
  if (cache_.size() >= capacity_) {
    int old_key = keys_.back();
    keys_.pop_back();
    cache_.erase(old_key);
  }

  keys_.push_front(key);
  cache_[key] = {value, keys_.begin()};
}
