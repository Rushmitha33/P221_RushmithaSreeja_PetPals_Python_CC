import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            connection = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=RUSHMITHA\\SQLEXPRESS01;'  # Use the correct server name (e.g., localhost or IP)
                'DATABASE=PetAdoptionDB;'  # Your database name
                'Trusted_Connection=yes;'  # This enables Windows Authentication
            )
            return connection
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None
