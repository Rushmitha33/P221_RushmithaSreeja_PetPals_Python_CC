from entity.pet import Pet

class Dog(Pet):
    def __init__(self, name: str, age: int, breed: str, dog_breed: str):
        super().__init__(name, age, breed)
        self.dog_breed = dog_breed

    def __str__(self):
        return super().__str__() + f", Dog Breed: {self.dog_breed}"
