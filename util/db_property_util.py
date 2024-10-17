class DBPropertyUtil:
    @staticmethod
    def get_connection_string(property_file):
        # Load connection string from a properties file
        return "Driver={SQL Server};Server=RUSHMITHA\\SQLEXPRESS01;Database=PetAdoptionDB;Trusted_Connection=yes;"
