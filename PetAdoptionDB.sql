-- Create the database
CREATE DATABASE PetAdoptionDB;


USE PetAdoptionDB;


-- Create Pets table
CREATE TABLE Pets (
    PetID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100),
    Age INT CHECK (Age > 0),  -- Age must be a positive integer
    Breed NVARCHAR(100)
);
GO

-- Create Donations table
CREATE TABLE Donations (
    DonationID INT PRIMARY KEY IDENTITY(1,1),
    DonorName NVARCHAR(100),
    Amount DECIMAL(10, 2) CHECK (Amount >= 10.00),  -- Minimum donation of $10
    DonationDate DATETIME DEFAULT GETDATE()
);
GO

-- Create AdoptionEvents table
CREATE TABLE AdoptionEvents (
    EventID INT PRIMARY KEY IDENTITY(1,1),
    EventName NVARCHAR(100),
    EventDate DATE
);
GO


USE PetAdoptionDB;

-- Insert initial data into Pets
INSERT INTO Pets (Name, Age, Breed) VALUES ('Buddy', 3, 'Golden Retriever');
INSERT INTO Pets (Name, Age, Breed) VALUES ('Mittens', 2, 'Siamese');
INSERT INTO Pets (Name, Age, Breed) VALUES ('Max', 5, 'Beagle');
INSERT INTO Pets (Name, Age, Breed) VALUES ('Whiskers', 4, 'Persian');

-- Insert initial data into Donations
INSERT INTO Donations (DonorName, Amount, DonationDate) 
VALUES ('Alice Johnson', 50.00, GETDATE());
INSERT INTO Donations (DonorName, Amount, DonationDate) 
VALUES ('Bob Smith', 20.00, GETDATE());

-- Insert initial data into AdoptionEvents
INSERT INTO AdoptionEvents (EventName, EventDate) 
VALUES ('Spring Adoption Fair', '2024-04-15');
INSERT INTO AdoptionEvents (EventName, EventDate) 
VALUES ('Summer Paw-tacular', '2024-08-10');


select * from Donations;
select * from Pets;
select * from AdoptionEvents;