from entity.pet import Pet

def read_pets_from_file(file_path):
    pets = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, age, breed = line.strip().split(',')
                pets.append(Pet(name, int(age), breed))
        return pets
    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: An error occurred while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
