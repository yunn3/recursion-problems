class Animal:
    def __init__(self, species: str, weightKg: float, heightM: float, predator: bool):
        self.species = species
        self.weightKg = weightKg
        self.heightM = heightM
        self.predator = predator

    def domasticate(self) -> None:
        self.predator = False


class Hunter:
    def __init__(
        self,
        name: str,
        weightKg: float,
        heightM: float,
        strength: float,
        cageCubicMeters: float,
    ):
        self.name = name
        self.weightKg = weightKg
        self.heightM = heightM
        self.strength = strength
        self.cageCubicMeters = cageCubicMeters

    def canCaptureAnimal(self, animal: Animal) -> bool:
        return (
            self.strengthKg() >= animal.weightKg
            and self.cageCubicMeters >= animal.heightM
            and not animal.predator
        )

    def attemptToDomesticate(self, animal: Animal) -> bool:
        if self.strengthKg() > animal.weightKg * 2:
            animal.domasticate()
            return True
        return False

    def strengthKg(self) -> float:
        return self.strength * self.weightKg


def capturedAnimals(hunter: Hunter, animals: list) -> list:
    result = []

    for animal in animals:
        if hunter.canCaptureAnimal(animal):
            result.append(animal)
    return result


def displayAnimals(animals: list) -> None:
    for animal in animals:
        print(animal.species)


def domesticateTheAnimals(hunter: Hunter, animals: list) -> None:
    for animal in animals:
        hunter.attemptToDomesticate(animal)


tiger = Animal("Tiger", 290, 2.6, True)
cow = Animal("Cow", 1134, 1.5, False)
snake = Animal("Snake", 100, 1.2, True)
cat = Animal("Cat", 10, 0.5, False)
hunternator = Hunter("Hunternator", 124.73, 1.85, 15, 3)
animals = [tiger, cow, snake, cat]

displayAnimals(capturedAnimals(hunternator, animals))
domesticateTheAnimals(hunternator, animals)
displayAnimals(capturedAnimals(hunternator, animals))
