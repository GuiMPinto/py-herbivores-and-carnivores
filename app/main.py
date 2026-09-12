class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"
    
class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
        # print(f"{self.name} is hiding.")   

class Carnivore(Animal):
    def bite(self, animal):
        if isinstance(animal, Carnivore):
            return
        elif isinstance(animal, Herbivore):
            if animal.hidden:
                return
            else:
                animal.health -= 50
                if animal.health <= 0:
                    Animal.alive.remove(animal)
                    return
