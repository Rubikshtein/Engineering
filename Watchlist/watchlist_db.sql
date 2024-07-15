CREATE DATABASE IF NOT EXISTS WatchlistDB;

USE WatchlistDB;

SET GLOBAL general_log = 'ON';
SET GLOBAL general_log = 1;
SET GLOBAL log_output = 'table';
SELECT * FROM mysql.general_log;



-- Table for platforms, each platform ID and name are unique to prevent duplicate entries, ID generated automatically
CREATE TABLE IF NOT EXISTS Platform (
platform_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
platform_name VARCHAR(100) NOT NULL,
monthly_cost DECIMAL(4,2),
-- UNIQUE (platform_ID),
UNIQUE (platform_name)
);

-- Table for programmes, each programme ID and name are unique to prevent duplicate entries, ID generated automatically
CREATE TABLE IF NOT EXISTS Programme (
programme_ID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
programme_name VARCHAR(100) NOT NULL,
-- ENUM to ensure only two types of values are accepted
programme_type ENUM('series', 'film'),
UNIQUE (programme_name)
);

/*Table for films and their duration, programme ID is defined as primary key to ensure it's unique to teh table, as well as a foreign key to correspond 
programme ID in Programme table */
CREATE TABLE IF NOT EXISTS Films (
programme_ID INTEGER NOT NULL PRIMARY KEY,
duration_minutes FLOAT, 
CONSTRAINT
fk_programme_ID_films
FOREIGN KEY
(programme_ID)
REFERENCES Programme
(programme_ID)
);

-- Table for series and and their total episodes
CREATE TABLE IF NOT EXISTS Series (
programme_ID INTEGER NOT NULL PRIMARY KEY,
total_episodes INTEGER,
CONSTRAINT
fk_programme_ID_series
FOREIGN KEY
(programme_ID)
REFERENCES Programme
(programme_ID)
);

-- Table for cast (director, main actor, supporting actor, etc.)
CREATE TABLE IF NOT EXISTS Cast (
cast_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
programme_ID INTEGER NOT NULL,
director_name VARCHAR(100),
lead_actor VARCHAR(100),
actor_name VARCHAR(100),
CONSTRAINT
fk_programme_ID_cast
FOREIGN KEY
(programme_ID)
REFERENCES Programme
(programme_ID)
);

-- Table for genres
CREATE TABLE IF NOT EXISTS Genre (
genre_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
genre_name VARCHAR(100) NOT NULL,
UNIQUE (genre_name)
);

-- Table to add genres for programmes
CREATE TABLE IF NOT EXISTS Programme_Genre (
programme_ID INTEGER NOT NULL,
genre_ID INTEGER NOT NULL,
CONSTRAINT
fk_programme_ID_p_genre
FOREIGN KEY
(programme_ID)
REFERENCES Programme
(programme_ID),
CONSTRAINT
fk_genre_ID_p_genre
FOREIGN KEY
(genre_ID)
REFERENCES Genre
(genre_ID),
PRIMARY KEY (programme_ID, genre_ID) -- each pair unique
);

-- Table for films progress, tracked in minutes, each programme ID is unique to the table
CREATE TABLE IF NOT EXISTS Progress_Films (
programme_ID INTEGER NOT NULL,
minutes_watched FLOAT DEFAULT NULL,
CONSTRAINT
fk_programme_ID_progress_films
FOREIGN KEY
(programme_ID)
REFERENCES Programme
(programme_ID),
UNIQUE (programme_ID)
);

-- Table for series progress, tracked in episodes watched, each programme ID is unique to the table
CREATE TABLE IF NOT EXISTS Progress_Series (
programme_ID INTEGER NOT NULL,
episodes_watched FLOAT DEFAULT NULL,
CONSTRAINT
fk_programme_ID_progress_series
FOREIGN KEY
(programme_ID)
REFERENCES Programme
(programme_ID),
UNIQUE (programme_ID)
);

-- Query to insert data into Platform table (ID generated automatically so name and cost only)
INSERT INTO Platform
(platform_name, monthly_cost)
VALUES
('Netflix', 10.99),
('Amazon Prime', 8.99),
('Disney+', 10.99),
('BBC iPlayer', 0.00);

-- Query to display all platforms from most expensive to cheapest
SELECT * FROM Platform ORDER BY monthly_cost DESC;

