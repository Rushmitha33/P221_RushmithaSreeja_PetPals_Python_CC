from util.db_conn_util import DBConnUtil
from dao.donation_dao import DonationDAO
from dao.pet_shelter_dao import PetShelterDAO
from exception.invalid_pet_age_exception import InvalidPetAgeException
from exception.insufficient_funds_exception import InsufficientFundsException
from exception.adoption_exception import AdoptionException
from util.file_util import read_pets_from_file
from entity.pet import Pet

def adopt_pet(pet_name, pet_shelter):
    available_pets = pet_shelter.fetch_available_pets()
    
    for pet in available_pets:
        if pet.name.lower() == pet_name.lower():
            pet_shelter.remove_pet(pet.name)  # Pass the pet's name, not the object
            print(f"Congratulations! You've adopted {pet_name}.")
            return

    # If pet is not found
    raise AdoptionException(f"Pet '{pet_name}' not available for adoption.")

def main():
    connection = DBConnUtil.get_connection()
    pet_shelter = PetShelterDAO(connection)
    donation_dao = DonationDAO(connection)

    while True:
        print("\nMenu:")
        print("1. Add Pet")
        print("2. List Available Pets")
        print("3. Record Cash Donation")
        print("4. Read Pets from File")
        print("5. Adopt a Pet")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter pet name: ")
            try:
                age = int(input("Enter pet age: "))
                if age <= 0:
                    raise InvalidPetAgeException()
                breed = input("Enter pet breed: ")
                pet = Pet(name, age, breed)
                pet_shelter.add_pet(pet)  # Save to the database
                print(f"{name} added successfully!")
            except ValueError:
                print("Invalid age. Please enter a positive integer.")
            except InvalidPetAgeException as e:
                print(e)

        elif choice == '2':
            print("Available Pets:")
            available_pets = pet_shelter.fetch_available_pets()
            if available_pets:
                for pet in available_pets:
                    print(f"Name: {pet.name}, Age: {pet.age}, Breed: {pet.breed}")
            else:
                print("No available pets.")

        elif choice == '3':
            try:
                donor_name = input("Enter donor name: ")
                amount = float(input("Enter donation amount: "))
                if amount < 10.00:
                    raise InsufficientFundsException()
                donation_dao.record_cash_donation(donor_name, amount)
                print("Donation recorded successfully!")
            except ValueError:
                print("Invalid amount. Please enter a number.")
            except InsufficientFundsException as e:
                print(e)

        elif choice == '4':
            file_path = input("Enter the path to the pets file: ")
            pets_from_file = read_pets_from_file(file_path)
            if pets_from_file:
                for pet in pets_from_file:
                    pet_shelter.add_pet(pet)  # Save pets from file to the DB
                print("Pets added from file.")
            else:
                print("No pets added.")

        elif choice == '5':
            pet_name = input("Enter the name of the pet to adopt: ")
            try:
                adopt_pet(pet_name, pet_shelter)  # Implementing adoption logic
            except AdoptionException as e:
                print(e)

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
