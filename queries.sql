#Query where prize money is over 1 million
SELECT * FROM Prize WHERE amountAwarded > 1000000;

#Query where all individual winners who have names that start with A
SELECT * FROM Individual WHERE firstName LIKE 'A%';

#Query that shows all women who have won a Nobel Prize
SELECT iD, firstName FROM Individual WHERE gender = 'female';

#Query with all nobel prize winners from Denmark
SELECT i.firstName, i.lastName
FROM Individual i
JOIN Country c ON i.Id = c.Id 
WHERE c.birthCountry = 'Denmark';

#Query that shows individual winners who died in a country different from their birth country.
SELECT i.firstName, i.lastName, c.birthCountry, c.deathCountry
FROM Individual i
JOIN Country c ON i.Id = c.Id 
WHERE c.birthCountry <> c.deathCountry AND c.deathCountry <> 'nan'; 

#Query that creates a union of the counts for individuals and organizations
SELECT Country, SUM(Count) as TotalLaureates
FROM
(
    #Counting individuals
    SELECT c.birthCountry AS Country, COUNT(i.Id) AS Count
    FROM Individual i
    JOIN Country c ON i.Id = c.Id
    GROUP BY c.birthCountry

    UNION ALL

    #Counting organizations
    SELECT orgCountry AS Country, COUNT(Id) AS Count
    FROM Organisation
    GROUP BY orgCountry
) AS combined
GROUP BY Country
ORDER BY TotalLaureates DESC;
