#ifndef LRUCACHE_HPP
#define LRUCACHE_HPP

#include <list>
#include <string>
#include <unordered_map>

class LRUCache {
 public:
  LRUCache(int capacity);
  ~LRUCache();
  std::string get(int key);
  void put(int key, const std::string& value);

 private:
  int capacity_;
  std::list<int> keys_;
  std::unordered_map<int, std::pair<std::string, std::list<int>::iterator>>
      cache_;
};

#endif
