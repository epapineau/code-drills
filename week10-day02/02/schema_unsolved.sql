/*
Start by creating the two tables "people" and "address".

People table contains the following columns 
* PersonId
* FirstName
* LastName
* Savings

Address table contains the following columns 
* AddressId
* PersonId
* City
* State
* Avg_Price

Check Images in README.md for table data.
*/

-- Drops the db if it already exists --
DROP DATABASE IF EXISTS joins_db;

-- Create a database called joins_db --
CREATE DATABASE joins_db;

USE joins_db;

CREATE TABLE people(
  PersonId INT NOT NULL AUTO_INCREMENT,
  FirstName VARCHAR(100),
  LastName VARCHAR(100),
  Savings INT,
  PRIMARY KEY (PersonId)
);

INSERT INTO people (FirstName, LastName, Savings)
	VALUES
    ('Tron', 'Jimmy', 10000),
    ('Saw', 'Bobert', 15000),
    ('Sing', 'Derick', 10000),
    ('Paste', 'Sosha', 20000),
    ('Claw', 'Rick', 18000);
    
CREATE TABLE address(
  AddressId INT NOT NULL AUTO_INCREMENT,
  PersonId Int,
  City VARCHAR(100),
  State VARCHAR(100),
  Avg_Price INT,
  PRIMARY KEY (AddressId)
);

INSERT INTO address (PersonId, City, State, Avg_Price)
	VALUES
    (1, 'San Jose', 'California', 100000),
    (2, 'Oakland', 'California', 800000),
    (4, 'Oakland', 'California', 800000),
    (5, 'Richmond', 'California', 750000),
    (7, 'San Francisco', 'Califnornia', 200000);