-- Query to insert data into Programme (ID generated automatically so name and type only)
INSERT INTO Programme
(programme_name, programme_type)
VALUES
('Bridgerton', 'series'),
('Emily in Paris', 'series'),
('Vamprire Diaries', 'series'),
('Killing Eve', 'series'),
('Upload', 'series'),
('Fallout', 'series'),
('Baby Reindeer', 'series'),
('The Marvels', 'film'),
('Ant-Man and the Wasp: Quantumania', 'film'),
('Atlas', 'film'),
('Poor Things', 'film'),
('Titanic', 'film');

-- Query to display programmes ordered by type
SELECT * FROM Programme ORDER BY programme_type;

-- Below query will result in an error because only films/series are allowed as programme types
-- INSERT INTO Programme
-- (programme_name, programme_type)
-- VALUES
-- ('MAFSA', 'TV show');

-- Query to insert data into Films
INSERT INTO Films
(programme_ID, duration_minutes)
VALUES
(8, 120),
(9, 122),
(10, 126),
(11, 132.6),
(12, 188.4);

-- Query to display films from shortest to longest
SELECT * FROM Films ORDER BY duration_minutes;

-- Query to insert data into series
INSERT INTO Series
(programme_ID, total_episodes)
VALUES
(1, 16),
(2, 20),
(3, 171),
(4, 24),
(5, 10),
(6, 12),
(7, 8);

-- Query to display series from longest to shortest
SELECT * FROM Series ORDER BY total_episodes DESC;

-- Query to insert data into Cast
INSERT INTO Cast
(programme_ID, director_name, lead_actor, actor_name)
VALUES
(1, 'Tom Verica', 'Phoebe Dynevor', 'Rege-Jean Page'),
(2, 'Andrew Fleming', 'Lily Collins', 'Ashley Park'),
(3, 'Chris Grismer', 'Nina Dobrev', 'Ian Somerhalder'),
(4, 'Damon Thomas', 'Sandra Oh', 'Jodie Comer'),
(5, 'Greg Daniels', 'Robbie Amell', 'Andy Allo'),
(6, 'Jonathan Nolan', 'Ella Purnell', 'Walton Goggings'),
(7, 'Weronika Tofilska', 'Jessica Gunning', 'Richard Gadd'),
(8, 'Nia DaCosta', 'Brie Larson', 'Iman Vellani'),
(9, 'Peyton Reed', 'Paul Rudd', 'Evangeline Lilly'),
(10, 'Brad Peyton', 'Jennifer Lopez', 'Sterling K. Brown'),
(11, 'Yorgos Lanthimos', 'Emma Stone', 'Mark Ruffalo'),
(12, 'James Cameron', 'Kate Winslet', 'Leonardo DiCaprio');

-- Query to display all cast information
SELECT * FROM Cast;

-- Query to insert data into Genre
INSERT INTO Genre 
(genre_name)
VALUES
('Romance'),
('Comedy'),
('Thriller'),
('Sci-Fi'),
('Action'),
('Steampunk'),
('Fiction'),
('Adventure'),
('Fantasy'),
('Drama'),
('Biography'),
('History');

-- Query to display all genres i alphabetical order
SELECT * FROM Genre ORDER BY genre_name;

-- Query to insert data into Programme_Genre
INSERT INTO Programme_Genre
(programme_ID, genre_ID)
VALUES
(1, 1),
(1, 12),
(1, 10),
(2, 1),
(2, 2),
(2, 10),
(3, 10),
(3, 1),
(3, 3),
(4, 5),
(4, 2),
(4, 3),
(5, 2),
(5, 4),
(6, 5),
(6, 2),
(6, 4),
(7, 11),
(7, 3),
(7, 10),
(8, 5),
(8, 8),
(8, 9),
(9, 5),
(9, 8),
(9, 9),
(10, 5),
(10, 4),
(11, 2),
(11, 6),
(11, 1),
(12, 1),
(12, 5),
(12, 8);

-- Query to display programme IDs and their genres
SELECT * FROM Programme_Genre ORDER BY programme_ID;

-- Query to insert data into Progress_Series
INSERT INTO Progress_Series
(programme_ID, episodes_watched)
VALUES
(1, 16),
(2, 18),
(3, 171),
(4, 20),
(5, 10),
(6, 11),
(7, 0);

