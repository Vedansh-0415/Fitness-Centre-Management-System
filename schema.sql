-- Run this once to set up the database and tables
CREATE DATABASE IF NOT EXISTS fit_project;
USE fit_project;

CREATE TABLE IF NOT EXISTS user_fitness_rahi1 (
    user_id  VARCHAR(20) PRIMARY KEY,
    password VARCHAR(50) NOT NULL,
    name     VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS custmer (
    custmer_id      INT PRIMARY KEY,
    custmer_name    VARCHAR(100) NOT NULL,
    custmer_address VARCHAR(200),
    joined_date     VARCHAR(20),
    amt_paid        INT
);

CREATE TABLE IF NOT EXISTS jim_items (
    object_id           INT PRIMARY KEY,
    object_name         VARCHAR(65) NOT NULL,
    date_of_parchase    VARCHAR(65),
    repairing_data      VARCHAR(65),
    total_people_using  INT
);
