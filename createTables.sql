SET sql_safe_updates = FALSE;

USE defaultdb;
DROP DATABASE IF EXISTS coursemanager CASCADE;
CREATE DATABASE IF NOT EXISTS coursemanager;

USE coursemanager;

DROP TABLE IF EXISTS coursereviews;

CREATE TABLE coursereviews (
    coursename VARCHAR(200) PRIMARY KEY NOT NULL,
    professor  VARCHAR(100),
    semester ENUM('Fall 2020', 'Spring 2021', 'Fall 2021', 'Spring 2022', 'Fall 2022'),
    courseload INTEGER,
    reviews LONGTEXT,
    industryroles ENUM('Data Scientist', 'SDE', 'Data Engineer'),
    prereqs LONGTEXT,
    difficulty INTEGER
);

DROP TABLE IF EXISTS profreviews;

CREATE TABLE profreviews (
    profname VARCHAR(100) PRIMARY KEY NOT NULL,
    classtaken VARCHAR(200),
    semester ENUM('Fall 2020', 'Spring 2021', 'Fall 2021', 'Spring 2022', 'Fall 2022'),
    rating INTEGER,
    reviews LONGTEXT
);

DROP TABLE IF EXISTS coursecatalog;

