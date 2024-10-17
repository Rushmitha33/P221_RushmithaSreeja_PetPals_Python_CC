class InvalidPetAgeException(Exception):
    def __init__(self, message="Invalid pet age. Age must be a positive integer."):
        self.message = message
        super().__init__(self.message)
