import random
class PetShop:

    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))


class Dog:
    def speak(self):
        return "woof woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "meow meow"

    def __str__(self):
        return "Cat"


# Create a random animal
def random_animal():
    return random.choice([Dog, Cat])()

def main():
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()

    random_shop= PetShop(random_animal)
    random_shop.show_pet()

if __name__=='__main__':
    main()