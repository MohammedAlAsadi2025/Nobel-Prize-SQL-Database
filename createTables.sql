DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Individual;
DROP TABLE IF EXISTS Organisation;
DROP TABLE IF EXISTS Laureate;
DROP TABLE IF EXISTS Prize;

CREATE TABLE Prize(
    Id            VARCHAR(4) NOT NULL,
    prizeName     VARCHAR(100) NOT NULL,
    description   VARCHAR(400),
    amountAwarded INT,
    dateAwarded   VARCHAR(10),
    PRIMARY KEY(Id)
);

CREATE TABLE Laureate(
    Id VARCHAR(4) NOT NULL,
    PRIMARY KEY(Id),
    FOREIGN KEY(Id) REFERENCES Prize(Id)
);

CREATE TABLE Organisation(
    Id           VARCHAR(4) NOT NULL,
    orgName      VARCHAR(100) NOT NULL,
    orgCountry   VARCHAR(100) NOT NULL,
    dateFounded  VARCHAR(10) NOT NULL,
    PRIMARY KEY(Id),
    FOREIGN KEY(Id) REFERENCES Laureate(Id)
);

CREATE TABLE Individual(
    Id         VARCHAR(4) NOT NULL,
    firstName  VARCHAR(25),
    lastName   VARCHAR(25),
    gender     VARCHAR(6),
    birthDate  VARCHAR(10),
    PRIMARY KEY(Id),
    FOREIGN KEY(Id) REFERENCES Laureate(Id)
);

CREATE TABLE Country(
    Id           VARCHAR(4) NOT NULL,
    birthCountry VARCHAR(100),
    deathCountry VARCHAR(100),
    PRIMARY KEY(Id),
    FOREIGN KEY(Id) REFERENCES Individual(Id)
);
