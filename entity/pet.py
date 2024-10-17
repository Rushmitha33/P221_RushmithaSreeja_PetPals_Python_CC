class Pet:
    def __init__(self, name: str, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}"
