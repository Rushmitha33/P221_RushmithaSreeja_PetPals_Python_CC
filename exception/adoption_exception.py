class AdoptionException(Exception):
    def __init__(self, message="Adoption error occurred."):
        self.message = message
        super().__init__(self.message)
