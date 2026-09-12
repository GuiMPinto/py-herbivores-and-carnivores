class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    @classmethod
    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, \
                   Hidden: {self.hidden}}}"
    
class Herbivore(Animal):
    def hide(self):
        self.hidden = True
        # print(f"{self.name} is hiding.")   

class Сarnivore(Animal):
    def bite(self, herbivore):
        if not herbivore.hidden:
            herbivore.health -= 50
            print(f"{self.name} bit {herbivore.name}\
                  . {herbivore.name}'s health is now {herbivore.health}.")
            if herbivore.health <= 0:
                print(f"{herbivore.name} has died.")
                Animal.alive.remove(herbivore)
        else:
            print(f"{herbivore.name} is hiding and cannot be bitten.")
