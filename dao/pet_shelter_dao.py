from entity.pet import Pet
class PetShelterDAO:
    def __init__(self, connection):
        self.connection = connection

    def add_pet(self, pet):
        cursor = self.connection.cursor()
        query = "INSERT INTO pets (name, age, breed) VALUES (?, ?, ?)"
        cursor.execute(query, (pet.name, pet.age, pet.breed))
        self.connection.commit()

    def fetch_available_pets(self):
        cursor = self.connection.cursor()
        query = "SELECT name, age, breed FROM pets"
        cursor.execute(query)
        rows = cursor.fetchall()
        pets = [Pet(row[0], row[1], row[2]) for row in rows]
        return pets

    def remove_pet(self, name):
        cursor = self.connection.cursor()
        query = "DELETE FROM pets WHERE name = ?"
        cursor.execute(query, (name,))
        self.connection.commit()  # Don't forget to commit the changes
