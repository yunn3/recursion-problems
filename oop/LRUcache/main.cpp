#include <iostream>

#include "LRUCache.hpp"

void test_get(LRUCache& cache, int key, const std::string& expected_value) {
  std::string value = cache.get(key);
  if (value.empty()) {
    std::cout << "get(" << key << "): キー" << key
              << "はキャッシュから削除されています (期待値: "
              << (expected_value.empty() ? "削除済み" : expected_value) << ")"
              << std::endl;
  } else {
    std::cout << "get(" << key << "): " << value << " (期待値: "
              << (expected_value.empty() ? "削除済み" : expected_value) << ")"
              << std::endl;
  }
}

void test_put(LRUCache& cache, int key, const std::string& value) {
  cache.put(key, value);
  std::cout << "put(" << key << ", \"" << value << "\") を実行しました。"
            << std::endl;
}

int main() {
  LRUCache cache(3);
  std::cout << "=== キャッシュにデータを追加 ===" << std::endl;
  test_put(cache, 1, "One");
  test_put(cache, 2, "Two");
  test_put(cache, 3, "Three");
  test_get(cache, 2, "Two");
  std::cout << "\n=== キー4を追加し、キャッシュ容量を超過 ===" << std::endl;
  test_put(cache, 4, "Four");
  test_get(cache, 1, "");
  test_get(cache, 2, "Two");
  test_get(cache, 3, "Three");
  std::cout << "\n=== キー5を追加し、キャッシュ容量を超過 ===" << std::endl;
  test_put(cache, 5, "Five");
  test_get(cache, 4, "");
  std::cout << "\n=== 現在のキャッシュの内容を確認 ===" << std::endl;
  test_get(cache, 3, "Three");
  test_get(cache, 4, "");
  test_get(cache, 5, "Five");
  std::cout << "\n=== キー3の値を更新 ===" << std::endl;
  test_put(cache, 3, "Three Updated");
  test_get(cache, 3, "Three Updated");
  std::cout << "\n=== 新しいキーを追加し、キャッシュ容量を超過 ==="
            << std::endl;
  test_put(cache, 6, "Six");
  test_put(cache, 7, "Seven");
  test_get(cache, 4, "");
  test_get(cache, 5, "");
  test_get(cache, 3, "Three Updated");
  test_get(cache, 6, "Six");
  test_get(cache, 7, "Seven");
  return 0;
}
