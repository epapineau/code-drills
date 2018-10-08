-- Show all data if people table's PersonId has a corresponding PersonId from Address table. See image 1 for output.
SELECT * FROM people
	RIGHT JOIN address
    ON people.PersonId = address.PersonId;

-- Show all data from people and add their corresponding address from Address table based on PersonId. See image 2 for output.
SELECT * FROM people
	LEFT JOIN address
    ON people.PersonId = address.PersonId;

-- Show all data from Address and add their corresponding person from people table based on PersonId.  See image 3 for output.
SELECT * FROM people
	RIGHT JOIN address
    ON people.PersonId = address.PersonId;

-- Show person's ID, LastName, FirstName, Savings, Avg_Price, and the TotalValue. TotalValue is defined as the sum of Savings + Avg_Price
-- See image 4 for output.
SELECT people.PersonId, people.LastName, people.FirstName, people.Savings, address.Avg_Price, (people.Savings + address.Avg_Price) AS TotalValue
	FROM people
	JOIN address
    ON people.PersonId = address.PersonId;