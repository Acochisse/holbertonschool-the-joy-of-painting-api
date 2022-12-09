-- this script needs to create a database of all the episodes of the "Joy of Painting" show
-- searchable by Month of airing, Colors used, and subject matter of the episode
-- the input data will be in 3 files inside of the directory "src_files"
-- the reference files are named "The Joy of Painiting - Episode List", "The Joy of Painiting - Colors Used", and "The Joy of Painting - Subject Matter

--The data has been collected from numerous sources and is everything required to create a database and API that would allow your local public broadcasting station to provide a service to filter episodes of The Joy Of Painting. Though this data is great, it was collected by three different individuals and they had three different ways they chose to store data. Please review the collected data and design a database that will store all of this information in a way that will make it usable via the API to filter episodes of The Joy of Painting.

--For this task you must:

--    Create a design document using UML documentation for the database that you will create
 --   Create the SQL scripts required to create your database from scratch based on the design document
 --       The SQL scripts must run locally when building your database
  --      You may use any SQL database you choose (examples: MySql, Postgres, SqlServer, etc.)
--column names are episode number in the format S**E** (Season 1 Episode 1 = S01E01),
--episode title, airdate, subject matter, and colors used
--using a many to many comparison to bring in the colors from a subtable and same for the subject matter


--create the database
CREATE DATABASE joy_of_painting;
CREATE TABLE joy_of_painting (
    episode_number VARCHAR(5) NOT NULL,
    episode_title VARCHAR(100) NOT NULL,
    airdate DATE NOT NULL,
    subject_matter VARCHAR(100) NOT NULL,
    colors_used VARCHAR(100) NOT NULL,
    PRIMARY KEY (episode_number)
);

-- create a multi to multi connection to a new table that will hold the colors used
CREATE TABLE colors_used (
    color_id INT NOT NULL AUTO_INCREMENT,
    color_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (color_id)
);
-- create a multi to multi connnection to a new table that will hold the subject_matter table
CREATE TABLE subject_matter (
    subject_id INT NOT NULL AUTO_INCREMENT,
    subject_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (subject_id)
);