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
    month_and_day VARCHAR(100) NOT NULL,
    year VARCHAR(100) NOT NULL,
    APPLE_FRAME TINYINT NOT NULL,
    AURORA_BOREALIS TINYINT NOT NULL,
    BARN TINYINT NOT NULL,
    BEACH TINYINT NOT NULL,
    BOAT TINYINT NOT NULL,
    BRIDGE TINYINT NOT NULL,
    BUILDING TINYINT NOT NULL,
    BUSHES TINYINT NOT NULL,
    CABIN TINYINT NOT NULL,
    CACTUS TINYINT NOT NULL,
    CIRCLE_FRAME TINYINT NOT NULL,
    CIRRUS TINYINT NOT NULL,
    CLIFF TINYINT NOT NULL,
    CLOUDS TINYINT NOT NULL,
    CONIFER TINYINT NOT NULL,
    CUMULUS TINYINT NOT NULL,
    DECIDUOUS TINYINT NOT NULL,
    DIANE_ANDRE TINYINT NOT NULL,
    DOCK TINYINT NOT NULL,
    DOUBLE_OVAL_FRAME TINYINT NOT NULL,
    FARM TINYINT NOT NULL,
    FENCE TINYINT NOT NULL,
    FIRE TINYINT NOT NULL,
    FLORIDA_FRAME TINYINT NOT NULL,
    FLOWERS TINYINT NOT NULL,
    FOG TINYINT NOT NULL,
    FRAMED TINYINT NOT NULL,
    GRASS TINYINT NOT NULL,
    GUEST TINYINT NOT NULL,
    HALF_CIRCLE_FRAME TINYINT NOT NULL,
    HALF_OVAL_FRAME TINYINT NOT NULL,
    HILLS TINYINT NOT NULL,
    LAKE TINYINT NOT NULL,
    LAKES TINYINT NOT NULL,
    LIGHTHOUSE TINYINT NOT NULL,
    MILL TINYINT NOT NULL,
    MOON TINYINT NOT NULL,
    MOUNTAIN TINYINT NOT NULL,
    MOUNTAINS TINYINT NOT NULL,
    NIGHT TINYINT NOT NULL,
    OCEAN TINYINT NOT NULL,
    OVAL_FRAME TINYINT NOT NULL,
    PALM_TREES TINYINT NOT NULL,
    PATH TINYINT NOT NULL,
    PERSON TINYINT NOT NULL,
    PORTRAIT TINYINT NOT NULL,
    RECTANGLE_3D_FRAME TINYINT NOT NULL,
    RECTANGULAR_FRAME TINYINT NOT NULL,
    RIVER TINYINT NOT NULL,
    ROCKS TINYINT NOT NULL,
    SEASHELL_FRAME TINYINT NOT NULL,
    SNOW TINYINT NOT NULL,
    SNOWY_MOUNTAIN TINYINT NOT NULL,
    SPLIT_FRAME TINYINT NOT NULL,
    STEVE_ROSS TINYINT NOT NULL,
    STRUCTURE TINYINT NOT NULL,
    SUN TINYINT NOT NULL,
    TOMB_FRAME TINYINT NOT NULL,
    TREE TINYINT NOT NULL,
    TREES TINYINT NOT NULL,
    TRIPLE_FRAME TINYINT NOT NULL,
    WATERFALL TINYINT NOT NULL,
    WAVES TINYINT NOT NULL,
    WINDMILL TINYINT NOT NULL,
    WINDOW_FRAME TINYINT NOT NULL,
    WINTER TINYINT NOT NULL,
    WOOD_FRAMED TINYINT NOT NULL,
    Black_Gesso TINYINT NOT NULL,
    Bright_Red TINYINT NOT NULL,
    Burnt_Umber TINYINT NOT NULL,
    Cadmium_Yellow TINYINT NOT NULL,
    Dark_Sienna TINYINT NOT NULL,
    Indian_Red TINYINT NOT NULL,
    Indian_Yellow TINYINT NOT NULL,
    Liquid_Black TINYINT NOT NULL,
    Liquid_Clear TINYINT NOT NULL,
    Midnight_Black TINYINT NOT NULL,
    Phthalo_Blue TINYINT NOT NULL,
    Phthalo_Green TINYINT NOT NULL,
    Prussian_Blue TINYINT NOT NULL,
    Sap_Green TINYINT NOT NULL,
    Titanium_White TINYINT NOT NULL,
    Van_Dyke_Brown TINYINT NOT NULL,
    Yellow_Ochre TINYINT NOT NULL,
    Alizarin_Crimson TINYINT NOT NULL,