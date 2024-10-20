#include <iostream>
#include <memory>
#include <vector>

#include "named.hpp"
#include "paper_airplane.hpp"
#include "rocket.hpp"

int main() {
  std::vector<std::unique_ptr<Fly>> flying_objects;

  auto paper_airplan = std::make_unique<PaperAirplane>();
  auto rocket = std::make_unique<Rocket>();

  flying_objects.push_back(std::move(paper_airplan));
  flying_objects.push_back(std::move(rocket));

  for (size_t i = 0; i < flying_objects.size(); i++) {
    if (auto named = dynamic_cast<Named*>(flying_objects[i].get())) {
      std::cout << named->name() << "の情報:" << std::endl;
    }
    flying_objects[i]->fly();
    std::cout << "最大飛行速度: " << flying_objects[i]->flight_height()
              << "メートル" << std::endl;
    std::cout << "飛行速度: " << flying_objects[i]->fly_speed()
              << "メートル毎秒" << std::endl;
    std::cout << std::endl;
  }
  return 0;
}
