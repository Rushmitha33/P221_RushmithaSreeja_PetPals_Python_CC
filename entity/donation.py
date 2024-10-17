class Donation:
    def __init__(self, donor_name: str, amount: float):
        self.donor_name = donor_name
        self.amount = amount

    def record_donation(self):
        raise NotImplementedError("This method should be overridden in subclasses.")
