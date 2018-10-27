-- Drops the programming_db if it already exists --
DROP DATABASE IF EXISTS sequel_db;
-- Create a database called programming_db --
CREATE DATABASE sequel_db;

USE sequel_db;

-- Create a table called movies_with_sequels
CREATE TABLE movies_with_sequels(
  -- Creates a numeric column called "id" which will automatically increment its default value as we create new rows. --
  id INT NOT NULL AUTO_INCREMENT,
  movie VARCHAR(100),
  rating INT,
  -- Creates a boolean column called "liked" (or whatever you want) which will automatically fill --
  -- with false when a new row is made and the value isn't otherwise defined. --
  liked BOOLEAN DEFAULT False,
  PRIMARY KEY (id)
);

-- Creates new rows with movie titles and ratings for each --
INSERT INTO movies_with_sequels (movie, rating, liked)
	VALUES
    ("Toy Story", 95, True),
    ("Toy Story 2", 80, True),
    ("Die Hard", 90, True),
    ("Die Harder", 75, False);

-- Display the table
SELECT * from movies_with_sequels;

-- Update the table and set liked to true where the movie's rating is greater than 75
UPDATE movies_with_sequels
	SET liked = True
    WHERE rating > 75;

-- Display the table again to see your changes --
SELECT * from movies_with_sequels;

-- Add a column called 'better_than_og' that takes a default boolean value
ALTER TABLE movies_with_sequels
	ADD better_than_og BOOLEAN DEFAULT False;

-- Update the column for movies you thought were better than the original
UPDATE movies_with_sequels
	SET better_than_og = True
    WHERE movie = "Toy Story 2";
    
-- Display the table again to see your changes --
SELECT * from movies_with_sequels;

-- Delete rows where liked and better_than_og are false
DELETE FROM movies_with_sequels
	WHERE liked = False
    AND better_than_og = False;
    
-- Display the table again to see your changes --
SELECT * from movies_with_sequels;