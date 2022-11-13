SET sql_safe_updates = FALSE;

USE defaultdb;
DROP DATABASE IF EXISTS coursegrained CASCADE;
CREATE DATABASE IF NOT EXISTS coursegrained;

USE coursegrained;

DROP TABLE IF EXISTS coursereviews;

-- CREATE TYPE sem AS ENUM ('Fall 2020', 'Spring 2021', 'Fall 2021', 'Spring 2022', 'Fall 2022');

CREATE TABLE coursereviews (
    id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
    coursename VARCHAR(200),
    professor  VARCHAR(100),
    semester VARCHAR(200),
    courseload INTEGER,
    reviews TEXT,
    industryroles VARCHAR(100),
    prereqs TEXT,
    difficulty INTEGER
);

DROP TABLE IF EXISTS profreviews;

CREATE TABLE profreviews (
    id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
    profname VARCHAR(100),
    classtaken VARCHAR(200),
    semester VARCHAR(200),
    rating INTEGER,
    reviews TEXT
);

DROP TABLE IF EXISTS coursecatalog;

CREATE TABLE coursecatalog (
    coursename VARCHAR(200) PRIMARY KEY NOT NULL,
    department VARCHAR(200),
    courseurl VARCHAR(200),
    description TEXT
);

DROP TABLE IF EXISTS professors;

CREATE TABLE professors (
    profname VARCHAR(100) PRIMARY KEY NOT NULL,
    pagelink VARCHAR(100),
    department VARCHAR(100)
);

DROP TABLE IF EXISTS courseinterest;

CREATE TABLE courseinterest (
    id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
    coursename VARCHAR(200),
    emailID VARCHAR(200),
    phone CHAR(10)
);