-- Query to display progress for all series
SELECT * FROM Progress_Series;

-- Query to insert data into Films progress
INSERT INTO Progress_Films
(programme_ID, minutes_watched)
VALUES
(8, 70),
(9, 122),
(10, 126),
(11, 0),
(12, 189);

-- Query to display progress for all films
SELECT * FROM Progress_Films;

-- Aggregate Function to count all series on the watchlist

SELECT COUNT(*) AS total_series
FROM Programme
WHERE programme_type = 'series';

-- Aggregate Function to count all films on the watchlist

SELECT COUNT(*) AS total_films
FROM Programme
WHERE programme_type = 'film';

-- Aggregate Function to establish average film length in hours

SELECT AVG(duration_minutes) AS average_film_length
FROM Films;

-- Function to display shortest series (joins Programme and Series tables and selects series with least total episodes)

SELECT
	p.programme_name AS shortest_series,
	s.total_episodes
FROM 
	Programme p
JOIN 
	Series s ON p.programme_ID = s.programme_ID
WHERE
	s.total_episodes = (
		SELECT MIN(total_episodes) FROM Series
	);

-- Query to display series progress (joins Programme, Progress_Series and Series tables)

SELECT
p.programme_name,
ps.episodes_watched,
s.total_episodes
FROM 
Programme p
JOIN
Progress_Series ps ON p.programme_ID = ps.programme_ID
JOIN
Series s ON p.programme_ID = s.programme_ID;

-- Query to display films progress (joins Programme, Progress_Films and Films tables)

SELECT
p.programme_name,
pf.minutes_watched,
f.duration_minutes
FROM 
Programme p
JOIN
Progress_Films pf ON p.programme_ID = pf.programme_ID
JOIN
Films f ON p.programme_ID = f.programme_ID;

-- TRIGGERS and STORED PROCEDURES
-- Create all triggers before creating and calling any stored procedures

-- TRIGGER to mark films as watched once deleted from Progress_Films (used for stored procedure)

/*
DELIMITER //
CREATE TRIGGER Mark_Film_As_Watched
-- records deleted from progress table by stored procedure
AFTER DELETE ON Progress_Films
FOR EACH ROW
BEGIN
    -- this variable is needed for update condition
	DECLARE film_duration FLOAT;
    
    -- assign retrieved value into a variable
    SELECT duration_minutes INTO film_duration
    FROM Films
    WHERE programme_ID = OLD.programme_ID;
    
    -- condition required to update programme_name in Programme table
	IF OLD.minutes_watched >= film_duration THEN
		UPDATE Programme
        -- (watched) is added to programme_name string
        SET programme_name = CONCAT(programme_name, ' (watched)')
        WHERE programme_ID = OLD.programme_ID;
	END IF;
END //
DELIMITER ;
*/

-- TRIGGER to mark series as watched once deleted from Progress_Series (used for stored procedure)

/*
DELIMITER //
CREATE TRIGGER Mark_Series_As_Watched
-- records deleted from progress table by stored procedure
AFTER DELETE ON Progress_Series
FOR EACH ROW
BEGIN
	-- this variable is needed for update condition
	DECLARE episodes FLOAT;
    -- assign retrieved value into a variable
    SELECT total_episodes INTO episodes
    FROM Series
    WHERE programme_ID = OLD.programme_ID;
    
    -- condition required to update programme_name in Programme table
	IF OLD.episodes_watched >= episodes THEN
		UPDATE Programme
        -- (watched) is added to programme_name string
        SET programme_name = CONCAT(programme_name, ' (watched)')
        WHERE programme_ID = OLD.programme_ID;
	END IF;
END //
DELIMITER ;
*/

-- If stored procedure is rolled back, but then data re-inserted, programme names would still be flagged as watched, so more triggers required

-- TRIGGER to revert Mark_Films_As_Watched in Programme table if stored procedure to remove film from Progress_Films is rolled back 

/*
DELIMITER //
CREATE TRIGGER Unmark_Watched_Films
-- data reinstated
AFTER INSERT ON Progress_Films
FOR EACH ROW
BEGIN 
	UPDATE Programme
    -- REPLACE function will replace (watched) flad with empty string
    SET programme_name = REPLACE(programme_name, ' (watched)', '')
    WHERE programme_ID = NEW.programme_ID;
END //
DELIMITER ;
*/

