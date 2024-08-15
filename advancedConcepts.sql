DROP PROCEDURE IF EXISTS DeleteById;
DROP PROCEDURE IF EXISTS UpdateById;

DELIMITER //

CREATE PROCEDURE DeleteById(IN targetId VARCHAR(4))
BEGIN
    -- Start by deleting from tables with foreign key constraints
    DELETE FROM Country WHERE Id = targetId;
    DELETE FROM Individual WHERE Id = targetId;
    DELETE FROM Organisation WHERE Id = targetId;
    DELETE FROM Laureate WHERE Id = targetId;
    DELETE FROM Prize WHERE Id = targetId;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE UpdateById(oldId VARCHAR(4), newId VARCHAR(4))
BEGIN
    START TRANSACTION;

    -- Insert new record in the main table
    INSERT INTO Prize (Id, prizeName, description, amountAwarded, dateAwarded)
    SELECT newId, prizeName, description, amountAwarded, dateAwarded
    FROM Prize WHERE Id = oldId;

    -- First, update the child tables 
    UPDATE Country SET Id = newId WHERE Id = oldId;
    UPDATE Individual SET Id = newId WHERE Id = oldId;
    UPDATE Organisation SET Id = newId WHERE Id = oldId;

    -- Then, update the parent table 
    UPDATE Laureate SET Id = newId WHERE Id = oldId;

    -- Delete old record from the main table
    DELETE FROM Prize WHERE Id = oldId;

    COMMIT;
END //

DELIMITER ;

CREATE VIEW OrganisationPrizes AS
SELECT 
    o.Id, o.orgName, o.orgCountry, o.dateFounded,
    p.prizeName, p.description, p.amountAwarded, p.dateAwarded
FROM Organisation o
JOIN Prize p ON o.Id = p.Id;

CREATE VIEW LaureateWinnings AS
SELECT 
    l.Id AS laureateId,
    COALESCE(i.firstName, o.orgName) AS firstNameOrOrgName,
    i.lastName,
    p.amountAwarded
FROM Laureate l
JOIN Prize p ON l.Id = p.Id
LEFT JOIN Individual i ON l.Id = i.Id
LEFT JOIN Organisation o ON l.Id = o.Id;
