-- Drops the pokemon_db if it already exists --
DROP DATABASE IF EXISTS pokemon_db;

-- Create a database called pokemon_db --
CREATE DATABASE pokemon_db;

-- Use the database
USE pokemon_db;

-- Delete all the weak links.
DELETE FROM pokemon WHERE Total < 500;

-- Alter the table and add an auto incrementing column with a primary ID.
ALTER TABLE pokemon
	ADD id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

-- Select all dragon type Pokemon
SELECT * FROM pokemon
	WHERE `Type 1` = "Dragon";

-- Select all Pokemon that are legendary AND has a stat total greater than or equal to 600 AND are dragon types
SELECT * FROM pokemon
	WHERE Legendary = 'True'
    AND TOTAL >= 600;

-- Create a new table called gen5_legendaries based on Pokemon from Generation 5 that are legendary
CREATE TABLE gen5_legendaries LIKE pokemon;

INSERT INTO gen5_legendaries
	SELECT * FROM pokemon
	WHERE Generation = 5
    AND Legendary = 'True';

-- Find the average of each statfor all pokemon in this new table
SELECT AVG(Total), AVG(HP), AVG(Attack), AVG(Defense), AVG(`Sp. Atk`), AVG(`Sp. Def`), AVG(Speed)
	FROM pokemon;

-- Find the strongest and weakest Pokemon from this table
-- Strongest
SELECT * FROM pokemon
	WHERE total = (SELECT MAX(total) FROM pokemon);

-- Weakest
SELECT * FROM pokemon
	WHERE total = (SELECT MIN(total) FROM pokemon);

-- Create another new table called `cute_legendaries`, a cute legendary is categorized as a Pokemon with a stat total of 600 and has 100 in every stat column.
CREATE TABLE cute_legendaries LIKE pokemon;

INSERT INTO cute_legendaries
    SELECT * FROM pokemon
    WHERE Total = 600
    AND HP = 100
    AND Attack = 100
    AND Defense = 100
    AND `Sp. Atk` = 100
    AND `Sp. Def` = 100
    AND Speed = 100;
    
-- Update Legendary to be true for all Pokemon in this table
UPDATE pokemon
	SET Legendary = TRUE;