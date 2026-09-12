class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, \
                   Hidden: {self.hidden}}}"
    
class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden
        # print(f"{self.name} is hiding.")   

class Сarnivore(Animal):
    def bite(self, animal):
        if isinstance(animal, Carnivore):
            print("Cannot bite another carnivore!")
            return
        elif isinstance(animal, Herbivore):
            if animal.hidden:
                print(f"{animal.name} is hiding and cannot be bitten.")
            else:
                animal.health -= 50
                print(f"{self.name} bit {animal.name}. {animal.name}'s health is now {animal.health}.")
                if animal.health <= 0:
                    print(f"{animal.name} has died.")
                    Animal.alive.remove(animal)
        
