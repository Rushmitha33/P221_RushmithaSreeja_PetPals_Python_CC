import pyodbc
from entity.donation import Donation

class DonationDAO:
    def __init__(self, connection):
        self.connection = connection

    def record_cash_donation(self, donor_name: str, amount: float):
        try:
            cursor = self.connection.cursor()
            # Update the column names to match your schema
            cursor.execute("INSERT INTO Donations (DonorName, Amount) VALUES (?, ?)", (donor_name, amount))
            self.connection.commit()
        except Exception as e:
            print(f"Error recording donation: {e}")