-- TRIGGER to revert Mark_Series_As_Watched in Programme table if stored procedure to remove series from Progress_Series is rolled back

/*
DELIMITER //
CREATE TRIGGER Unmark_Watched_Series
-- data reinstated
AFTER INSERT ON Progress_Series
FOR EACH ROW
BEGIN 
	UPDATE Programme
    -- REPLACE function will replace (watched) flad with empty string
    SET programme_name = REPLACE(programme_name, ' (watched)', '')
    WHERE programme_ID = NEW.programme_ID;
END //
DELIMITER ;
*/

-- STORED PROCEDURE to delete watched films (once minutes_watched from Progress_Films are equal or greater to duration_minutes from Films table)

/*
DELIMITER //
CREATE PROCEDURE Remove_Watched_Films()
BEGIN
	DELETE pf
    FROM Progress_Films pf
    INNER JOIN Films f ON pf.programme_ID = f.programme_ID
    WHERE pf.minutes_watched >= f.duration_minutes;
END //
DELIMITER ;

-- MySQL is in safe update mode, use below command to disable safe update mode for the duration of the session to be able to call the procedure)
SET sql_safe_updates = 0;

-- Call function within transaction to be able to revert changes or commit
START TRANSACTION;
CALL Remove_Watched_Films();

-- Check film progress query - Atlas, Ant-Man and Titanic are removed
SELECT
p.programme_name,
pf.minutes_watched,
f.duration_minutes
FROM 
Programme p
JOIN
Progress_Films pf ON p.programme_ID = pf.programme_ID
JOIN
Films f ON p.programme_ID = f.programme_ID;

-- Query to display watched programmes
SELECT UPPER(programme_name) AS Watched_Programmes
FROM Programme
WHERE programme_name LIKE '%watched%';

-- Programme names are marked as watched in Programme table
SELECT * FROM Programme WHERE programme_type = 'film';

ROLLBACK;
*/

-- Rollback: Progress_Films will be updated and programme names in Programmes unmarked as watched (use progress and programme queries to test)

-- Procedure and triggers can be removed if necessary

-- DROP PROCEDURE Remove_Watched_Films;
-- DROP TRIGGER IF EXISTS Mark_Film_As_Watched;
-- DROP TRIGGER IF EXISTs Unmark_Watched_Films;

-- STORED PROCEDURE to delete watched series (once episodes_watched from Progress_Series are equal or greater to total_episodes from Series table)

/*
DELIMITER //
CREATE PROCEDURE Remove_Watched_Series()
BEGIN
	DELETE ps
    FROM Progress_Series ps
    INNER JOIN Series s ON ps.programme_ID = s.programme_ID
    WHERE ps.episodes_watched >= s.total_episodes;
END //
DELIMITER ;

-- Call function within transaction to be able to revert changes or commit 
START TRANSACTION;
CALL Remove_Watched_Series();

-- Check series progress - Bridgerton, Vampire Diaries and Upload have been removed
SELECT
p.programme_name,
ps.episodes_watched,
s.total_episodes
FROM 
Programme p
JOIN
Progress_Series ps ON p.programme_ID = ps.programme_ID
JOIN
Series s ON p.programme_ID = s.programme_ID;

-- Query to display watched programmes
SELECT UPPER(programme_name) AS Watched_Programmes
FROM Programme
WHERE programme_name LIKE '%watched%';

-- Programme names are marked as watched in Programme table
SELECT * FROM Programme WHERE programme_type = 'series';

ROLLBACK;
*/

-- Progress_Series will be updated and programme names in Programmes unmarked as watched (use progress and programme queries to test)

-- Procedure and triggers can be removed if necessary

-- DROP PROCEDURE Remove_Watched_Series;
-- DROP TRIGGER IF EXISTS Mark_Series_As_Watched;
-- DROP TRIGGER IF EXISTS Unmark_Watched_Series;

-- Call procedures again and commit to preserve changes (uncomment desired outcome)

-- START TRANSACTION;
-- CALL Remove_Watched_Series();
-- CALL Remove_Watched_Films();
-- ROLLBACK;
-- COMMIT;

-- Check results

-- SELECT * FROM Programme;

-- As I am not doing anything with Cast table yet, it can be removed

-- DROP TABLE Cast;





