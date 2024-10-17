class NullReferenceException(Exception):
    def __init__(self, message="Pet information is missing."):
        self.message = message
        super().__init__(self.message)
