class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
    def eat(self, food: str) -> None:
        print(self.name, "is eating", food)
class Bird(Animal):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name=name)
        self.color = color
    def fly(self) -> None:
        print(self.color, self.name, "is flying")