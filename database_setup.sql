CREATE DATABASE Colabs_Ecosystem;
USE Colabs_Ecosystem;

CREATE TABLE Members (
    MemberID INT PRIMARY KEY IDENTITY(1,1),
    FullName VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    JoinDate DATE,
    MembershipType VARCHAR(50)
);

CREATE TABLE Desks_Rooms (
    ResourceID INT PRIMARY KEY IDENTITY(101,1),
    ResourceName VARCHAR(50) NOT NULL,
    ResourceType VARCHAR(30),
    HourlyRate DECIMAL(10,2)
);

CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY IDENTITY(1001,1),
    MemberID INT,
    ResourceID INT,
    BookingDate DATE,
    HoursUsed INT,
    AmountPaid DECIMAL(10,2),
    PaymentStatus VARCHAR(20)
);

-- 2. "Ganda Data" Insert Karein
INSERT INTO Members (FullName, Email, JoinDate, MembershipType) VALUES
('Ahmed Ali', 'ahmed.ali@email.com', '2026-01-15', 'Hot Desk'),
('Fatima Khan', NULL, '2026-02-01', 'Private Office'),
('Zainab Hassan', 'zainab@email.com', '2026-03-10', 'Dedicated Desk'),
('Bilal Siddiqui', 'bilal.siddique@email.com', NULL, 'Hot Desk');

INSERT INTO Desks_Rooms (ResourceName, ResourceType, HourlyRate) VALUES
('Desk-A1', 'Desk', 200.00),
('Desk-A2', 'Desk', 200.00),
('Chinar-Room', 'Meeting Room', 1500.00),
('Shahkar-Cabin', 'Cabin', 800.00);

INSERT INTO Bookings (MemberID, ResourceID, BookingDate, HoursUsed, AmountPaid, PaymentStatus) VALUES
(1, 101, '2026-05-10', 4, 800.00, 'Paid'),
(2, 103, '2026-05-11', 2, 3000.00, 'Paid'),
(3, 102, '2026-05-12', 5, NULL, 'Pending'),
(4, 104, '2026-05-12', NULL, 0.00, NULL),
(1, 103, '2026-05-13', 3, 4500.00, 'Paid');

SELECT * FROM Bookings;
select * from Members;
select * from Desks_Rooms;